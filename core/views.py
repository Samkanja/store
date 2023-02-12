from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from item.models import Item, Category

class IndexListView(ListView):
    template_name = 'core/index.html'
    model = Item
    context_object_name = 'items'

    def get_queryset(self):
        return self.model.objects.filter(is_sold=False)[0:6]

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['categories'] = Category.objects.all()
        return context

