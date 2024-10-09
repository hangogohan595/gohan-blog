from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return f"{self.author} - {self.title}"

