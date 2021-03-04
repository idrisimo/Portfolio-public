from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    urltag = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project_difficulties = models.TextField(null=True, blank=True)
    project_solutions = models.TextField(null=True, blank=True)
    technology = models.CharField(max_length=200)
    s3_image_path = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title