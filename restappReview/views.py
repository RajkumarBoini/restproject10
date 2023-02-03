from django.shortcuts import render
from .permissions import IsAdminOrReadOnly
from .models import Product,Review
from .serializers import ProductSerializer,ReviewSerializer
from rest_framework import generics
from .permissions import IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly

class Productlist(generics.RetrieveUpdateDestroyAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=(IsAdminOrReadOnly,)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ReviewSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)