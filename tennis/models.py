from django.db import models
from embed_video.fields import EmbedVideoField
class Statistic(models.Model):


    title = models.CharField('Матч', max_length=80)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    video = EmbedVideoField(verbose_name="123")  # same like models.URLField()

    def __str__(self):
       return self.title






class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'




from django.db import models

# Create your models here.
