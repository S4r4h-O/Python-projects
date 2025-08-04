from typing import Counter
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3)

    def __str__(self):
        return str(self.name)


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(20)

    def __str__(self):
        return f"{self.street}, {self.city} - {self.postal_code}"

    class Meta:
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=80)
    rating = models.IntegerField(
            validators=[MinValueValidator(0), MaxValueValidator(5)])
    # One to many relationship
    author = models.ForeignKey(Author, on_delete=models.CASCADE, 
                               null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, 
                                        related_name="books")

    def get_absolute_url(self):
        return reverse("book_detail_slug", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"
