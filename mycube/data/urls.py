from django.conf.urls import url
from . import views

urlpatterns = [

    # /data/00-00-0000
    url(r'^(?P<date>[0-9]{8})/$', views.detail , name = 'detail' ),
    url(r'^$', views.index, name = 'index'),

]
