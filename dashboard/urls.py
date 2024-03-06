from django.urls import path
from .views import *

urlpatterns = [

    # CRUD for Employee
    path('create_employees/', CreateEmployee.as_view()),
    path('update_employees/<int:pk>/', UpdateEmployee.as_view()),
    path('delete_employees/<int:pk>/', DeleteEmployee.as_view()),

    # CRUD for Cashflow
    path('create_cashflows/', CreateCashflow.as_view()),
    path('update_cashflows/<int:pk>/', UpdateCashflow.as_view()),
    path('delete_cashflows/<int:pk>/', DeleteCashflow.as_view()),

    # CRUD for Pricing
    path('create_pricings/', CreatePricing.as_view()),
    path('update_pricings/<int:pk>/', UpdatePricing.as_view()),
    path('delete_pricings/<int:pk>/', DeletePricing.as_view()),

    # CRUD for Room
    path('create_rooms/', CreateRoom.as_view()),
    path('update_rooms/<int:pk>/', UpdateRoom.as_view()),
    path('delete_rooms/<int:pk>/', DeleteRoom.as_view()),

    # CRUD for Service
    path('create_services/', CreateService.as_view()),
    path('update_services/<int:pk>/', UpdateService.as_view()),
    path('delete_services/<int:pk>/', DeleteService.as_view()),
]

