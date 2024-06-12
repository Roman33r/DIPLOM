from django.urls import path
from .views import home, catalog, nedvig_page

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name="catalog"),
    path('catalog/nedvig_page/', nedvig_page, name="nedvig_page"),
]