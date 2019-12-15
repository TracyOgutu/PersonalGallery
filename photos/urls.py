from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^singlephoto/(\d+)',views.singlephoto,name='singlephoto'),
    url(r'^search/', views.search_category, name='search_category'),
    url(r'^searchlocation/', views.search_location, name='search_location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)