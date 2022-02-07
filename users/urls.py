from django.urls import path

from users.views import RegistrationView, LoginView

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
]