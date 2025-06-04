from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        try:
            return self.request.user.profile
        except Profile.DoesNotExist:
            # Create profile if it doesn't exist (fallback)
            return Profile.objects.create(user=self.request.user)
    
    def perform_update(self, serializer):
        # Handle picture deletion if null is passed
        if 'picture' in self.request.data and self.request.data['picture'] is None:
            serializer.instance.picture.delete(save=False)
        serializer.save()