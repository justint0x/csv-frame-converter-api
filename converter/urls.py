from django.urls import path

from converter.views import *

urlpatterns = [
    path('', DataConverterAPIView.as_view())
]