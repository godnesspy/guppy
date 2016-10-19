# -*- coding: utf-8 -*-
""""""
import json

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

default_logo = "http://www.logoquan.com/upload/list/20160911/logoquan14762469644.PNG"


class ConsumerTest(APITestCase):
    """"""

    def test_register(self):
        """"""
        data = {
            'username': 'test1',
            'password': 'test1',
            'email': '7jgffi@163.com'
        }
        r = self.client.post('/consumer/', data=data, format='json')
        self.assertEqual(r.status_code, 201)
        content = json.loads(r.content)
        self.assertEqual(content['username'], data['username'])

    def test_consumer(self):
        """"""
        import datetime
        u = User.objects.create_user(
            username='guppy',
            password='test',
            email='dgfygii@163'
        )
        u.save()
        print(u.id)
        data = {
            "user_id": 1,
            "nick_name": "ddfdf",
            "avatar": default_logo,
            "phone": '18780454407',
            "pay_pwd": "bigbird",
            "sex": "M",
            "age": 22,
            "birthday": datetime.date(1970, 1, 1),
            "live_city": 1,
            "qq_num": "6348967",
            "wx_num": "reyvgrr"
        }
        r = self.client.post('/consumer/profile/', data=data, format='json')
        self.assertEqual(201, r.status_code)
        print(json.loads(r.content))