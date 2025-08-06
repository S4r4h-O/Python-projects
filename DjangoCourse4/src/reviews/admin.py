from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ["review_text", "rating"]


admin.site.register(Review, ReviewAdmin)
