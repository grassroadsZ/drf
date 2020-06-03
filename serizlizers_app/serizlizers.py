# -*- encoding:utf-8 -*-
"""
@Author: grassroadsZ
@data: 2020/5/15 18:07
@file: serizlizers
"""

from rest_framework import serializers
from .models import SerizlizerApp, LANGUAGE_CHOICES, STYLE_CHOICES


class SerizlizerSerizlers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.CharField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.CharField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        return SerizlizerApp.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
