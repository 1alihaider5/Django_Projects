from rest_framework import generics , permissions
from .models import Commnent
from .serializers import CommentSerializer

class CommentCreateView (generics.ListCreateAPIView):
    queryset = Commnent.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]    
    