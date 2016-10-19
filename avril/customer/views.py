# -*- coding: utf-8 -*-
""""""

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Consumer as UserProfile
from .serializers import UserSerializer, DisplayConsumerSerializer


class Consumer(APIView):
    """Register and update user, consumer."""

    def post(self, request, format='json'):
        """"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ConsumerView(APIView):
    """"""

    def post(self, request):
        """"""
        user = get_object_or_404(User, pk=request.data.get('user_id'))
        up = UserProfile(
            user=user,
            nick_name=request.data['nick_name'],
            avatar=request.data['avatar'],
            phone=request.data['phone'],
            sex=request.data['sex'],
            age=request.data['age'],
            birthday=request.data['birthday'],
            live_city=request.data['live_city'],
            qq_num=request.data['qq_num'],
            wx_num=request.data['wx_num']
        )
        up.create_pay_password(request.data['pay_pwd'])
        up.save()
        serializer = DisplayConsumerSerializer(up)
        return Response(serializer.data, status.HTTP_201_CREATED)
