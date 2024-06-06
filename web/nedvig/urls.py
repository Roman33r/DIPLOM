from django.urls import path
from .views import home, catalog

urlpatterns = [
    path('', home, name='home'),
    path('', catalog, name="catalog"),
]