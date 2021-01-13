from django.urls import path
from purchase import views
from purchase.views import list_add, get_update_delete

urlpatterns = [
    path('', list_add),
    path('<str:TransNo>', get_update_delete),
]
