from django.conf.urls import url
from .views import index

urlpatterns = [
    url(r'(?P<slug>^[0-9a-z^\/]*)', index, name= 'index'),
]