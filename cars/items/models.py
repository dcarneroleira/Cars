from django.db import models
from django.contrib import admin

# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    @admin.display(description="Models")
    def get_models(self):
        return self.cars.count()

class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="cars")
    name = models.CharField(max_length=150)

    class Meta:
        unique_together = ['brand', 'name']

    def __str__(self):
        return self.name


    @admin.display(
        boolean=True,
        description='Has owners?',
    )
    def has_owners(self):
        return self.owners.exists()


class Owner(models.Model):
    name = models.CharField(max_length=200)
    cars = models.ManyToManyField(Car, related_name="owners", blank=True)

    def __str__(self):
        return self.name

    @admin.display(
        boolean=True,
        description='Has cars?',
    )
    def has_cars(self):
        return self.cars.exists()