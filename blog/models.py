from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255) #Recebe strings de até 255 caracteres.
    slug = models.SlugField(max_length=255, unique=True) #Texto usado na URL dos posts. Ex:www.meusite.com/blog/"introducao-ao-django" - SLUG.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField() #Texto sem limite de caracteres.
    created = models.DateTimeField(auto_now_add=True) #Adiciona automaticamente a data e hora de criacao do artigo.
    updated = models.DateTimeField(auto_now=True) #Atualiza a data e hora a cada modificação do post.

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})