"""NiCatApp_PYTHON URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^api/ApiNation/', include('nation.urls')),
    re_path(r'^api/ApiDeliveryTypes/', include('delivery_type.urls')),
    re_path(r'^api/ApiSuppliers/', include('supplier.urls')),
    re_path(r'^api/ApiCommodities/', include('commodity.urls')),
    re_path(r'^api/ApiOrders/', include('order.urls')),
    re_path(r'^api/ApiReceipt/', include('receipt.urls')),
    re_path(r'^api/ApiPurchase/', include('purchase.urls')),
    re_path(r'^api/ApiTradings/', include('trading.urls')),
    re_path(r'^api/ApiShippers/', include('shipper.urls')),
    re_path(r'^api/ApiCashFlow/', include('cashflow.urls')),
]
