from django.urls import path
from .views import all_visitors

urlpatterns = [
    path("", all_visitors, name="visitors"),
]
