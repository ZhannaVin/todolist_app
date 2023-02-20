from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.http import require_http_methods
from .forms import *

def showtasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'main/main_page.html', {'tasks' : tasks})


def get_task(request):
    if request.method == "POST":
        form = Form_posttask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showtasks')
    else:
        form = Form_posttask()
    return render(request, 'main/form_template.html', {'form': form})