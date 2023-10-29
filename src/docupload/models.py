from enum import unique
import uuid
from django.db import models
from users.models import Profile

class Categorie(models.Model):
    libelleCat = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.libelleCat

class Document(models.Model):
    TYPE_CHOICES = (
        ('fichier','Fichier'),
        ('image','Image'),
        ('video','Video'),
    )
    libelleDoc = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    typeDoc = models.CharField(choices=TYPE_CHOICES, default='fichier',max_length=10)
    docUpload = models.FileField(upload_to='')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    operator = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.libelleDoc

