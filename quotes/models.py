from django.db import models
from registration.models import User
import uuid



class QuoteCategory(models.Model):
    title=models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title

class Quote(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    quote=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(QuoteCategory, blank=True)
    pub_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.quote)>50:
            return self.quote[:50] + '...'
        return self.quote



