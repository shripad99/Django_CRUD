from django.db import models


# Create your models here.
class User(models.Model):
    objects = None
    name = models.CharField(max_length=70, null=False)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name + " " + self.email + " " + self.password
