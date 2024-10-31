# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "serializers"
"""
  * @File    :   serializers.py
  * @Time    :   2024/10/31 09:11:39
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from rest_framework import viewsets
from xy_django_serializer.serializers import Serializer

from .models import MDemo
from Resource.serializers import SImage


class SDemo(Serializer):
    default_value = ""
    image = SImage(
        many=False,
        read_only=True,
    )

    class Meta:
        model = MDemo
        fields = "__all__"


class VSDemo(viewsets.ModelViewSet):
    queryset = MDemo.objects.all()
    serializer_class = SDemo
