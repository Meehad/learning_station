from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home.html',views.home,name='home'),
    path('mulern.html',views.mulern,name='mulern'),
    path('cc.html',views.cc,name='cc'),
    path('domains.html',views.domains,name='domains'),
    path('feedback.html',views.feedback,name='feedback'),
    path('wd.html',views.wd,name='wd'),
    path('md.html',views.md,name='md'),
    path('mark.html',views.mark,name='mark'),
    path('blc.html',views.blc,name='blc'),
    path('aidv.html',views.aidv,name='aidv'),
    path('ar.html',views.ar,name='ar'),
    path('csec.html',views.csec,name='csec'),
    path('pm.html',views.pm,name='pm'),
    path('uix.html',views.uix,name='uix'),
    path('gd.html',views.gd,name='gd'),
    path('lno.html',views.lno,name='lno'),
    path('iot.html',views.iot,name='iot'),
    path('devops.html',views.devops,name='devops'),
    path('flut.html',views.flut,name='flut'),
]