# items/tables.py
from django.db import models
import django_tables2 as tables

from .models import Car, Owner


class OwnerTable(tables.Table):
    cars = tables.Column(empty_values=())

    def render_cars(self, record):
        return ", ".join([car.name for car in record.cars.all()])

    class Meta:
        model = Owner
        template_name = "django_tables2/bootstrap.html"
        sequence = ("id", "name", "cars", )
        # template_name = "django_tables2/bootstrap.html"
        # fields = ("name", "brand", )


class CarTable(tables.Table):
    owners = tables.Column(empty_values=())

    def render_owners(self, record):
        return ", ".join([owner.name for owner in record.owners.all()])

    class Meta:
        model = Car
        sequence = ("name", "owners", )
        # template_name = "django_tables2/bootstrap.html"
        # fields = ("name", "brand", )