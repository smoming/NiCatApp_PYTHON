from django.urls import path
from delivery_type import views
from delivery_type.views import list_add, get_update_delete

urlpatterns = [
    path('', list_add),
    path('/<str:id>', get_update_delete),
]
