from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('sites/', views.SiteListView.as_view(), name='sites'),
    path('sites/<int:pk>/', views.SiteDetailView.as_view(), name='site_detail'),

    path('country/', views.CountryAreaListView.as_view(), name='country_area'),
    path('country/<int:pk>/', views.CountryAreaDetailView.as_view(), name='country_area_detail'),

]