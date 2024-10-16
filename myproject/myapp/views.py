from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
def home(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'  
    success_url = reverse_lazy('home')

def hrest(request):
    return render(request, 'hrest.html')

def nema(request):
    return render(request, 'nema.html')

