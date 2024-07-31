from django.contrib import admin
from todo.models import Todo, Category, Tag


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'category',
        'is_active',
        'created_at',
        'updated_at',
    ]

    list_display_links = [
        'id',
        'title',
        'category',
        'is_active',
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
        'is_active',
    ]

    list_display_links = [
        'id',
        'title',
        'slug',
        'is_active',
    ]


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
    ]

    list_display_links = [
        'id',
        'title',
        'slug',
    ]


admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)