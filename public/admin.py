from django.contrib import admin
from .models import (
    Slider, FewWords, Services, ArtShowcase, Artist, Advantage, Category, Gallery, Fact, WhyChooseUs,
    Faq
)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'slogan', 'description', 'image', 'show_button', 'button_text', 'language']
    list_filter = ['language']
    search_fields = ['title', 'slogan', 'description']


@admin.register(FewWords)
class FewWordsAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_a', 'section_b', 'image', 'language']
    list_filter = ['language']
    search_fields = ['title', 'section_a', 'section_b']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'language']
    list_filter = ['language']
    search_fields = ['title', 'description']


@admin.register(ArtShowcase)
class ArtShowcaseAdmin(admin.ModelAdmin):
    list_display = ['section_a', 'section_b', 'language']
    list_filter = ['language']
    search_fields = ['section_a', 'section_b']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_a', 'image_a', 'language']
    list_filter = ['language']
    search_fields = ['title', ]



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['category', 'image', 'include_in_showcase', 'include_in_home', ]
    list_filter = ['category', 'include_in_showcase', 'include_in_home', ]
    search_fields = ['category__name', ]
    
    actions = ['make_visible_in_showcase', 'make_invisible_in_showcase', 'make_visible_in_home', 'make_invisible_in_home']

    def make_visible_in_showcase(self, request, queryset):
        queryset.update(include_in_showcase=True)
    make_visible_in_showcase.short_description = "Make visible in showcase"
    
    def make_visible_in_home(self, request, queryset):
        queryset.update(include_in_home=True)
    make_visible_in_home.short_description = "Make visible in home"
    
    def make_invisible_in_showcase(self, request, queryset):
        queryset.update(include_in_showcase=False)
    make_invisible_in_showcase.short_description = "Make invisible in showcase"
    
    def make_invisible_in_home(self, request, queryset):
        queryset.update(include_in_home=False)
    make_invisible_in_home.short_description = "Make invisible in home"
    


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]
    list_display = ['name', 'german_name', ]
    search_fields = ['name', ]


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ['title', 'number', 'suffix', 'language']
    list_filter = ['language']
    search_fields = ['title', ]


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_a', 'section_b', 'image_a', 'image_b', 'language']
    list_filter = ['language']
    search_fields = ['title', 'section_a', 'section_b', ]


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'language']
    list_filter = ['language']
    search_fields = ['question', 'answer', ]
