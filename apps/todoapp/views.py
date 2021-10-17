from apps.todoapp.forms import TaskForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from django.urls import reverse_lazy
from django.views import generic


class TaskListView(generic.ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'


class TaskDetailView(generic.detail.DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'



class TaskUpdateView(generic.edit.UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    
    
    def get_success_url(self):
        return reverse_lazy('cls_details',kwargs={'pk':self.object.id})


class TaskDeleteView(generic.edit.DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cls_home')

def index(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request,'index.html' , {'tasks':tasks})
    
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        
        todo = Task(name=name, priority=priority, date=date)
        todo.save()
        return redirect('/')
    
    
def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html', {'task':task})


def update(request,id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None , instance=task)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'update.html', {'task': task, 'form': form})
