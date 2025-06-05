# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Comment, Like
from .serializers import CommentSerializer, LikeSerializer


class CommentCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        post_id = request.data.get("post")
        liked = request.data.get("liked")

        like_obj, created = Like.objects.get_or_create(
            user=request.user, post_id=post_id,
            defaults={"liked": liked}
        )

        if not created:
            like_obj.liked = liked
            like_obj.save()

        serializer = self.get_serializer(like_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     permission_classes = [permissions.IsAuthenticated]

    # def get_object(self):
    #     post_id = self.kwargs.get('post_id')
    #     return get_object_or_404(self.get_queryset(), post_id=post_id)
