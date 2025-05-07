# urls.py
from django.urls import path

from .views import SignUpView, LoginView, logout_view, account_activation

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', account_activation, name='account_activation'),
]
