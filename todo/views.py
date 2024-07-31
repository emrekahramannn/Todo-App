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
def todo_detail(request, category_slug, id):
    todo = get_object_or_404(Todo, category__slug=category_slug, pk=id, user=request.user)
    context = dict(
        page_title = todo.title,
        todo = todo,
    )
    return render(request, 'todo/todo_detail.html', context)


@login_required(login_url='/admin/login/')
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    todos = Todo.objects.filter(category=category, is_active=True, user=request.user)
    context = dict(
        page_title = category.title,
        category=category,
        todos = todos,
    )
    return render(request, 'todo/todo_list.html', context)


@login_required(login_url='/admin/login/')
def tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    todos = tag.todo_set.filter(user=request.user, is_active=True)
    context = dict(
        page_title = tag.title,
        todos = todos,
        tag=tag,
    )
    return render(request, 'todo/todo_list.html', context)