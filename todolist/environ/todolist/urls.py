from django.urls import path
from .import views

urlpatterns = [
        path('', views.home, name='home'),
        path('update/<str:pk>/', views.updateTask, name='update'),
        path('delete/<str:pk>/', views.delete, name='delete'),
        ]
# note we use the dynamic url which will only allow the paremeters passed in the view.py file
