from django.contrib import admin
from .models import Author, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "excerpt", "author"]
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
