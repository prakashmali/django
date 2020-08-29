"""Restaurant URL Configuration

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
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home', views.home,name='home'),
    path('add', views.add,name='add'),
    path('dises/<int:pk>', views.dises,name='dises'),
    
    path('delete/<int:pk>', views.delete,name='dises'),

    path('edit', views.editSave,name='dises'),
    path('edit/<int:pk>', views.edit,name='dises'),

    path('editdises', views.editSaveDises,name='dises'),
    path('editdises/<int:res_id>/<int:pk>', views.editDises,name='dises'),

    path('deletedises/<int:res_id>/<int:pk>', views.deleteDises,name='dises'),
    path('adddis', views.addDis,name='add'),
    path('dises/billing/<int:res_id>', views.billing,name='billing'),

    path('dises/billdata/', views.billData,name='add'),
    path('billview', views.billview,name='add'),


]
