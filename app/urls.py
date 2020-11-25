from django.urls import path
from . import views


app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('artykuly/', views.articles, name='article'),
    path('artykul/<slug:slug>/', views.article, name='article'),
    path('comment/', views.comment, name='comment'),
    path('drobne-ogloszenia/<slug:slug>/', views.small_ads, name='small_ads'),
    path('artykuly/<slug:slug>/', views.articles, name='articles'),
    path('cennik/wydanie-gazetowe/', views.pricing_paper, name='pricing_paper'),
    path('cennik/wydanie-internetowe/', views.pricing_internet, name='pricing_internet'),
    path('wyszukiwarka/', views.search, name='search'),
    path('o-nas/', views.about, name='about'),
    path('kontakt/', views.contact, name='contact'),
    path('polityka-prywatnosci/', views.privacy, name='privacy'),
    path('regulamin-strony/', views.regulations, name='regulations'),
    path('ogloszenia/create/', views.add_create, name='add_create'),
    path('ogloszenia/<slug:slug>/', views.add_list, name='add_list'),
    path('ogloszenia_detail/<slug:slug>/', views.add_detail, name='add_list'),
    path('subscribe_email/', views.subscribe_email, name='subscribe_email'),
]