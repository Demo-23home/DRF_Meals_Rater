from django.contrib import admin
from .models import Meal, Rating


# Admin Classes
class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']



class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal', 'user', 'rate']
    list_filter = ['meal', 'user']

# Register your models here.






admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)