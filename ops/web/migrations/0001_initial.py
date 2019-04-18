# Generated by Django 2.2 on 2019-04-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(default='123456', max_length=20)),
                ('status', models.IntegerField(default=0, max_length=1)),
                ('homedirectory', models.CharField(max_length=30)),
                ('groupname', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '系统用户',
                'db_table': 'user_sys',
                'ordering': ('create_time',),
            },
        ),
    ]
