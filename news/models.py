from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=250,)
    intro = models.CharField('Anons', max_length=250)
    full_text = models.TextField('presentation')
    date = models.DateTimeField('date')

    def __str__(self):
        return f'Articles:{self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'Articles'