from django.db import models
from django.utils import timezone

class Student(models.Model):
    # photo=models.ImageField()
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    bio = models.TextField()
    creation = models.DateTimeField('Account Created', default=timezone.now)

    def __str__(self):
        return self.name.upper()