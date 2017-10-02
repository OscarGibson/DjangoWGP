from django.conf.urls import url
from .views import post

urlpatterns = [
	url(r'(?P<post_id>[0-9a-z\-]+)', post, name= 'post'),
]