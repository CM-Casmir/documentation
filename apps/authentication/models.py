from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    # PERMISSION_CHOICES = (
    #     ('read_write', 'Read and Write'),
    #     ('read_only', 'Read Only'),
    # )
    # permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default='read_write')

    def __str__(self):
        return self.user.email
