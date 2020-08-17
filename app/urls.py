from django.urls import path
from . import views


app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('artykul/<slug:slug>/', views.article, name='article'),
    path('comment/', views.comment, name='comment'),
]