from django.shortcuts import render
from webapp.models import Tasks, STATUS_CHOICES


def tasks_view(request, *args, **kwargs):
    tasks = Tasks.objects.all()
    return render(request, 'index.html', context={
        'tasks': tasks

    })


def task_all_view(request, *args, **kwargs):
    task_id = request.GET.get('id')
    tasks = Tasks.objects.get(pk=task_id)
    return render(request, 'task_all.html', context={
        'tasks': tasks
    })



def task_create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'create.html', context={
            'status_choices' : STATUS_CHOICES
        })
    elif request.method =='POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        created_at = request.POST.get('created_at')



        task = Tasks.objects.create(description=description, status=status, created_at=created_at)
        return render(request, 'task_all.html', {'task' : task})