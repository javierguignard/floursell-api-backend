from django.shortcuts import render

# Create your views here.
from production.models import Product, ProducedReport
from production.serializer import  ProductSerializer, ProducedReportSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class ProductListCreate(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Product.objects.all()
        else:
            return Product.objects.filter(created_by__lt=0)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProducedReportListCreate(viewsets.ModelViewSet):
    queryset = ProducedReport.objects.all()
    serializer_class = ProducedReportSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)