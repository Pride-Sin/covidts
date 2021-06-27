# Django imports
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import LoginView

class AuthView(LoginView):
    template_name = 'users/auth.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')