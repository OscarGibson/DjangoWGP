from django.conf.urls import url
from .views import gener_push

urlpatterns = [
	url(r'gener_push', gener_push, name= 'gener_push'),
]