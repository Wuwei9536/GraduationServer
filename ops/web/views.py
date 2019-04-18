from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from web.models import UserSystem
from web.serializers import UserSystemSerializer


@csrf_exempt
def system_user(request):
    params = request.GET  # 获取Get参数
    print(params['userName'],params['password'])
    systemUser = UserSystem.manager.filter(
        name=params['userName'], password=params['password'])  # QuerySet对象
    systemUserSerializer = UserSystemSerializer(
        systemUser, many=True)  # 序列化后的QuerySet对象
    print('systemUser', len(systemUser))
    if len(systemUser) > 0:
        return JsonResponse({'status': 'ok', 'data': systemUserSerializer.data, 'currentAuthority': 'admin', 'type': params['type']}, safe=False)
    else:
        a = JsonResponse({'status': 'error', 'data': '您还未注册',
                          'currentAuthority': 'guest'})
        print(a)
        return JsonResponse({'status': 'error', 'data': '您还未注册', 'currentAuthority': 'guest'})


def create_system_user(request):
    dic = {'name': 'wien', 'password': "123"}
    UserSystem.manager.create(**dic)
    systemUser = UserSystem.manager.filter(name='wien')
    systemUserSerializer = UserSystemSerializer(systemUser, many=True)
    return JsonResponse(systemUserSerializer.data, safe=False)
