from django.db import models

class Penerima(models.Model):
    email = models.EmailField(unique=True)  # Unique email field
    password = models.CharField(max_length=128)  # Password field
    name = models.CharField(max_length=100)  # Name field
    institute = models.CharField(max_length=200, blank=True, null=True)  # Institute field (optional)

    def __str__(self):
        return self.name
