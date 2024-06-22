from django.urls import path
from .views import Home, Catalog, NedvigDetailViews

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('catalog/', Catalog.as_view(), name="catalog"),
    path('catalog/nedvig_page/<int:pk>/', NedvigDetailViews.as_view(), name="nedvig_page"),
]
