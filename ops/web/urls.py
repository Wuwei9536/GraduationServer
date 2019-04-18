from django.urls import path
from web import views

urlpatterns = [
    path('systemuser', views.system_user),
    path('createsystemuser', views.create_system_user),
]