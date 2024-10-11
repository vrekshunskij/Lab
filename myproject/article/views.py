from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()  # Отримуємо всі статті з бази даних
    return render(request, 'index.html', {'articles': articles})  # Передаємо статті в шаблон

def create(request):
    if request.method == 'POST':
        Article.objects.create(
            title=request.POST['title'],
            description=request.POST['description']
        )
        return redirect('/')
    return render(request, 'create.html')
