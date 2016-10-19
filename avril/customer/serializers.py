# -*- coding: utf-8 -*-
""""""

from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Consumer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class DisplayConsumerSerializer(serializers.ModelSerializer):
    """"""
    user = UserSerializer(read_only=True)

    class Meta:
        model = Consumer
        # exclude = ("pay_pwd", )
        extra_kwargs = {
            'pay_pwd': {'write_only': True}
        }
