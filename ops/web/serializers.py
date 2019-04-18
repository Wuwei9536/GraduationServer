from rest_framework import serializers
from web.models import UserSystem


class UserSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSystem
        fields = ('id', 'name', 'password', 'status', 'homedirectory', 'groupname')
