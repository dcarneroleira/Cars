from django.db import models

# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=200)
    car = models.ManyToManyField(Car)

    def __str__(self):
        return self.name