from django.urls import path
from .views import documentation_views

urlpatterns = [
    path('', documentation_views),
]
