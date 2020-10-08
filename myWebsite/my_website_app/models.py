from django.db import models


# Create your models here.
class UserEnquiries(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    enquiry_title = models.CharField(max_length=150)
    message = models.CharField(max_length=4000)

    def __str__(self):
        return self.enquiry_title

