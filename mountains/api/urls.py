from django.urls import path
from mountains.api import views

urlpatterns = [
    path('mountains/', views.ListView.as_view(), name='list'),
    path('mountains/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
