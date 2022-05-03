from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView

from django_tables2 import SingleTableView

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse

from items.tables import CarTable, OwnerTable
from items.serializers import CarBrandSerializer, CarSerializer, OwnerSerializer
from items.models import CarBrand, Car, Owner

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    """API root

    Returns a URL for each table of the database
    """

    return Response({
        'carbrands': reverse('carbrand-list', request=request, format=format),
        'cars': reverse('car-list', request=request, format=format),
        'owners': reverse('owner-list', request=request, format=format),
    })



class CarBrandViewSet(viewsets.ModelViewSet):
    """View for the brands

    Default Viewset, depends on the method returns or modify the indicated data
    """

    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]


class CarViewSet(viewsets.ModelViewSet):
    """View for the cars

    Default Viewset, depends on the method returns or modify the indicated data
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]


    def get_cars_by_brand(self, request, brand):
        """List all cars of the brand provided
        """
        queryset = Car.objects.filter(brand__name__contains=brand)
        serializer = CarSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class OwnerViewSet(viewsets.ModelViewSet):
    """View for the owners

    Default Viewset, depends on the method returns or modify the indicated data
    """

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]

    def list(self, request):
        """List all owners of cars 3 or 4 (Ibiza, León)
        """
        queryset = Owner.objects.filter(cars__in=[3,4])
        serializer = OwnerSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

'''
class CarsListView(SingleTableView):
    model = Car
    table_class = CarTable
    template_name = 'items/cars.html'
'''
class OwnersListView(SingleTableView):
    model = Owner
    table_class = OwnerTable
    template_name = 'items/cars.html'

def owners_list(request):
    table = OwnerTable(Owner.objects.all())

    return render(request, "items/cars.html", {
        "table": table
    })


def cars_list(request):
    table = CarTable(Car.objects.all())

    return render(request, "items/cars.html", {
        "table": table
    })