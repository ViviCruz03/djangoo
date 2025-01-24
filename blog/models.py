from django.conf import settings
from django.db import models
from django.utils import timezone

#Simpre comenzar el nombre de una  clase con Mayuscula
class Post(models.Model): #se define el modelo 
    #model.Model indica que es un modelo de Django, por lo que Djando sabe que debe guardarse en su BD
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # es un enlace a otro modelo
    title = models.CharField(max_length=200) #nimero limitado de caracteres
    text = models.TextField() #Textos largos sin limite
    created_date = models.DateTimeField(default=timezone.now) #Fecha y hora
    published_date=models.DateTimeField(blank=True, null=True) #fecha y hora

    def publicacion(self):
        self.publish_date =timezone.now()
        self.save()

    def __str__(self):
        return self.title
    