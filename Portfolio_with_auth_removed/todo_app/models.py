from django.db import models


class Todo_list(models.Model):
    list_item = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.list_item