from rest_framework import serializers

from items.models import CarBrand, Car, Owner


class CarBrandSerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.HyperlinkedRelatedField(many=True, view_name="car-detail", read_only=True)

    class Meta:
        model = CarBrand
        fields = ['url', 'name', 'cars']


class CarSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.HyperlinkedRelatedField(queryset=CarBrand.objects.all(), view_name="carbrand-detail")
    owners = serializers.HyperlinkedRelatedField(many=True, queryset=Owner.objects.all(), view_name="owner-detail")

    class Meta:
        model = Car
        fields = ['url', 'brand', 'name', 'owners']


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.HyperlinkedRelatedField(many=True, queryset=Car.objects.all(), view_name="car-detail")

    class Meta:
        model = Owner
        fields = ['url', 'name', 'cars']