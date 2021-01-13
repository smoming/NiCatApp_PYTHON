from django.urls import path
from cashflow import views
from cashflow.views import account, unaccount

urlpatterns = [
    path('DoAccound/', account),
    path('DoUnAccound/', unaccount),
]
