#coding=utf-8
from django.conf.urls import patterns, include, url
from app import views

urlpatterns = [
    # url(r'^$',  views.index),
    url(r'^$',  views.welcome),
    url(r'^welcome', views.welcome), # 欢迎页面，介绍目的，感谢团队
    url(r'^index',  views.index), # index 页面
    url(r'^autism$', views.autism), # 孤独症；儿童孤独症；孤独性
    url(r'^schizophrenia$', views.schizophrenia), # 精神分裂症；早发性痴呆
    url(r'^depression$', views.depression), # 忧郁症；萧条；消沉
    url(r'^concern$', views.concern), # 关注；忧虑
    url(r'^care$', views.care), # 护理；照顾
    
]
