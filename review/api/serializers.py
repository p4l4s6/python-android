from rest_framework import serializers

from review.models import Review

class RestaurantReviewaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields= [
            'review_count',
            'comment'
        ]