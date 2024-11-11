"""
URL configuration for RestarentManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('displayAllRestarents/',views.displayAllRestarents,name='displayAllRestarents'),
    path('findRestarent/',views.findRestarent,name='findRestarent'),
    path('displayFItems/',views.displayFItems,name='displayFItems'),
    path('getFood/',views.getFood,name='getFood'),
    path('rinput/',views.rinput,name='rinput'),
    path('insertRRecords/',views.insertRRecords,name='insertRRecords'),
    path('insertFData/', views.insertFData,name='insertFData'),
    path('insertFRecords/',views.insertFRecords,name='insertFRecords'),
    path('delateRData/',views.delateRData,name='delateRData'),
    path('delateRRecords/',views.delateRRecords,name='delateRRecords'),
    path('delateFdata/',views.delateFdata,name='delateFdata'),
    path('delateFRecords/',views.delateFRecords,name='delateFRecords'),
    path('uRData/',views.uRData,name='uRData'),
    path('updateRRecords/',views.updateRRecords,name='updateRRecords'),
    path('updateRRs/',views.updateRRecords,name='updateRRs'),
    path('uFData/',views.uFData,name='uFData'),
    path('updateFRecords/',views.updateFRecords,name='updateFRecords'),

    path('about/',views.about,name='about'),

    path('displayFRREST/',views.displayFRREST,name='displayFRREST'),
    path('displayRRREST/',views.displayRRREST,name='displayRRREST'),
    path('findRestarentREST/',views.findRestarentREST,name='findRestarentREST'),
    path('getFoodREST/',views.getFoodREST,name='getFoodREST'),
    path('insertRRRest/',views.insertRRRest,name='insertRRRest'),
    path('delateRRREST/',views.delateRRREST,name='delateRRREST'),
    path('insertFRREST/',views.insertFRREST,name='insertFRREST'),
    path('delateFRREST/',views.delateFRREST,name='delateFRREST'),
    path('updateRRREST/',views.updateRRREST,name='updateRRREST'),



    path('bdelate/<int:restarentId>/',views.bdelate,name='bdelate'),
    path('bupdate/<int:restarentId>',views.bupdate,name='bupdate'),
    





]
