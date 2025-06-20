from datetime import datetime

from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Post, AutomationForm, Holidays
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    AutomationFormSerializer,
    HolidaysSerializer,
)
from .utils import get_holidays
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        return PostCreateSerializer if self.request.method == "POST" else PostSerializer

    def perform_create(self, serializer):
        """Handle image upload properly"""
        try:
            # Ensure user is set
            serializer.validated_data["user"] = self.request.user

            # Save the instance
            instance = serializer.save()

            # Debug output
            print(
                f"Saved post with image: {instance.image}"
            )  # Check if image was saved
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
        return (
            PostCreateSerializer
            if self.request.method in ["PUT", "PATCH"]
            else PostSerializer
        )

    def perform_update(self, serializer):
        """Handle image updates properly"""
        try:
            if "image" in self.request.data:
                if self.request.data["image"] is None:  # Delete existing image
                    if serializer.instance.image:
                        serializer.instance.image.delete(save=False)
                    serializer.validated_data["image"] = None
            serializer.save()
        except Exception as e:
            print(f"Error updating post: {str(e)}")
            raise


# === AutomationProcess Views ===


class AutomationFormView(generics.ListCreateAPIView):
    queryset = AutomationForm.objects.all()
    serializer_class = AutomationFormSerializer
    permission_classes = [permissions.IsAuthenticated]


class AutomationFormDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AutomationForm.objects.all()
    serializer_class = AutomationFormSerializer
    permission_classes = [permissions.IsAuthenticated]


# ======== Implement Calenderific ===============


class HolidayView(APIView):
    def get(self, request):
        country = request.GET.get("country", "PK")
        year = request.GET.get("year", "2025")

        holidays = get_holidays(country, year)
        return Response(holidays)


User = get_user_model()


# class UserHolidayView(APIView):
#     def get(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return Response(
#                 {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
#             )

#         # Use user's country to fetch holidays
#         country = user.country or "PK"
#         year = request.GET.get("year", "2025")

#         holidays = get_holidays(country=country, year=year)
#         return Response(holidays)


class UserHolidayView(APIView):
    def get(self, request, user_id):
        # Step 1: Get user or return 404
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # Step 2: Setup country & year
        country = user.country or "PK"
        year = request.GET.get("year") or str(datetime.now().year)

        # Step 3: Return saved holidays if they exist
        holidays = Holidays.objects.filter(user=user, country=country, date__year=year)
        if holidays.exists():
            return Response(HolidaysSerializer(holidays, many=True).data)

        # Step 4: Fetch and save external holidays
        fetched = get_holidays(country, year)
        new_holidays = []

        for h in fetched:
            try:
                date = datetime.strptime(h["date"]["iso"], "%Y-%m-%d").date()
                holiday = Holidays.objects.create(
                    user=user,
                    name=h.get("name"),
                    description=h.get("description", ""),
                    date=date,
                    country=country,
                )
                new_holidays.append(holiday)
            except Exception:
                continue

        return Response(
            HolidaysSerializer(new_holidays, many=True).data,
            status=status.HTTP_201_CREATED,
        )
