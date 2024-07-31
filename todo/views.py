from django.shortcuts import render
from todo.models import Todo, Category, Tag
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def home(request):
    context = dict(
        todos = Todo.objects.filter(is_active=True, user=request.user),
        page_title = "Home",
    )
    return render(request, 'todo/todo_list.html', context)