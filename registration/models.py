import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# from slugify import slugify
from autoslug import AutoSlugField

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class User(AbstractUser):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    slugged_username = AutoSlugField(populate_from='username',always_update=True, unique_with='email')

# Automatically generate token for every user    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)