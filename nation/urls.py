from django.urls import path
from nation import views
from nation.views import list_add, get_update_delete

urlpatterns = [
    path('', list_add),
    path('/<str:id>', get_update_delete),
]
