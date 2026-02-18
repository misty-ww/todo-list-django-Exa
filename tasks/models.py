from django.db import models

class tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False,
                                 blank=True,
                                 null=True)
    date = models.DateField(auto_now_add=True)
