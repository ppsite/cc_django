from django.contrib import admin
from tag.models import ColoredTag


@admin.register(ColoredTag)
class ColorTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'content_type', 'object_id']
    search_fields = ['name']
    fieldsets = [
        ("基础信息", {'classes': ['grp-collapse grp-open'],
                  'fields': ['name', 'color', 'content_type', 'object_id']}),
    ]
