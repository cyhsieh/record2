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
from testapp import views as testviews
from django.urls import path, re_path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('record_cv/', views.RecordListView.as_view()),
    # path('record/<int:pk>', views.RecordDetailView.as_view(), name='record-detail'),
    re_path('^record/(?P<pk>\d+)$', views.RecordDetailView.as_view(), name='record-detail'),
    url(r'^$', views.list_record, name='list_record'),
    # url(r'^list_bulletin$', views.list_bulletin),
    # url(r'^new_bulletin$', views.new_bulletin),
    # url(r'^edit_bulletin/(\d+)/$', views.edit_bulletin),
    url(r'^list_record/$', views.list_record),
    re_path('^list_record2/(?P<page>\d+)$', views.list_record2, name="list_record2"),
    path('new_record3/', views.recordform, name="new_record3"),
    re_path('^edit_record3/(?P<pk>\d+)$', views.recordform, name="edit_record3"),
    # url(r'^new_record/$', views.new_record),
    url(r'^new_record2/$', views.new_record2, name='new_record2'),
    url(r'^new_record_cli/$', views.new_record_cli, name='new_record_cli'),
    url(r'^edit_record/(\d+)/$', views.edit_record),
    url(r'^delete_record/(\d+)/$', views.delete_record),
    url(r'^testindex/$', testviews.testindex),
    # url(r'^movie_base/$', movieviews.movie_base),
    # url(r'^movie_list/$', movieviews.movie_list),
    #url(r'^new_record/$', views.new_record),
    # url(r'^edit_record/$', views.edit_record),
    path('list_tobuy/', views.TobuyItemView.as_view(), name="list_tobuy"),
    path('new_tobuy/', views.TobuyForm, name="new_tobuy"),
    re_path('^edit_tobuy/(?P<pk>\d+)$', views.TobuyForm, name="edit_tobuy"),
]
