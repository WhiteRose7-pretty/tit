from django.urls import path
from . import views


app_name = 'simple_cms'


urlpatterns = [
    path('', views.home, name='home'),
    path('edycja-strony/<int:id>/', views.edit_page, name='edit_page'),
]