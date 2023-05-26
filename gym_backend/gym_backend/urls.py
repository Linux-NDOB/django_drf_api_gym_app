"""
URL configuration for gym_backend project.

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
from django.urls import re_path
from gym_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^api/admins/$', views.admin_list),
    re_path(r'^api/admins/([0-9])$', views.admin_actions),

    re_path(r'^api/persons/$', views.person_list),
    re_path(r'^api/persons/([0-9])$', views.person_actions),

    re_path(r'^api/actives/$', views.actives_list),
    re_path(r'^api/actives/([0-9])$', views.actives_actions),

    re_path(r'^api/reports/$', views.reports_list),
    re_path(r'^api/reports/([0-9])$', views.reports_actions),
]
