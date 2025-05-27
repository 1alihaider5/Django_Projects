from django.urls import path
from .views import ProfileDetailView

urlpatterns = [
    path('me/', ProfileDetailView.as_view(), name='my-profile'),
    path('me/update/', ProfileDetailView.as_view(), name='update-profile'),
]