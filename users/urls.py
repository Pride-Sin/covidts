# Django imports
from django.urls import path
from django.contrib.auth.views import LogoutView
# Local imports
from .views import AuthView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('logout/', LogoutView.as_view(next_page='auth'), name='logout'),
]
