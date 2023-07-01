from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Photographs

@receiver(post_save, sender=Photographs)
def save_upload(sender, instance, **kwargs):
    instance.profile.save()