from django.urls import path
from .views import List_all, ArticleCreate, VideoCreate, ArticleDetail, VideoDetail, ArticleDeleteView,VideoDeleteView, ArticleUpdateView, VideoUpdateView

urlpatterns = [
    path('', List_all.as_view(), name='List_all'),
    path('add_article/', ArticleCreate.as_view(), name='add_article'),
    path('add_video/', VideoCreate.as_view(), name='add_video'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article'),
    path('video/<int:pk>', VideoDetail.as_view(), name='video'),
    path('article_update<int:pk>', ArticleUpdateView.as_view(), name='article_update'),
    path('article_delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
    path('video_update/<int:pk>', VideoUpdateView.as_view(), name='video_update'),
    path('video_delete/<int:pk>', VideoDeleteView.as_view(), name='video_delete'),
]