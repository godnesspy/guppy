# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password


class Consumer(models.Model):
    """"""
    SEX_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
        ('U', 'unknown')
    )

    user = models.OneToOneField(User)   # username, password, email

    nick_name = models.CharField('昵称', max_length=64, default="")
    avatar = models.URLField('头像', default="")
    phone = models.CharField('电话', max_length=16)

    vip_source = models.IntegerField('会员分数', default=0)
    vip_level = models.IntegerField('会员等级', default=1)
    pay_pwd = models.CharField('支付密码', max_length=128)

    sex = models.CharField('性别', max_length=1, choices=SEX_CHOICES, default='U')
    age = models.IntegerField('年龄', default=0)
    birthday = models.DateField('生日', default=datetime.date(1970, 1, 1))
    live_city = models.IntegerField('所在城市', default=0)
    qq_num = models.CharField('QQ', max_length=16, default="")
    wx_num = models.CharField('微信', max_length=64, default="")
    is_delete = models.IntegerField('是否删除', default=0)  # 0: 有效, 1: 删除
    created_at = models.DateTimeField('注册时间', auto_now=True)
    updated_at = models.DateTimeField('更新时间', auto_now_add=True)

    class Meta:
        db_table = 'consumer'
        ordering = ('-updated_at', )

    def __str__(self):
        return 'username:{0}'.format(self.user.username)

    def create_pay_password(self, raw):
        """"""
        self.pay_pwd = make_password(raw)

    def check_pay_password(self, raw):
        """"""
        # return self.pay_pwd == make_password(raw)
        def setter(raw_password):
            self.create_pay_password(raw_password)
            self.save(update_fields=["pay_pwd"])
        return check_password(raw, self.pay_pwd, setter)

    def calc_vip_level(self):
        """:return user`s vip level"""
        _source = 3 ** self.vip_level
        return self.vip_source // _source