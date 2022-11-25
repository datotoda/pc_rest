from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cpu import views

router = DefaultRouter()
router.register('cpu', views.CpuViewSet, basename="cpu")

urlpatterns = [
    path('', include(router.urls)),
]
