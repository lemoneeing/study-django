from django.urls import path
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list, name="snippets" ),
    path('snippet/<int:pk>', views.snippet_detail, name="snippet" ),
]