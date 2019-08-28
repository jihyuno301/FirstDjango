#path라는 모듈을 불러온다.
from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name="list")
]