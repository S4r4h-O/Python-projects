from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return str(self.caption)


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=50, null=True)
    content = models.TextField(max_length=2000, 
                        validators=[MinLengthValidator(20)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name="posts")
    tag = models.ManyToManyField(Tag, related_name="tag", null=True)

    def __str__(self):
        return str(self.title)


