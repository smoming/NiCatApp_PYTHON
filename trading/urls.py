from django.urls import path
from trading import views
from trading.views import list_add, get_update_delete, getUnShipped

urlpatterns = [
    path('', list_add),
    path('<str:TransNo>', get_update_delete),
    path('GetUnShipped/', getUnShipped),
]
