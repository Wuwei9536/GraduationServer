from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from web.models import UserSystem, Equipment, Cpu
from web.serializers import UserSystemSerializer, EquipmentSerializer, CpuSerializer
import time
from datetime import datetime


@csrf_exempt
# 登陆login
def system_user(request):
    params = request.GET  # 获取Get参数
    systemUser = UserSystem.manager.filter(
        name=params['userName'], password=params['password'])  # QuerySet对象
    systemUserSerializer = UserSystemSerializer(
        systemUser, many=True)  # 序列化后的QuerySet对象    数据在 QuerySet.data 里
    if len(systemUser) > 0:  # 计算数组长度需要用QuerySet对象
        return JsonResponse({'status': 'ok', 'data': systemUserSerializer.data, 'currentAuthority': 'admin', 'type': params['type']}, safe=False)
    else:
        return JsonResponse({'status': 'error', 'data': '您还未注册', 'currentAuthority': 'guest', 'type': params['type']})


@csrf_exempt
# 注册
def create_system_user(request):
    dic = {'name': 'wien', 'password': "123"}
    UserSystem.manager.create(**dic)
    systemUser = UserSystem.manager.filter(name='wien')
    systemUserSerializer = UserSystemSerializer(systemUser, many=True)
    return JsonResponse(systemUserSerializer.data, safe=False)


@csrf_exempt
# equipment
def getEquipmentData(request):  # param equip_name:设备名称 status：使用状态
    # params = request.GET
    equipments = Equipment.manager.all()  # 遍历到底是遍历queryset呢还是序列化后的data呢
    equipmentsSerializer = EquipmentSerializer(equipments, many=True)
    for item in equipmentsSerializer.data:
        cpu = Cpu.manager.filter(equip_id=item['id'])
        cpuSerializer = CpuSerializer(cpu, many=True)
        timeArray = time.strptime(cpuSerializer.data[0]['check_time'], '%Y-%m-%dT%H:%M:%S') #东八区时间转换成时间元组
        timestamp = time.mktime(timeArray)*1000 # 时间元组转换成时间戳（以秒为单位）所以要乘以1000
    return JsonResponse(cpuSerializer.data, safe=False)
