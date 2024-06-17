from django.urls import path
from .views import home, Catalog, NedvigDetailViews

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', Catalog.as_view(), name="catalog"),
    path('catalog/nedvig_page/<int:pk>/', NedvigDetailViews.as_view(), name="nedvig_page"),
]
