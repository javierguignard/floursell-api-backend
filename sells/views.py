from django.shortcuts import render

# Create your views here.
from sells.models import Customer, Order, Sell, Payment, ItemOrder, ItemSell
from sells.serializer import  CustomerSerializer, OrderSerializer, SellSerializer, PaymentCustomerSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class CustomerListCreate(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Customer.objects.filter(created_by=user)
        else:
            return Customer.objects.filter(created_by__lt=0)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class OrderListCreate(viewsets.ModelViewSet):
    """
    Example map to create:
    {
        "items": [{"product":1, "quantity":2}],
        "created_by": null,
        "customer": 1
    }
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)


    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(created_by=user)
        else:
            return Order.objects.filter(created_by__lt=0)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SellListCreate(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Sell.objects.filter(created_by=user)
        else:
            return Sell.objects.filter(created_by__lt=0)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PaymentListCreate(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentCustomerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Payment.objects.filter(created_by=user)
        else:
            return Payment.objects.filter(created_by__lt=0)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProductionOrderListCreate(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)