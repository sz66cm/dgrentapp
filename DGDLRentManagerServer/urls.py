"""DGDLRentManagerServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ManagerApp import views as mav
from ManagerApp.operation import operation_add

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_user_type_page/$', mav.show_add_user_type_page),
    url(r'^add_user_type/$',operation_add.add_user_type),
    url(r'^add_user_page/$', mav.show_add_user_page),
    url(r'^add_user/$', operation_add.add_user),
    
]
