from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from django.core.cache import cache



from operation.models import Statistics, Category
from operation.serializers import StatisticsSerializer, CategorySerializer
from .utils import send_email_with_template, send_html_email


class StatisticsViewSet(ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def index(request):
    return render(request, 'index.html')


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
