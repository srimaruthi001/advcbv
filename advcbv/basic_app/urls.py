from django.conf.urls import url, include
from . import views

app_name='basic_app'

urlpatterns=[
    url(r'^$',views.SchoolList.as_view(),name='list')

]
