from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import tasks
from .forms import tasksForm
from django.shortcuts import get_object_or_404

# Create your views here.

def main(request):
    if request.method == 'POST':
        form = tasksForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new = tasks(name=data['name'],
                        description = data['desk'])
            new.save()
    else:
        form = tasksForm() 
    baze = tasks.objects.all
    return render(request,
                  "tasks/main_page.html",{
                      "todo":baze
                  })


def add_task(request):
    form = tasksForm
    return render(request,
                  'tasks/add_task.html',{
                      'form': form
                  })


def change_status(request,id_task :int):
    task = get_object_or_404(tasks,id=id_task)
    if task.status:
        task.status = False
        task.save()
    else:
        task.status = True
        task.save()
    return HttpResponseRedirect('/task')


def reload_task(request):
    return HttpResponseRedirect('/task')



def delete_task(request,id_delete: int):
    task = get_object_or_404(tasks, id=id_delete)
    if task:
        task.delete()
    return HttpResponseRedirect('/task')
    




