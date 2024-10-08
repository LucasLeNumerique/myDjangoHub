from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    crea_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 