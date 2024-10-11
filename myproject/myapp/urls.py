from django.urls import path
from .views import home, about
from article import views
#urlpatterns = [
#    path('', home, name='home'),
#    path('about/', about, name='about'),
#]
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
]
