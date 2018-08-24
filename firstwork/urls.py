"""firstwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^student/', views.student, name='student'),
    url(r'^get_student/', views.get_student, name='get_student'),
    url(r'^video-(?P<direction_id>(\d+))-(?P<classification_id>(\d+))-(?P<level_id>(\d+))/$', views.video, name='video'),
]
