from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

## ViewSet 사용 시 URL 설정 직접하기
# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight',
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/', snippet_list, name="snippet-list"),
#     path('snippet/<int:pk>/', snippet_detail, name="snippet-detail"),
#     path('snippet/<int:pk>/highlight/', snippet_highlight, name="snippet-highlight"),
#     path('users/', user_list, name="users-list"),
#     path('user/<int:pk>/', user_detail, name="user-detail"),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
# # http://localhost:8080/snippets/1.json 처럼 화면에 response 를 표시할 형식을 결정할 수 있다.

router = DefaultRouter()
router.register('snippets', views.SnippetViewSet, basename='snippet')
router.register('user', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
