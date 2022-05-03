from datetime import datetime

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
    actual_time = serializers.SerializerMethodField('get_current_time')

    class Meta:
        model = Car
        fields = ['url', 'brand', 'name', 'owners', 'actual_time']

    def get_current_time(self, car):
        return datetime.now()


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.HyperlinkedRelatedField(many=True, queryset=Car.objects.all(), view_name="car-detail")
    welcome = serializers.SerializerMethodField('welcome_text')
    
    class Meta:
        model = Owner
        fields = ['url', 'name', 'cars', 'welcome']
        read_only_fields = ('model_method_field',)
    
    def welcome_text(self, owner):
        # return f'Welcome {car.name}'
        return 'Welcome %(name)s' % {'name': owner.name}

    