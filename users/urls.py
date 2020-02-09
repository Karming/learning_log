# @Time : 2020/2/8 17:37 

# @Author : karming

# @File : urls.py 

# @Description:
"""为应用程序users定义URL模式"""
from django.conf.urls import url

from django.contrib.auth.views import LoginView
from . import views

# LoginView.as_view后面要加上()
urlpatterns =[
    #登录页面
    url(r'^login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 注销
    url(r'^logout/', views.logout_view, name='logout'),
    # 注册页面
    url(r'^register/', views.register, name='register'),
]
