from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from web.models import UserSystem, Equipment, Cpu
from web.serializers import UserSystemSerializer, EquipmentSerializer, CpuSerializer
import time
import json
import xlwt
from io import BytesIO
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


# 注册 增加系统用户

@csrf_exempt
def createSystemUser(request):
    params = json.loads(request.body)
    UserSystem.manager.create(**params)
    systemUser = UserSystem.manager.filter(name=params['name'])
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
        timeArray = time.strptime(
            cpuSerializer.data[0]['check_time'], '%Y-%m-%dT%H:%M:%S')  # 东八区时间转换成时间元组
        timestamp = time.mktime(timeArray)*1000  # 时间元组转换成时间戳（以秒为单位）所以要乘以1000
    return JsonResponse(cpuSerializer.data, safe=False)


@csrf_exempt
# 拉取系统用户
def getSystemUser(request):
    params = request.GET.dict()  # 获取Get参数
    if(params):
        if('name' in params and 'homedirectory' in params):
            systemUser = UserSystem.manager.filter(
                name=params['name'], homedirectory=params['homedirectory'])
        elif('name' in params):
            systemUser = UserSystem.manager.filter(name=params['name'])
        else:
            systemUser = UserSystem.manager.filter(
                homedirectory=params['homedirectory'])
    else:
        systemUser = UserSystem.manager.all()
    systemUserSerializer = UserSystemSerializer(systemUser, many=True)
    res = []
    for item in systemUserSerializer.data:
        res.append({
            'key': item['id'],
            'name': item['name'],
            'status': item['status'],
            'catalogue': item['homedirectory'],
            'group': item['groupname'],
        })
    return JsonResponse(res, safe=False)


# 删除系统用户

@csrf_exempt
def deleteSystemUser(request):
    params = request.GET
    res = UserSystem.manager.filter(id=params['id'])
    # 序列化必须在res.delete之前，否则res就不存在了。
    resData = UserSystemSerializer(res, many=True)
    systemUser = res.delete()
    return JsonResponse(resData.data, safe=False)


# 更新系统用户

@csrf_exempt
def updateSystemUser(request):
    # request.body 是二进制数据， json.loads转换未json格式
    params = json.loads(request.body)
    res = UserSystem.manager.filter(id=params['id'])
    # 序列化必须在res.delete之前，否则res就不存在了。
    resData = UserSystemSerializer(res, many=True)
    systemUser = res.update(**params)  # **就是js里的...
    return JsonResponse(resData.data, safe=False)


@csrf_exempt
def excel(request):
  # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=order.xls'
    # 创建一个文件对象
    wb = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet对象
    sheet = wb.add_sheet('order-sheet')


    # 写入文件标题
    sheet.write(0, 0, '申请编号')
    sheet.write(0, 1, '客户名称')
    sheet.write(0, 2, '联系方式')
    sheet.write(0, 3, '身份证号码')
    sheet.write(0, 4, '办理日期')
    sheet.write(0, 5, '处理人')
    sheet.write(0, 6, '处理状态')
    sheet.write(0, 7, '处理时间')

    # # 写入数据
    # data_row = 1
    # # UserTable.objects.all()这个是查询条件,可以根据自己的实际需求做调整.
    # for i in UserTable.objects.all():
    #     # 格式化datetime
    #     pri_time = i.pri_date.strftime('%Y-%m-%d')
    #     oper_time = i.operating_time.strftime('%Y-%m-%d')
    #     sheet.write(data_row, 0, i.loan_id)
    #     sheet.write(data_row, 1, i.name)
    #     sheet.write(data_row, 2, i.user_phone)
    #     sheet.write(data_row, 3, i.user_card)
    #     sheet.write(data_row, 4, pri_time)
    #     sheet.write(data_row, 5, i.emp.emp_name)
    #     sheet.write(data_row, 6, i.statu.statu_name)
    #     sheet.write(data_row, 7, oper_time)
    #     data_row = data_row + 1

    # 写出到IO
    output = BytesIO()
    wb.save(output)
    # 重新定位到开始
    output.seek(0)
    response.write(output.getvalue())
    return response
