from django.urls import path

from .views import ProfileEditView, ProfileDetailView

urlpatterns = [
    path('edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('<str:username>/', ProfileDetailView.as_view(), name='profile_detail'),
]
