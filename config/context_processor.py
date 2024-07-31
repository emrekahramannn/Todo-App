from todo.models import Category

def global_context(request):
    return dict(
        categories = Category.objects.filter(is_active=True)
    )