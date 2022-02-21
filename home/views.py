from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/login.html'

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class TimelineView(LoginRequiredMixin, TemplateView):
    template_name = 'timeline.html'