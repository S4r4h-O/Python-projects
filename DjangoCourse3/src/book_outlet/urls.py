from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('<int:id>', views.book_detail_by_id, name="book_detail"),
    path('<slug:slug>', views.book_detail, name="book_detail_slug")
]
