from django.contrib import admin
from demo.models import Demo


# Register your models here.

@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'author', 'is_removed', 'created', 'modified']
    list_filter = ['status', 'is_removed']
    search_fields = ['name']
    fieldsets = [
        ('基础信息', {'fields': ['name', 'author']}),
        ('状态管理', {'fields': ['status', 'status_changed']}),
        ('标记删除', {'fields': ['is_removed']})
    ]
