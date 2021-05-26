from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Application(models.Model):

    NONE = 'NO'
    ACCEPTED = 'AC'
    REJECTED = 'RE'
    RESULT_CHOICES = [
        (NONE, 'None'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected')
    ]

    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=50, null=False)
    resume = models.BooleanField(default=False, null=False)
    interview = models.BooleanField(default=False, null=False)
    date = models.DateTimeField(null=True)
    result = models.CharField(max_length=2, choices=RESULT_CHOICES, default=NONE)



