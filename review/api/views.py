from rest_framework import generics
from review.api.serializers import RestaurantReviewaSerializer
from review.models import Review



class ReviewListAPIView(generics.ListAPIView):
    serializer_class = RestaurantReviewaSerializer

    def get_queryset(self):
        return Review.objects.all()