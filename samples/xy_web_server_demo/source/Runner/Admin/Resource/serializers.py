# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "serializers"
"""
  * @File    :   serializers.py
  * @Time    :   2024/10/31 10:32:38
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from rest_framework import viewsets
from xy_django_serializer.serializers import Serializer


from .models import MImage


class SImage(Serializer):
    default_value = ""

    class Meta:
        model = MImage
        fields = "__all__"


class VSImage(viewsets.ModelViewSet):
    queryset = MImage.objects.all()
    serializer_class = SImage
