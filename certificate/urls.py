from django.urls import re_path,include
from .views import Search
urlpatterns = [
    re_path(r'^(?P<url_key>[0-9a-f-]+)/',Search,name='search'),
]