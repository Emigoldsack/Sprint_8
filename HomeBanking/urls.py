"""HomeBanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from cuenta.views import AccountBalance
from prestamo.views import CreateLoan, Loan
from sucursal.views import BranchList 
from cliente.views import CustomerDetails, CustomerList
from tarjeta.views import TarjetasCliente 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('itbank/customer/<int:pk>', CustomerDetails.as_view()),
    path('itbank/customers', CustomerList.as_view()),
    path('itbank/branch', BranchList.as_view()),
    path('itbank/account/<int:customer_id>', AccountBalance.as_view()),
    path('itbank/loan/<int:customer_id>', Loan.as_view()),
    path('itbank/card/<int:customer_id>', TarjetasCliente.as_view()),
    path('itbank/loan', CreateLoan.as_view()),
]
