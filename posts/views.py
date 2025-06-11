
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post , AutomationForm
from .serializers import PostSerializer, PostCreateSerializer , AutomationFormSerializer

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        return PostCreateSerializer if self.request.method == 'POST' else PostSerializer

    def perform_create(self, serializer):
        """Handle image upload properly"""
        try:
            # Ensure user is set
            serializer.validated_data['user'] = self.request.user

                
            # Save the instance
            instance = serializer.save()
            
            # Debug output
            print(f"Saved post with image: {instance.image}")  # Check if image was saved
            if instance.image:
                print(f"Image path: {instance.image.path}")  # Verify file exists
        except Exception as e:
            print(f"Error saving post: {str(e)}")
            raise

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        return PostCreateSerializer if self.request.method in ['PUT', 'PATCH'] else PostSerializer

    def perform_update(self, serializer):
        """Handle image updates properly"""
        try:
            if 'image' in self.request.data:
                if self.request.data['image'] is None:  # Delete existing image
                    if serializer.instance.image:
                        serializer.instance.image.delete(save=False)
                    serializer.validated_data['image'] = None
            serializer.save()
        except Exception as e:
            print(f"Error updating post: {str(e)}")
            raise
        
 # === AutomationProcess Views ===
 
class AutomationFormView (generics.ListCreateAPIView):
    queryset = AutomationForm.objects.all()
    serializer_class = AutomationFormSerializer
    permission_classes = [permissions.IsAuthenticated]
    
             
class AutomationFormDetailView  (generics.RetrieveUpdateDestroyAPIView):
    queryset = AutomationForm.objects.all()
    serializer_class = AutomationFormSerializer
    permission_classes = [permissions.IsAuthenticated]      