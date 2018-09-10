from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Imagen(models.Model):
    denominacion = models.CharField(max_length=50)
    file = models.BinaryField()
    content_type_file = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object_padre = GenericForeignKey('content_type','object_id')
    lugar = models.CharField(max_length=50, default="None")
