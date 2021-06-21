from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    # Id do autor/Relação um para muitos.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Corpo do Texto
    body = models.TextField()
    # Data e hora criação do post
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})    