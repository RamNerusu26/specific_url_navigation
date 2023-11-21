from django.urls import path
from app1.views import *

app_name='ram'

urlpatterns=[
    path('ram/',ram,name='ram'),
]