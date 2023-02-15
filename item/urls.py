from django.urls import path
from .views import StoreDetailView

app_name = 'item'
urlpatterns = [
    path('<int:pk>/',StoreDetailView.as_view(),name='item_detail'),
]