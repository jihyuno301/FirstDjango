#path라는 모듈을 불러온다.
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #select path경로로 접근하면
    #마지막에 /를 써줘야한다.
    #정적이 페이지
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),

]