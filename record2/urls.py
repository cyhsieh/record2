"""record2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from record2app import views
from movies import views as movieviews
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.list_record),
    # url(r'^list_bulletin$', views.list_bulletin),
    # url(r'^new_bulletin$', views.new_bulletin),
    # url(r'^edit_bulletin/(\d+)/$', views.edit_bulletin),
    url(r'^list_record/$', views.list_record),
    # url(r'^new_record/$', views.new_record),
    url(r'^new_record2/$', views.new_record2),
    url(r'^edit_record/(\d+)/$', views.edit_record),
    # url(r'^movie_base/$', movieviews.movie_base),
    # url(r'^movie_list/$', movieviews.movie_list),
    #url(r'^new_record/$', views.new_record),
    # url(r'^edit_record/$', views.edit_record),
]
