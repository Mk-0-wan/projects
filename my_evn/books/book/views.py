from django.shortcuts import render, redirect
from .models import BookName
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.


def book_list(request):
    all = BookName.objects.all()
    context = {'all': all}
    return render(request, 'home.html', context)


def book_detail(request, pk):
    list = get_object_or_404(BookName, pk=pk)
    context = {'list': list}
    return render(request, 'detail.html', context)


def redirect_me(request):
    return redirect(reverse('bok:home'))
# takes in a reverse function which you need to pass out the url namespace for that particular page
