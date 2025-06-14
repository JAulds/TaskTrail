from django.http import HttpResponse
from django.views import generic
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm, TaskStatusForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import viewsets
from .serializer import TaskSerializer
import datetime
from datetime import date, timedelta
import logging
from collections import defaultdict
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

class TaskList(generic.ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        return Task.objects.all().order_by('due')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_list = self.get_queryset()
        grouped_tasks = defaultdict(list)
        today = date.today()

        for task in task_list:
            if not task.due:
                group_label = "No Due Date"
                task.due_in = "No due date"
            else:
                start_of_week = task.due - timedelta(days=task.due.weekday())
                group_label = start_of_week.strftime("Week of %b %d")

                delta = task.due - today
                if delta.days < 0:
                    task.due_in = f"Overdue by {-delta.days} day(s)"
                elif delta.days == 0:
                    task.due_in = "Due today"
                else:
                    task.due_in = f"Due in {delta.days} day(s)"

            grouped_tasks[group_label].append(task)

        logger.warning("Accessed Home Page at " + str(datetime.datetime.now()) + " hours!")

        context['grouped_tasks'] = dict(grouped_tasks)
        return context

class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'task_detail.html'

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    logger.warning("Register was accessed at " + str(datetime.datetime.now()) + " hours!")
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                logger.warning("Logged in at " + str(datetime.datetime.now()) + " hours!")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    logger.warning("Logged out at " + str(datetime.datetime.now()) + " hours!")
    return redirect("login")

@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskStatusForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', slug=task.slug)
    else:
        form = TaskStatusForm(instance=task)

    return render(request, 'update_task_status.html', {'form': form, 'task': task})
