from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=80)
    rating = models.IntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(5)])
    # One to many relationship
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    
    def get_absolute_url(self):
        return reverse("book_detail_slug", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"
