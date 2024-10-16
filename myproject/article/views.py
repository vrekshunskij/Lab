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

def clear_articles(request):
    if request.method == 'POST':
        Article.objects.all().delete()  # Очищення всіх статей
        return redirect('/')  # Перенаправлення на головну сторінку
    return render(request, 'clear.html')  # Повертаємо шаблон для підтвердження очищення