from django.shortcuts import render
from django.contrib.auth.models import User
#Internal imports
from .models import Meal, Rating
from .serializers import MealSerailizer, RatingSerializer, UserSerializer
#Rest imports
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.




class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        json = {
            "token":token.key
        }
        return Response(json, status=status.HTTP_201_CREATED)




class MealViewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerailizer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
        
    @action(methods=['POST'], detail=True)
    def rate_meal(self, request, pk):
        if 'stars' in request.data:
            '''
            update or create
            '''
            meal = Meal.objects.get(id=pk)
            user = request.user
            # print(user)
            # username = request.data['username']
            stars = request.data['stars']
            # user = User.objects.get(username=username)


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

    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)


    def create(self, request, *args, **kwargs):
        json = {
            "message":"this is not the right way to create a Rate"
        }
        return Response(json,status=status.HTTP_400_BAD_REQUEST)
    


    def update(self, request ,*args, **kwargs):

        json = {
            "message":"this is not the right way to update a Rate"
        }

        return Response(json, status=status.HTTP_400_BAD_REQUEST)