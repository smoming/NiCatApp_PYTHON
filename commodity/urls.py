from django.urls import path
from commodity import views
from commodity.views import list_add, get_update_delete

urlpatterns = [
    path('/', list_add),
    path('/<str:id>', get_update_delete),
]
