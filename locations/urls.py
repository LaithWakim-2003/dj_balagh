from django.urls import re_path
from . import views


urlpatterns = [
    re_path('show/governorates/',views.get_governorates),
    re_path('create/governorate/',views.create_governorate),
    re_path(r'^update/governorate/(?P<governorate_id>\d+)/$',views.update_governorate),
    re_path(r'^delete/governorate/(?P<governorate_id>\d+)/$',views.delete_governorate),
    
    re_path(r'^show/cities/(?P<governorate_id>\d+)/$',views.get_cities),
    re_path('create/city/',views.create_city),
    re_path(r'^update/city/(?P<city_id>\d+)/$',views.update_city),
    re_path(r'^delete/city/(?P<city_id>\d+)/$',views.delete_city),

]
