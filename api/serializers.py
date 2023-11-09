#rest imports
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
#internal imports
from .models import Meal, Rating

#Django Imports
from django.contrib.auth.models import User






class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}
        


        
class MealSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description','no_of_ratings','rate_avg')





class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'meal')