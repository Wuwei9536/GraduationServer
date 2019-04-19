from rest_framework import serializers
from web.models import UserSystem, Equipment,Cpu


class UserSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSystem
        fields = ('id', 'name', 'password', 'status',
                  'homedirectory', 'groupname')


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'equip_name', 'ip', 'node_type', 'cpu_model',
                  'core_num', 'storage', 'disk', 'isagent', 'remarks')


class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = ('id', 'equip_id', 'usage_rate', 'check_time')
