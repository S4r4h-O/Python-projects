from django.shortcuts import render
from django.views import generic
from RestaurantMenu.models import Item
from .models import MEAL_TYPE


class MenuList(generic.ListView):
    model = Item
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        context["item_list"] = Item.objects.order_by("date_created")

        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
