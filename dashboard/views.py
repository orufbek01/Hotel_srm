from django.shortcuts import render
from main.serializers import *
from rest_framework.response import Response
from main.models import *
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView

''' Start CRUD Employee '''


class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

''' End CRUD Employee '''


''' Start CRUD Cashflow '''


class CreateCashflow(ListCreateAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class UpdateCashflow(UpdateAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class DeleteCashflow(DestroyAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer

''' End CRUD Cashflow '''




''' Start CRUD Pricing '''


class CreatePricing(ListCreateAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class UpdatePricing(UpdateAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class DeletePricing(DestroyAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

''' End CRUD Pricing '''


''' Start CRUD Room '''


class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UpdateRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

''' End CRUD Room '''


''' Start CRUD Service '''


class CreateService(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class UpdateService(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class DeleteService(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

''' End CRUD Service '''
