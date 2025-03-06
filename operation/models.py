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
        
    def delete_old_image(self):
        if self.pk:
            try:
                old_image = Category.objects.get(pk=self.pk).image
                if old_image and old_image != self.image:
                    old_image.delete(save=False)
                    
            except Category.DoesNotExist:
                pass
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.delete_old_image()
        return super().save(force_insert, force_update, using, update_fields)
    
    def delete(self, using=None, keep_parents=False):
        self.image.delete(save=False)
        return super().delete(using, keep_parents)
