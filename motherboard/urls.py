from django.urls import path, include
from rest_framework.routers import DefaultRouter
from motherboard import views

router = DefaultRouter()
router.register('motherboard', views.MotherboardViewSet, basename='motherboard')

urlpatterns = [
    path('', include(router.urls)),
]
