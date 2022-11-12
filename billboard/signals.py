from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Comment

from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


@receiver(post_save, sender=Comment)
def send_mail(sender, instance, created, **kwargs):
    if created:
        user = instance.post.author

        html = render_to_string(
            'billboard/messages/new_comment.html',
            {
                'user': user,
                'comment': instance,
            },
        )

        msg = EmailMultiAlternatives(
            subject=f'New response',
            from_email=os.getenv('EMAIL_HOST_USER'),
            to=[user.email]
        )

        msg.attach_alternative(html, 'text/html')
        msg.send()
    else:
        user = instance.author

        html = render_to_string(
            'billboard/messages/update_comment.html',
            {
                'user': user,
                'comment': instance,
            },
        )

        msg = EmailMultiAlternatives(
            subject=f'Your response received',
            from_email=os.getenv('EMAIL_HOST_USER'),
            to=[user.email]
        )

        msg.attach_alternative(html, 'text/html')
        msg.send()
