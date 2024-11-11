from django.urls import path
from .views import HomeView, PizzaMenu, IndexView

app_name = 'restaurant'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('index/', IndexView.as_view(), name='index'),
    path('menu/pizza/', PizzaMenu.as_view(), name='pizza_menu'),
]