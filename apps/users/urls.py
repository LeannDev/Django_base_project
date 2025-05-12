from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView, LoginView, logout_view, account_activation, CustomPasswordChangeView, CustomPasswordChangeDoneView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', account_activation, name='account_activation'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
]
