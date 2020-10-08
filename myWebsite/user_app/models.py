from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    # this create a 1 to 2 relationship with the Users class
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
