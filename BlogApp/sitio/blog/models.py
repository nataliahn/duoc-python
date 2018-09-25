from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField("Titulo",max_length=200)
    articulo = models.TextField("Artículo")
    fecha_creacion = models.DateTimeField("Fecha Creación", default=timezone.now)
    fecha_publicacion = models.DateTimeField("Fecha Publicación", blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo 