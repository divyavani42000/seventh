from newzland.views import *
from django.urls import path
app_name='philips'
urlpatterns=[
    path('williamson/',williamson,name='williamson'),
]