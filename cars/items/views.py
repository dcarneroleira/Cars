from audioop import reverse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from items.serializers import CarBrandSerializer, CarSerializer, OwnerSerializer
from items.models import CarBrand, Car, Owner

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'carbrands': reverse('carbrand-list', request=request, format=format),
        'cars': reverse('car-list', request=request, format=format),
        'owners': reverse('owner-list', request=request, format=format),
    })


class CarBrandViewSet(viewsets.ModelViewSet):

    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CarViewSet(viewsets.ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OwnerViewSet(viewsets.ModelViewSet):

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]