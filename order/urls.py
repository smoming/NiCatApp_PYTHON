from django.urls import path
from order import views
from order.views import list_add, get_update_delete, getUnPaid, getUnPurchase

urlpatterns = [
    path('', list_add),
    path('<str:TransNo>', get_update_delete),
    path('GetUnPaid/', getUnPaid),
    path('GetUnPurchase/', getUnPurchase),
]
