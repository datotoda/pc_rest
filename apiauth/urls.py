from django.urls import path
from apiauth import views


urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('register/', views.RegistrationViewSet.as_view({'post': 'create'})),
    path('reset_token/', views.TokenResetAPIView.as_view()),
    path('activate/<token>/', views.ActivateAPIView.as_view()),
]
