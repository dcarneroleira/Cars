from django.urls import URLPattern, path, include, re_path

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib import admin
admin.autodiscover()

from items import views


'''
carbrand_list = views.CarBrandViewSet.as_view({
    'get':'list',
    'post':'create',
})
carbrand_detail = views.CarBrandViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})
car_list = views.CarViewSet.as_view({
    'get':'list',
    'post':'create',
})
car_list_brand = views.CarViewSet.as_view({
    'get':'get_cars_by_brand',
})
car_detail = views.CarViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})
owner_list = views.OwnerViewSet.as_view({
    'get':'list',
    'post':'create',
})
owner_detail = views.OwnerViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy',
})


urlpatterns = [
    path('', views.api_root),
    path('carbrands/', carbrand_list, name='carbrand-list'),
    path('carbrands/<int:pk>/', carbrand_detail, name='carbrand-detail'),

    path('cars/', car_list, name='car-list'),
    path('cars/<str:brand>/', car_list_brand, name='car-list-brand'),
    path('cars/<int:pk>/', car_detail, name='car-detail'),

    path('owners/', owner_list, name='owner-list'),
    path('owners/<int:pk>/', owner_detail, name='owner-detail'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)


'''
router = DefaultRouter()
router.register(r'carbrands', views.CarBrandViewSet, basename="carbrand")
router.register(r'cars', views.CarViewSet, basename="car")
router.register(r'owners', views.OwnerViewSet, basename="owner")

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include(router.urls)),
    path(
        'cars/get_cars_by_brand/<str:brand>',
        views.CarViewSet.as_view(
            {'get':'get_cars_by_brand'},
        ),
    ),
    path('listCars/', views.OwnersListView.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]