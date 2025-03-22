
class ImageCleanupMixin:
    """
    A mixin to handle deleting old images when updating the image field
    and ensuring image deletion on model deletion.
    """
    
    image_field_names = ["image"]  # Default field name (can be overridden in subclasses)

    def delete_old_images(self):
        if self.pk:
            old_instance = self.__class__.objects.get(pk=self.pk)
            for field_name in self.image_field_names:
                try:
                    old_image = getattr(old_instance, field_name)
                    new_image = getattr(self, field_name)
                    if old_image and old_image != new_image:
                        old_image.delete(save=False)
                except self.__class__.DoesNotExist:
                    pass
    
    def save(self, *args, **kwargs):
        self.delete_old_images()
        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        for field_name in self.image_field_names:
            image = getattr(self, field_name)
            if image:
                image.delete(save=False)
        return super().delete(*args, **kwargs)
