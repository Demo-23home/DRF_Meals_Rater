from django.shortcuts import render
#Internal imports
from .models import Meal, Rating
from .serializers import MealSerailizer, RatingSerializer
#Rest imports
from rest_framework import viewsets
# Create your views here.


class MealViewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerailizer


class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer