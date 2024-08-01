from django.db.models.signals import post_save
from django.dispatch import receiver
from todo.models import Todo, Category

@receiver(post_save, sender=Todo)
def update_category_on_todo_save(sender, instance, **kwargs):
    if instance.category:
        instance.category.update_status()
