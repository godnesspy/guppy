# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import Consumer, ConsumerView

urlpatterns = [
    url(r'^auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^verify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^register/$', Consumer.as_view()),    # register.
    url(r'^profile/$', ConsumerView.as_view())  # 补充用户资料
]
