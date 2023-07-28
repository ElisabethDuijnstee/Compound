from django.urls import path 
from . import views


# URLConfiguration model
"""The URL pattern 'daily_choices/' corresponds to the view function views.daily_choices, which will handle requests to http://127.0.0.1:8000/daily_choices/
The URL pattern 'user_choice/<int:task_id>/' corresponds to the view function views.user_choice, which will handle requests to URLs like http://127.0.0.1:8000/user_choice/1/, http://127.0.0.1:8000/user_choice/2/, etc. 
<int:task_id> part is a URL parameter that will be passed to the user_choice view, allowing you to access the specific task ID that the user selects.
"""
urlpatterns = [
    path('daily_choices/', views.daily_choices, name='daily_choices'),
    path('user_choice/<int:task_id>/', views.user_choice, name='user_choice'),
]
