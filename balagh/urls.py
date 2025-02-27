from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path,include
urlpatterns = [
    re_path('auth/', include('authenticate.urls')),
    re_path('location/',include('locations.urls')),
    re_path('report/',include('reports.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
