from django.urls import path
from .views import home, Catalog, nedvig_page

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', Catalog.as_view(), name="catalog"),
    path('catalog/nedvig_page/<int:pk>', nedvig_page, name="nedvig_page"),
]
