"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from theapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('404/', views.error, name='error'),
    path('blank/', views.blank, name='blank'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('charts/', views.charts, name='charts'),
    path('forgot-password/', views.password, name='password'),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tables/', views.tables, name='tables'),
    path('utilities-animation/', views.animation, name='animation'),
    path('utilities-border/', views.border, name='border'),
    path('utilities-color/', views.color, name='color'),
    path('utilities-other/', views.other, name='other'),
    path('participating-vote/', views.participate, name='participate'),
    path('completion-participating-vote/', views.completion_participate, name='completion-participate'),
    path('mypage/',views.mypage, name='mypage'),
    path('notice/',views.notice, name='notice'),
    path('suggest-vote/',views.suggest_vote, name='suggest-vote'),
    path('suggest-other/',views.suggest_other, name='suggest-other'),
    path('main/',views.main, name='main'),
    path('school-vote/', views.school_vote, name='school-vote'),
    path('college-vote/', views.college_vote, name='college-vote'),
    path('department-vote/', views.department_vote, name='department-vote'),
    path('make-vote/', views.make_vote, name='make-vote'),
    path('school-voting/', views.school_voting, name='school-voting'),
    path('school-pledge/', views.school_pledge, name='school-pledge'),
    path('college-voting/', views.college_voting, name='college-voting'),
    path('college-pledge/', views.college_pledge, name='college-pledge'),
    path('department-voting/', views.department_voting, name='department-voting'),
    path('department-pledge/', views.department_pledge, name='department-pledge'),
    path('result/',views.result, name='vote-result'),
]
