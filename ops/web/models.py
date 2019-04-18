from django.db import models

# Create your models here.


class UserSystem(models.Model):
    # 姓名
    name = models.CharField(max_length=30)
    # 密码
    password = models.CharField(default='123456', max_length=20)
    # 登陆状态 默认0：离线  1:登陆
    status = models.IntegerField(default=0)
    homedirectory = models.CharField(max_length=30, blank=True)
    groupname = models.CharField(max_length=30, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    manager = models.Manager()

    class Meta:
        db_table = 'user_sys'  # 自定义表名称为user_sys
        verbose_name = '系统用户'  # 指定在admin管理界面中显示的名称
        ordering = ('create_time',)
