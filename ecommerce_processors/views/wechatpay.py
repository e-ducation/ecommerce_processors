import json
import logging
import requests

from django.urls import reverse
from django.conf import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from oscar.core.loading import get_model
from ecommerce.extensions.checkout.utils import get_receipt_page_url
from ecommerce.extensions.payment.processors.wechatpay import WechatPay
from ecommerce.extensions.payment.views.alipay import AlipayPaymentExecutionView, AlipayPaymentResultView
from payments.wechatpay.wxpay import OrderQuery_pub, Wxpay_server_pub

Basket = get_model('basket', 'Basket')
Order = get_model('order', 'Order')
PaymentProcessorResponse = get_model('payment', 'PaymentProcessorResponse')

logger = logging.getLogger(__name__)


class WechatpayPaymentExecutionView(AlipayPaymentExecutionView):

    @property
    def payment_processor(self):
        return WechatPay(self.request.site)

    def verify_data(self, data):
        """ verify request """
        try:
            verify_srv = Wxpay_server_pub()
            verify_srv.saveData(data)
            return verify_srv.checkSign(), verify_srv.getData()
        except Exception, e:
            logger.exception(e)
        return False, {}


class WechatpayOrderQuery(APIView):

    NOTPAY = 1
    SUCCESS = 2
    PAID = 3
    START_QUERY_TIME = 300
    PAYQUERY_KEY_EXPIRED = 3600

    def get(self, request, pk):
        '''
        query order
        GET /payment/wechatpay/order_query/{basket.id}
        '''
        status = self.NOTPAY
        receipt_url = ''
        try:
            basket = Basket.objects.get(owner=request.user, id=pk)
            order = Order.objects.filter(number=basket.order_number, status='Complete')
            payquery_key = 'payquery_{}'.format(basket.id)
            payquery_time_key = 'payquery_time_{}'.format(basket.id)
            if basket.status == 'Submitted':
                status = self.PAID
            else:
                if not cache.get(payquery_time_key):
                    if not cache.get(payquery_key):
                        cache.set(payquery_key, 1, self.PAYQUERY_KEY_EXPIRED)
                        cache.set(payquery_time_key, 1, self.START_QUERY_TIME)
                    elif cache.get(payquery_key):
                        status, resp = self.wechatpay_query(basket)
                        if status == self.PAID and not order:
                            post_data = {'original_data': json.dumps({'data': resp})}
                            requests.post(settings.ECOMMERCE_URL_ROOT + reverse('wechatpay:execute'), data=post_data)

            if status == self.PAID and order:
                receipt_url = get_receipt_page_url(
                    order_number=basket.order_number,
                    site_configuration=basket.site.siteconfiguration
                )
                status = self.SUCCESS
                cache.delete(payquery_key)
        except Exception, e:
            logger.exception(e)

        return Response({
            'status': status,
            'receipt_url': receipt_url,
        })

    @classmethod
    def wechatpay_query(cls, basket):
        '''
        query pay result
        '''
        orderquery_pub = OrderQuery_pub()
        pay_resp = PaymentProcessorResponse.objects.get(processor_name=WechatPay.NAME, basket=basket)
        resp = pay_resp.response
        orderquery_pub.setParameter('out_trade_no', pay_resp.transaction_id)
        trade_no = resp.get('trade_no')
        if trade_no:
            orderquery_pub.setParameter('transaction_id', trade_no)

        result = orderquery_pub.getResult()
        logger.info(result)
        if result.pop('sign') == orderquery_pub.getSign(result) and result.get('trade_state') == 'SUCCESS':
            return cls.PAID, orderquery_pub.response
        return cls.NOTPAY, ''
