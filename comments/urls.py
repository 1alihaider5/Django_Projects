from django.urls import path 
from .views import CommentCreateView, CommentDetailView , LikeCreateView 

urlpatterns = [
    path('api/comments/', CommentCreateView.as_view(), name='post-comment' ),
    path('api/comments/<int:pk>/', CommentDetailView.as_view() , name='comment-detail'),
    path('api/like/post/', LikeCreateView.as_view(), name='like'),   
    # path('api/like/post/<int:post_id>/', LikeDetailView.as_view(), name='like-detail'),
]
