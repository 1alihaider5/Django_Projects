from django.urls import path 
from .views import CommentCreateView, CommentDetailView

urlpatterns = [
    path('', CommentCreateView.as_view(), name='post-comment' ),
    path('<int:pk>/', CommentDetailView.as_view() , name='comment-detail')
]
