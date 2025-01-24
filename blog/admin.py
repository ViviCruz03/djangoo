from django.contrib import admin #importación del modelo
from .models import Post # Registrar el modelo

# Register your models here.

admin.site.register(Post)