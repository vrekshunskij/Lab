from django.urls import path
from .views import home, about
from article import views
from .views import LoginView
from .views import hrest
from .views import nema

urlpatterns = [
    path('', home, name='main'),
    path('hrest', hrest, name='hrest'),
    path('nema', nema, name='nema'),
    path('about', about, name='about'),
    path('index', views.index, name='index'),
    path('create', views.create, name='create'),
    path('clear', views.clear_articles, name='clear_articles'),
    path('login', LoginView.as_view(), name='login'),

]

