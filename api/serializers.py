#rest imports
from rest_framework import serializers

#iinternal imports
from .models import Meal, Rating




class MealSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description','no_of_ratings','rate_avg')





class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'meal')