from django.urls import path
from .views import *


urlpatterns = [
    # <-------- Start Get URL ------->  #

    path('get-employee/', Get_Employee.as_view()),
    path('get-cashflow/', Get_Cashflow.as_view()),
    path('get-pricing/', Get_Pricing.as_view()),
    path('get-room/', Get_Room.as_view()),
    path('get-services/', Get_Service.as_view()),

    # <-------- End Get URL ------->  #

    # <-------- Start Filter URL -------> #

    path('employee-by-full_name/<int:id>/', employee_by_full_name),
    path('employee-by-phone_number/<int:id>/', employee_by_phone_number),
    path('employee-by-salary/<int:id>/', employee_by_salary),
    path('employee-by-age/<int:id>/', employee_by_age),
    path('employee-by-gender/<int:id>/', employee_by_gender),
    path('employee-by-speciality/<int:id>/', employee_by_specialty),
    path('cashflow-by-description/<int:id>/', cashflow_by_description),
    path('cashflow-by-payment_type/<int:id>/', cashflow_by_payment_type),
    path('pricing-by-room_type/<int:id>/', pricing_by_room_type),
    path('pricing-by-price/<int:id>/', pricing_by_price),
    path('room-by-name/<int:id>/', room_by_name),
    path('room-by-price/<int:id>/', room_by_price),
    path('room-by-description/<int:id>/', room_by_description),
    path('services-by-name/<int:id>/', services_by_name),

    # <-------- End Filter URL ------->  #
]