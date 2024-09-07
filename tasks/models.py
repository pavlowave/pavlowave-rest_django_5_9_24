from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.description}"