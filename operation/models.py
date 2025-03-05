from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Statistics(models.Model):
    info = models.CharField(max_length=100)
    value = models.IntegerField()
    logo = models.CharField(max_length=100)

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
