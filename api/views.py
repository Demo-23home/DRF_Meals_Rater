from django.shortcuts import render
from django.contrib.auth.models import User
#Internal imports
from .models import Meal, Rating
from .serializers import MealSerailizer, RatingSerializer
#Rest imports
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class MealViewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerailizer
        
    @action(methods=['POST'], detail=True)
    def rate_meal(self, request, pk):
        if 'stars' in request.data:
            '''
            update or create
            '''
            meal = Meal.objects.get(id=pk)
            username = request.data['username']
            stars = request.data['stars']
            user = User.objects.get(username=username)

            try:
                rating = Rating.objects.get(user=user.id, meal=meal.id) #get specific rate
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                json = {
                    "message":"Meal Rate Updated",
                    "result":serializer.data
                }
                return Response(json, status=status.HTTP_202_ACCEPTED)
            
            except:
                rating = Rating.objects.create(stars=stars, user=user, meal=meal)   
                serializer = RatingSerializer(rating, many=False)
                json = {
                    "message":"Meal Rate Created",
                    "result":serializer.data
                }
                return Response(json,status=status.HTTP_201_CREATED)

        json = {
            "message":"stars were not provided"
        }
        return Response(json,status=status.HTTP_400_BAD_REQUEST)





class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer