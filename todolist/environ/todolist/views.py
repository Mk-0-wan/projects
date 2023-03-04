from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def home(request):
    all = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'all': all, 'form': form}
    return render(request, 'home.html', context)


def updateTask(request, pk):
    update = Task.objects.get(id=pk)
    form = TaskForm(instance=update)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'update.html', context)

# create another form which will let you make updates to the current objects
# combine a new form with the instance you made called update to make only changes with the exisiting objects
# make sure the action remains to none to avoid stacked objects


def delete(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'delete.html', context)
