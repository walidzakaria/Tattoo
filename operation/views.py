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

from .models import Appointment, Subscription
from .serializers import AppointmentSerializer, SubscriptionSerializer
from .utils import send_email_with_template, send_html_email
from django.conf import settings


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            confirmation_mail = send_html_email(
                subject='Hani Tattoo Appointment Confirmation',
                template='confirmation.html',
                context=serializer.data,
                recipient_list=(request.data['email'],),
            )
            notification_email = send_html_email(
                subject='Hani Tattoo New Appointment',
                template='appointment.html',
                context=serializer.data,
                recipient_list=settings.ADMIN_EMAILS,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        existing_subscription = Subscription.objects.filter(email=request.data['email']).first()
        if existing_subscription:
            return Response({'message': 'You are already subscribed'}, status=status.HTTP_200_OK)
        if serializer.is_valid():
            serializer.save()
            
            
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    # mail_success = send_html_email(
    #     subject='Tattoo Appointment Confirmation',
    #     template='confirmation.html',
    #     context=context,
    #     recipient_list=('walidpianooo@gmail.com',),
    # )

    return render(request, 'confirmation.html', context=context)
