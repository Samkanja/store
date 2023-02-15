from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
from .models import Item


class StoreDetailView(DetailView):
    model = Item
    template_name = 'item/detail.html'
    context_object_name = 'item'

  