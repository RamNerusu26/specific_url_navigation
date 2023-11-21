from django.urls import path
from app2.views import *

app_name='bindu'

urlpatterns=[
    path('bindu/',bindu,name='bindu')
]