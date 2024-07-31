from django.shortcuts import render, get_object_or_404
from todo.models import Todo, Category, Tag
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def home(request):
    context = dict(
        todos = Todo.objects.filter(is_active=True, user=request.user),
        page_title = "Home",
    )
    return render(request, 'todo/todo_list.html', context)


@login_required(login_url='/admin/login/')
def todo_detail(request, id):
    todo = get_object_or_404(Todo, pk=id, user=request.user)
    context = dict(
        page_title = todo.title,
        todo = todo,
    )
    return render(request, 'todo/todo_detail.html', context)