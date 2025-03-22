from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import activate
from django.views.decorators.csrf import csrf_exempt
from django.utils import translation
import random

from .models import Slider, FewWords, Services, ArtShowcase, Artist, Advantage, Category, Gallery, Fact
from operation.utils import send_html_email

# Create your views here.
def index(request):
    
    lang = request.GET.get('lang', 'en')  # اللغة الافتراضية الإنجليزية
    activate(lang)
    sliders = Slider.objects.filter(language=lang)
    few_words = FewWords.objects.filter(language=lang).first()
    services = Services.objects.filter(language=lang)
    art_showcase = ArtShowcase.objects.filter(language=lang).first()
    showcase_images = Gallery.objects.filter(include_in_showcase=True)
    artists = Artist.objects.all()
    advantages = Advantage.objects.filter(language=lang).first()
    categories = Category.objects.all()
    gallery = Gallery.objects.filter(include_in_home=True).all()
    facts = Fact.objects.filter(language=lang).all()
    
    
    context = {
        'sliders': sliders,
        'few_words': few_words,
        'services': services,
        'art_showcase': art_showcase,
        'showcase_images': showcase_images,
        'artists': artists,
        'advantages': advantages,
        'categories': categories,
        'gallery': gallery,
        'facts': facts,
    }
    template_path = f'{lang}/index.html'
    return render(request, template_path, context)


@csrf_exempt
def set_language(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        language = data.get('language', 'en')
        activate(language)
        print('Language set to', language)
        return JsonResponse({'message': 'Language set to ' + language})
    return JsonResponse({'message': 'Invalid request method'})



def confirmation(request):
    context = {
        'user': 'John Doe',
        'date': '2023-08-15',
        'time': '10:00 AM',
        'tattoo_artist': 'Jane Smith',
        'design': 'Floral',
        'size': 'Small',
        'price': '$50',
    }

    mail_success = send_html_email(
        subject='Tattoo Appointment Confirmation',
        template='confirmation.html',
        context=context,
        recipient_list=('walidpianooo@gmail.com',),
    )

    return render(request, 'confirmation.html', context=context)
