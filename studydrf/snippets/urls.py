from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
    path('snippet/<int:pk>/', views.SnippetDetail.as_view(), name="snippet-detail"),
    path('snippet/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name="snippet-highlight"),
    path('users/', views.UserList.as_view(), name="users-list"),
    path('user/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# http://localhost:8080/snippets/1.json 처럼 화면에 response 를 표시할 형식을 결정할 수 있다.