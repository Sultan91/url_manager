from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Url(models.Model):
    text = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text



