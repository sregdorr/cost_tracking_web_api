from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

router = routers.DefaultRouter()

router.register(r'clients', views.ClientViewSet, base_name='client')
router.register(r'projects', views.ProjectViewSet, base_name='project')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', views.schema_view),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework'))

]

