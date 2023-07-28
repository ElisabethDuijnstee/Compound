from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Define database models to represent tasks and user choices. 
# Models for tasks which has a field to store the difficulty level 
# Models for user choices 

DIFFICULTY_CHOICES = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'), 
)

class Task(models.Model):
    """representing tasks that users can choose from"""
    title = models.CharField(max_length=100) #character field: title of the task 
    description = models.TextField() #text field: detailed description of task
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, max_length=10) # character field: choices defined by DIFFICULTY_CHOICES: represents the difficulty level of the task and allows users to select from easy medium or hard

    def __str__(self):
        return self.title 
    
class UserChoice(models.Model):
    """representing choices made by users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE) #establishes relationship between user and their choice 
    task = models.ForeignKey(Task, on_delete=models.CASCADE) #establishes relationship between a choice and the task the user selected 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.task.title}"
    
