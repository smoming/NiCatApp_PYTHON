from django.urls import path
from receipt import views
from receipt.views import list_add, get_update_delete

urlpatterns = [
    path('', list_add),
    path('<str:TransNo>', get_update_delete),
]
