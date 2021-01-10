from django.urls import path
from supplier import views
from supplier.views import list_add, get_update_delete

urlpatterns = [
    path('', list_add),
    path('<str:id>', get_update_delete),
]
