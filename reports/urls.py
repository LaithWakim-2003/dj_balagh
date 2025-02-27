from django.urls import re_path
from . import views


urlpatterns = [
    re_path('show/',views.show_my_reports),
    re_path('create/',views.create_report),
    re_path(r'^update/(?P<report_id>\d+)/$',views.update_report),
    re_path(r'^delete/(?P<report_id>\d+)/$',views.delete_report),
]
