from django.db import models
from django.core.validators import FileExtensionValidator
from .mixins import ImageCleanupMixin

# Create your models here.
class LanguageChoices(models.TextChoices):
    EN = 'en', 'English'
    DE = 'de', 'Deutsch'


class Slider(models.Model, ImageCleanupMixin):

    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='sliders/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
                              help_text='Image size: 1024x567')
    show_button = models.BooleanField(default=True)
    button_text = models.CharField(max_length=50, default='Read More')
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)
    
    def __str__(self):
        return self.title


class FewWords(models.Model, ImageCleanupMixin):
    title = models.CharField(max_length=100)
    section_a = models.TextField(max_length=300)
    section_b = models.TextField(max_length=600)
    image = models.ImageField(upload_to='few_words/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
                              help_text='Image size: 1920x662')
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Few Words'


class Services(models.Model, ImageCleanupMixin):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='services/',
                              validators=[FileExtensionValidator(['png'])],
                              help_text='Image size: 80x80, PNG format, Transparent background')
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Services'


class ArtShowcase(models.Model):
    section_a = models.TextField(max_length=300)
    section_b = models.TextField(max_length=500)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)

    def __str__(self):
        return self.section_a

    class Meta:
        verbose_name_plural = 'Art Showcase'


class Artist(models.Model, ImageCleanupMixin):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artists/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
                              help_text='Image size: 1920x1280')

    def __str__(self):
        return self.name


class Advantage(models.Model, ImageCleanupMixin):
    
    image_field_names = ['image_a', 'image_b', 'image_c']
    
    title = models.TextField(max_length=300)
    section_a = models.TextField(max_length=500)
    section_b = models.TextField(max_length=500)
    image_a = models.ImageField(upload_to='advantages/',
                                validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
                                help_text='Image size: 900x584')
    image_b = models.ImageField(upload_to='advantages/',
                                validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
                                help_text='Image size: 1024x683')
    image_c = models.ImageField(upload_to='advantages/',
                                validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
                                help_text='Image size: 1000x667')
    quotation = models.CharField(max_length=200)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    german_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Gallery(models.Model, ImageCleanupMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='galleries')
    image = models.ImageField(upload_to='gallery/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])])
    include_in_showcase = models.BooleanField(default=False)
    include_in_home = models.BooleanField(default=False)
    
    def __str__(self):
        return self.category.name
    
    class Meta:
        verbose_name_plural = 'Gallery'


class Fact(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    suffix = models.CharField(max_length=50, default='', help_text='Example: "+" or "%" or "years"')
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model, ImageCleanupMixin):
    
    image_field_names = ['image_a', 'image_b']
    
    title = models.CharField(max_length=200)
    section_a = models.TextField(max_length=300)
    section_b = models.TextField(max_length=300)
    image_a = models.ImageField(upload_to='why_choose_us/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
                              help_text='Image size: 1920x1280')
    image_b = models.ImageField(upload_to='why_choose_us/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])],
                              help_text='Image size: 1920x1280')
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Why Choose Us'


class Faq(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField(max_length=500)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.EN)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'