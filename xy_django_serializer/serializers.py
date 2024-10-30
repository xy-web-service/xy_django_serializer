# -*- coding: UTF-8 -*-

from typing import Dict
from rest_framework import routers, serializers, viewsets
from collections import OrderedDict
from rest_framework import serializers
from rest_framework.fields import SkipField


# Serializers define the API representation.
class serializer(serializers.ModelSerializer):

    default_value = None
    default_value_map = {}
    filtered_fields = ["id"]

    @classmethod
    def initial(
        cls,
        instance=None,
        default_value=None,
        default_value_map=None,
        filtered_fields=None,
        *args,
        **kwargs,
    ):
        admin_model_serializer = cls(instance)
        admin_model_serializer.default_value = default_value
        if default_value_map != None and type(default_value_map) == type({}):
            admin_model_serializer.default_value_map = default_value_map
        if filtered_fields != None and type(filtered_fields) == type([]):
            admin_model_serializer.filtered_fields = filtered_fields
        return admin_model_serializer

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            try:
                if not value:
                    if key in self.default_value_map.keys():
                        data[key] = self.default_value_map.get(key)
                    else:
                        data[key] = self.default_value
            except KeyError:
                continue
            except:
                continue
        dataCache = data.copy()
        for key in dataCache.keys():
            if self.filtered_fields and key in self.filtered_fields:
                del data[key]
        return data
