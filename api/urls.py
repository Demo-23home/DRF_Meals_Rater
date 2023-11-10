from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('meals', MealViewset)
router.register('rate',RatingViewset)
router.register('users',UserViewset)



urlpatterns = [
path('', include(router.urls))
]
