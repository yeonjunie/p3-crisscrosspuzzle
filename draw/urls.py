# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    url(r'^studentinterface$', views.StudentInterface, name='student'),
    url(r'^teacherinterface$',views.TeacherInterface, name='teacher'),
    url(r'^success$',views.Success, name ='success'),
]

