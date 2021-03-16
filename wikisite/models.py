from django.db import models
from django.urls import reverse
import uuid


class Article(models.Model):

    class Meta:
        verbose_name= 'Статьи'
    
    title = models.CharField(max_length=255,verbose_name='Заголовок')
    text = models.TextField(max_length=5000,verbose_name='Текст статьи')
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True,verbose_name='ПУбликовать?')
    version = models.IntegerField(default=1)
    number = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return "id: {} , {}, версия {}".format( self.id, self.title,self.version)

    def get_absolute_url(self):
        return reverse('article',kwargs={'pk':self.pk})

