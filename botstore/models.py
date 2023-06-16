from django.utils import timezone

from django.db import models
from django.urls import reverse, re_path
from django.conf import settings
# from rasa.api import get_chat_response
# Create your models here.



class ChatHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    user_input = models.TextField(max_length=250, blank=True, null=True)
    bot_response = models.TextField(max_length=250, blank=True, null=True)
    # conversation = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'ChatHistories'
    
    def get_absolute_url(self):
        return reverse ("chat_details", kwargs ={'pk': self.pk})