from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.



class Meal(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)

    def rate_avg(self):
        sum = 0
        ratings = Rating.objects.filter(meal=self)
        for x in ratings:
            sum += x.stars
        if len(ratings)>0:
            return sum/len(ratings)
        return 0
        
        
         


    

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def __str__(self):
        return str(self.meal)
    

    class Meta:
        unique_together = (('user','meal'),)
        index_together = (('user','meal'),)
    
