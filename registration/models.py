import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# from slugify import slugify
from autoslug import AutoSlugField

# Create your models here.
class User(AbstractUser):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    slugged_username = AutoSlugField(populate_from='username',always_update=True, unique_with='email')

    
