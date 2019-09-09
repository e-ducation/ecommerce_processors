# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.conf import settings
from .views import alipay, wechatpay

from . import views

app_name = 'ecommerce_processors'
urlpatterns = [
]
ALIPAY_URLS = [
    url(r'^execute/$', alipay.AlipayPaymentExecutionView.as_view(), name='execute'),
    url(r'^result/$', alipay.AlipayPaymentResultView.as_view(), name='result'),
]
WECHATPAY_URLS = [
    url(r'^order_query/(?P<pk>\d+)$', wechatpay.WechatpayOrderQuery.as_view(), name='order_query'),
    url(r'^execute/$', wechatpay.WechatpayPaymentExecutionView.as_view(), name='execute'),
]

if settings.ENABLE_ALIPAY_WECHATPAY:
    urlpatterns += [
        url(r'', include('payments.urls')),
    ]
