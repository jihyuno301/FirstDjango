"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from first import views
from django.urls import path, include

urlpatterns = [
    #도메인을 치고 들어오자마자 바로 보여지는 페이지는 index메소드의 응답값으로 하겠다
    #path('', views.index, name='index'),
    #첫번째 인자값에 패스경로를 설정하면 url이 first/까지 가게 하기위함이다.
    path('first/', include('first.urls')),
    path('second/', include('second.urls')),
    path('admin/', admin.site.urls),

]
