from django.db import models

# Create your models here.

class Subscription(models.Model):
    data = models.JSONField()
