from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
        path('', views.frontpage, name='frontpage'),
        path('<slug:slug>/', views.post_detail, name='detail'),]

# comments
# these will help in the reverse look up
