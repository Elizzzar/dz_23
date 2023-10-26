from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User_human
from .forms import User_human_Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def user_auth(request):
    if not request.user.is_authenticated:
        HttpResponse('Вы не зарегистрированы')
        return redirect('sign_up')
    
    logger.info('Request data: %s', request.GET)
    
    user = request.user
    return render(request, 'home.html', {'user': user})

def home_auth(request):
    user = request.user
    return render(request, 'home.html', {'user': user}) 

class Sign_Up(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')
    # 

class Login(LoginView):
    template_name = 'login.html'
    next_page = 'home'
    # 

class Log_out(LogoutView):
    next_page = '/'