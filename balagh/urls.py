from django.urls import re_path,include
urlpatterns = [
    re_path('auth/', include('authenticate.urls')),
    re_path('location/',include('locations.urls')),
    re_path('report/',include('reports.urls')),
]
