from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings

# def send_email(subject, message, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL):
#     return send_mail(
#         subject,
#         message,
#         from_email,
#         recipient_list,
#         fail_silently=False,
#     )


def send_email_with_template(subject, message, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        html_message=message,
    )


def send_html_email(subject, template, context, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL):
    html_content = render_to_string(template, context)
    plain_content = strip_tags(html_content)

    return send_mail(
        subject=subject,
        message=plain_content,
        from_email=from_email,
        recipient_list=recipient_list,
        html_message=html_content,
    )
