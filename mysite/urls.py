"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp.views import home_view, indexdos_view, ho_view, indextres_view, indexcuatro_view, indexcinco_view, indexseis_view, indexsiete_view, iframe_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='hello'),
    path('ho/', ho_view, name='ho'),
    path('indexdos/', indexdos_view, name='indexdos'),
    path('indextres/', indextres_view, name='indextres'),
    path('indexcuatro/', indexcuatro_view, name='indexcuatro'), 
    path('indexcinco/', indexcinco_view, name='indexcinco'),  
    path('indexseis/', indexseis_view, name='indexseis'), 
    path('indexsiete/', indexsiete_view, name='indexsiete'),
    path('iframe/', iframe_view, name='iframe'),  
]
