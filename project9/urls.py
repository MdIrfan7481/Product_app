"""
URL configuration for project9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from productapp.views import Homeview,Insertview,InsertInput,DeleteView,Dispalyview,UpdateView,UpdateInputView,DeleteInputView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',Homeview.as_view()),
    path('Home/insertinput/',InsertInput.as_view()),
    path('Home/insertinput/insert/',Insertview.as_view()),
    path('Home/display/',Dispalyview.as_view()),
    path('Home/deleteinput/',DeleteInputView.as_view()),
    path('Home/deleteinput/delete/',DeleteView.as_view()),
    path('Home/updateinput/',UpdateInputView.as_view()),
    path('Home/updateinput/update/',UpdateView.as_view()),
]
