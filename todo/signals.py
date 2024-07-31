from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Todo, Category

@receiver(post_save, sender=Todo)
def update_category_status_on_todo_save(sender, instance, **kwargs):
    # Check if the Todo item is active
    if instance.is_active:
        # Update the category if necessary
        if not instance.category.is_active:
            # Check if there are any active Todo items in this category
            if instance.category.todos.filter(is_active=True).exists():
                instance.category.is_active = True
                instance.category.save()

@receiver(post_delete, sender=Todo)
def update_category_status_on_todo_delete(sender, instance, **kwargs):
    # If the deleted Todo item was active
    if instance.is_active:
        # Re-check if the category should be deactivated
        if not instance.category.todos.filter(is_active=True).exists():
            instance.category.is_active = False
            instance.category.save()
