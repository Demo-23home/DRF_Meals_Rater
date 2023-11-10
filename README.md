# DRF Meals Rater

Welcome to the **DRF Meals Rater** repository! This project is a Django Rest Framework (DRF) application designed to allow users to rate meals. It includes authentication features and implements CRUD operations for users, meals, and rates. Below, you'll find all the necessary information to understand, set up, and use this application effectively.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [CRUD Operations](#crud-operations)
- [Project URLs](#project-urls)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (>=3.6)
- Django (>=3.0)
- Django Rest Framework (>=3.0)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Demo-23home/DRF_Meals_Rater.git
   ```
2. Navigate to the project directory:
```
cd DRF_Meals_Rater
```
3. Install the required packages:
```
pip install -r requirements.txt
```
4. Usage:
```
python manage.py runserver
```
5.API Endpoints

The application will be accessible at http://localhost:8000/.

POST /api/token/: Obtain an access token by providing valid credentials.
POST /api/token/refresh/: Refresh an expired access token.
POST /api/users/: Create a new user.
GET/PUT/DELETE /api/users/{user_id}/: Retrieve, update, or delete a specific user.
GET/POST /api/meals/: List all meals or create a new meal.
GET/PUT/DELETE /api/meals/{meal_id}/: Retrieve, update, or delete a specific meal.
GET/POST /api/rates/: List all rates or create a new rate.
GET/PUT/DELETE /api/rates/{rate_id}/: Retrieve, update, or delete a specific rate.

6. Authentication
Authentication is implemented using JSON Web Tokens (JWT). To access protected endpoints, include the access token in the Authorization header of your HTTP request:
```
Authorization: Bearer <your_access_token>
```

7. CRUD Operations:
Users: Use the API endpoints to create, retrieve, update, or delete users.
Meals: Use the API endpoints to create, retrieve, update, or delete meals.
Rates: Use the API endpoints to create, retrieve, update, or delete rates.

8. Project URLs
In your project's urls.py file, you have defined the following URLs:
```
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('api.urls')),
    path("tokenrequest/", obtain_auth_token),
]
```
In your API app's urls.py file, you have defined the following API endpoints:
```
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('meals', MealViewset)
router.register('rate', RatingViewset)
router.register('users', UserViewset)

urlpatterns = [
    path('', include(router.urls))
]
```
With this setup, your API endpoints will be accessible at the following URLs relative to your project's base URL:

/api/token/: Obtain an access token.
/api/token/refresh/: Refresh an access token.
/api/users/: Create a new user or retrieve all users.
/api/users/{user_id}/: Retrieve, update, or delete a specific user.
/api/meals/: List all meals or create a new meal.
/api/meals/{meal_id}/: Retrieve, update, or delete a specific meal.
/api/rates/: List all rates or create a new rate.
/api/rates/{rate_id}/: Retrieve, update, or delete a specific rate.
Make sure your viewsets (MealViewset, RatingViewset, and UserViewset) are correctly defined in your views file (views.py) and your models are properly set up to handle the CRUD operations. If you encounter any issues or have specific questions about your viewsets or models, feel free to ask!

9. Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository
Create your feature branch: git checkout -b feature/new-feature
Commit your changes: git commit -m 'Add a new feature'
Push to the branch: git push origin feature/new-feature
Submit a pull request
10. License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details. 

You are free to use, modify, and distribute the code in this repository for both commercial and non-commercial purposes. Attribution is not required, but it is appreciated. Remember that this project comes with no warranty or support. Use it at your own risk.

