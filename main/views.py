from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


class Get_Employee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Get_Cashflow(ListAPIView):
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class Get_Pricing(ListAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class Get_Room(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class Get_Service(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer




@api_view(["GET"])
def employee_by_full_name(request):
    full_name = request.GET.get('full_name')
    employee = Employee.objects.filter(full_name__icontains=full_name)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    employee = Employee.objects.filter(phone_number__icontains=phone_number)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_salary(request):
    salary = request.GET.get('salary')
    employee = Employee.objects.filter(salary__icontains=salary)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_age(request):
    age = request.GET.get('age')
    employee = Employee.objects.filter(age__icontains=age)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_gender(request):
    gender = request.GET.get('gender')
    employee = Employee.objects.filter(gender__icontains=gender)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_specialty(request):
    specialty = request.GET.get('specialty')
    employee = Employee.objects.filter(specialty__icontains=specialty)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(["GET"])
def cashflow_by_description(request):
    description = request.GET.get('description')
    cashflow = Cashflow.objects.filter(description__icontains=description)
    ser = CashflowSerializer(cashflow, many=True)
    return Response(ser.data)


@api_view(["GET"])
def cashflow_by_payment_type(request):
    payment_type = request.GET.get('payment_type')
    cashflow = Cashflow.objects.filter(payment_type__icontains=payment_type)
    ser = CashflowSerializer(cashflow, many=True)
    return Response(ser.data)


@api_view(["GET"])
def pricing_by_room_type(request):
    room_type = request.GET.get('room_type')
    pricing = Pricing.objects.filter(room_type__icontains=room_type)
    ser = PricingSerializer(pricing, many=True)
    return Response(ser.data)


@api_view(["GET"])
def pricing_by_price(request):
    price = request.GET.get('price')
    cashflow = Pricing.objects.filter(price__icontains=price)
    ser = PricingSerializer(cashflow, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_name(request):
    name = request.GET.get('name')
    room = Room.objects.filter(name__icontains=name)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_price(request):
    price = request.GET.get('price')
    room = Room.objects.filter(price__icontains=price)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def room_by_description(request):
    description = request.GET.get('description')
    room = Room.objects.filter(description__icontains=description)
    ser = RoomSerializer(room, many=True)
    return Response(ser.data)


@api_view(["GET"])
def services_by_name(request):
    name = request.GET.get('name')
    services = Service.objects.filter(name__icontains=name)
    ser = ServiceSerializer(services, many=True)
    return Response(ser.data)
