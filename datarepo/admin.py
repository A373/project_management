from django.contrib import admin
from .models import CustomUser, Task, Project
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'email', 'mobile', 'user_type', 'created']


UserAdmin.fieldsets += (
    (
        'Custom fields', {
            'fields': ('mobile', 'user_type', 'created')
        }
    ),
)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'project', 'status']
    list_filter = ['task', 'project']
    search_fields = ['task']
    ordering = ['status']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)