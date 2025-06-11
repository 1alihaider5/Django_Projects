from django.urls import path
from .views import PostListView, PostDetailView, AutomationFormView ,AutomationFormDetailView

urlpatterns = [
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/automation-processes/', AutomationFormView.as_view(), name='AutomationForm-list'),
    path('api/automation-processes/<int:pk>/', AutomationFormDetailView.as_view(), name='AutomationForm-detail'),
    
]