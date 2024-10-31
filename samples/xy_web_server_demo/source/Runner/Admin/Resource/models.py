# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "models"
"""
  * @File    :   models.py
  * @Time    :   2024/10/31 10:11:32
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""


import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models

from xy_django_model.model import gen_upload_to


# Create your models here.
@gen_upload_to
def images(instance=None, filename=None):
    pass


class MImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_at = models.DateTimeField(
        verbose_name=_("创建时间"),
        auto_now_add=True,
        editable=True,
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"),
        auto_now_add=True,
        editable=True,
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("是否启用"),
        null=True,
        blank=True,
        default=False,
    )
    image = models.ImageField(
        verbose_name=_("图片"),
        upload_to=images,
        null=True,
        blank=True,
        default=None,
        help_text=_("图片"),
    )

    class Meta:
        verbose_name = _("图片")
        verbose_name_plural = _("图片")
        app_label = "Resource"

    def __str__(self):
        return f"{self.id}. {self.identifier}"
