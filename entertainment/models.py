from django.db import models
from django.conf import settings
# Create your models here.

class Entertainment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField('Titúlo', max_length = 255)
    type = models.CharField('Tipo', max_length = 100, help_text='Ex: Filme, Curso etc.')
    status = models.BooleanField(default = False)
    review = models.TextField('Resenha')
    start_date = models.DateField(auto_now_add = True)
    end_date = models.DateField()

    def __str__(self):
        return self.title