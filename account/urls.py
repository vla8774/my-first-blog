from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),

]