from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

# Only allow user to update/view their own profile
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
