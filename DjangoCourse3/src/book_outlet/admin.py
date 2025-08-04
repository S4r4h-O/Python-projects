from django.contrib import admin
import book_outlet
from book_outlet.models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author")
    list_display = ("title", "author",)


admin.site.register(Book, BookAdmin)
