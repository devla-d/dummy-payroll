from venv import create
from django.db.models.signals import post_save
from django.dispatch import receiver

from baseapp import utils

from .models import Account


@receiver(post_save, sender=Account)
def createUser(sender, instance, created, **kwargs):
    if created:
        utils.send_welcome_mail(instance)
