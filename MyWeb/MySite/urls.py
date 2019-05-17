from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
	url('trans/', views.translate),
	url(r'^news_list/(\d+)', views.news_list),
	url(r'filter/', views.filter_test),
	url('all/', views.search_all),
	url('search_name', views.search_name),
	url('search_price', views.search_price),
	url('search_sort', views.searchsort),
	url('reg/', views.reg),  # 注册界面
	url('register/', views.register),  # 提交注册
	url('check/', views.check),  # 检查用户名是否注册
	url('change/', views.change),  # 打开修改密码页面
	url('changepass/', views.changepass),  # 提交密码修改

]