from django.db import models

class Message(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    favourite_color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
