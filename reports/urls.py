from django.urls import re_path
from . import views


urlpatterns = [
    re_path('show/',views.show_my_reports),
    re_path('create/',views.create_report),
    #re_path(r'^update/governorate/(?P<governorate_id>\d+)/$',views.update_governorate),
]
