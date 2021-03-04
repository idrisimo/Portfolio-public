from django.db import models

# Create your models here.
class Urlmodel(models.Model):
    long_url = models.CharField(max_length=100)
    short_string = models.CharField(max_length=50)

    def __str__(self):
        return self.long_url