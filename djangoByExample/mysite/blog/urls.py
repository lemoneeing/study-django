from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name="blog"

urlpatterns=[
    # path('', views.PostList.as_view(), name='post_list'),
    path('', views.PostList.as_view(), name='post_list'),
    path('<str:tag_slug>', views.PostList.as_view(), name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.PostList.as_view(), name='post_search'),
]