from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的User的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的Group的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
