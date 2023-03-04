from django.urls import path
from . import views

app_name = 'bok'

urlpatterns = [
    path('', views.book_list, name="home"),
    path('<int:pk>/', views.book_detail, name="detail"),
    path('blog/', views.redirect_me, name="redirect"),
]
