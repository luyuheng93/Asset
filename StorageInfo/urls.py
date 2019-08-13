#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path
from StorageInfo import views


app_name = 'StorageInfo'
urlpatterns = [
    #path('report/', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/<int:asset_id>/', views.detail, name='detail'),
    path('storagedetail/<int:asset_id>/', views.storagedetail, name='storagedetail'),
    path('sanswitchdetail/<int:asset_id>/', views.sanswitchdetail, name='sanswitchdetail'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('asset_coding/', views.asset_coding, name='asset_coding'),
    path('', views.dashboard),
]






