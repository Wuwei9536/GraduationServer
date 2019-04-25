from django.urls import path
from web import views

urlpatterns = [
    # 登陆接口
    path('login', views.login),
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
    # 导出excel 系统
    path('downloadexcel', views.downloadExcel),
    # 导入excel 系统
    path('uploadexcel', views.uploadExcel),
    # 获取系统用户
    path('getstudentuser', views.getStudentUser),
    # 删除学生用户
    path('deletestudentuser', views.deleteStudentUser),
    # 更新学生用户
    path('updatestudentuser', views.updateStudentUser),
    # 增加学生用户
    path('createstudentuser', views.createStudentUser),
    # 导出excel 学生
    path('downloadexcelstu', views.downloadExcelStu),
    # 导入excel 学生
    path('uploadexcelstu', views.uploadExcelStu),
    #获取登陆用户信息
    path('getcurrentuser',views.getCurrentUser)
]
