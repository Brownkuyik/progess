from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'progres/signup.html'
    success_url = reverse_lazy("company:home")

    # to login()
class LoginViews(FormView):
    form_class = AuthenticationForm
    template_name = 'progres/login.html'
    success_url = reverse_lazy('company:home')




