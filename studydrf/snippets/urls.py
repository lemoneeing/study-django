from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list, name="snippets" ),
    path('snippet/<int:pk>', views.snippet_detail, name="snippet" ),
]

urlpatterns = format_suffix_patterns(urlpatterns) # http://localhost:8080/snippets/1.json 처럼 화면에 response 를 표시할 형식을 결정할 수 있다.