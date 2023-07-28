from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
# view function takes a request and gives a response
# request handler (called action in django)


def daily_choices(request):
    # Fetch tasks from the database and sort them by difficulty
    tasks = Task.objects.order_by('difficulty')

    # Implement logic to present the user with daily choices based on their progress

    return render(request, 'daily_choices.html', {'tasks': tasks})

def user_choice(request, task_id):
    # Implement logic to handle the user's selection and provide feedback
    selected_task = get_object_or_404(Task, id=task_id)

    return render(request, 'user_choice_feedback.html', {'selected_task': selected_task})

