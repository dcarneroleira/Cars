from django.contrib import admin

from items.models import CarBrand, Car, Owner

# Register your models here.


class CarInline(admin.StackedInline):
    model = Car
    extra = 1


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_models')
    inlines = [CarInline]
    search_fields = ['name']


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'has_owners')
    filter_horizontal = ('owners',)
    search_fields = ['name']


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_cars')
    filter_horizontal = ('cars' ,)
    search_fields = ['name']


admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Owner, OwnerAdmin)