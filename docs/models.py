import re
from django.db import models

# Create your models here.

class Doc(models.Model):

    # def func(self, dirrr, file_upload):
    #     file_upload = models.ImageField(upload_to=dirrr)
    
    # def upload_where(self, dirrr):
    #     print(dirrr)
    #     return 'datas/'.join(dirrr)

    upload = models.ImageField(upload_to='datas/')

    def __str__(self):
        return str(self.pk)

