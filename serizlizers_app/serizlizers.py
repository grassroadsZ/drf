# -*- encoding:utf-8 -*-
"""
@Author: grassroadsZ
@data: 2020/5/15 18:07
@file: serizlizers
"""

from rest_framework import serializers
from .models import SerizlizerApp


class SerizlizerSerizlers(serializers.ModelSerializer):
    class Meta:
        model = SerizlizerApp
        fields = ('id','title', 'code', 'linenos', 'language', 'style')
