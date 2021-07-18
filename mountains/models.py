from django.db import models

class Mountain(models.Model):
    mountain_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    height = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=100)
    days_to_climb = models.CharField(max_length=100)
    notes = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.mountain_name
