from django.urls import path
from web import views

urlpatterns = [
    # 登陆接口
    path('systemuser', views.system_user),
    # 创建系统用户
    path('createsystemuser', views.createSystemUser),
    # 获取设备列表
    path('equipment', views.getEquipmentData),
    # 获取系统用户
    path('getsystemuser', views.getSystemUser),
    # 删除系统用户
    path('deletesystemuser', views.deleteSystemUser),
    # 更新系统用户
    path('updatesystemuser', views.updateSystemUser),
    path('excel', views.excel)

]
