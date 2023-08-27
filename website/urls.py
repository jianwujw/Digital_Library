from django.urls import path
from .views_package import views



urlpatterns = [
    path('',views.home),
    path('content/<selection>/', views.content),
    path('content/<selection>/<pageNum>/',views.read),
    path('search',views.search),
    path('search/<letter>/',views.search_results),
    path('quicksearch/',views.quicksearch),
    path('random/',views.randomsearch),
]