from django.contrib import admin

from media.models import ExternalImage


@admin.register(ExternalImage)
class ExternalImageAdmin(admin.ModelAdmin):
    list_display = ['owner', 'image', 'created', 'modified']
    search_fields = ['owner', 'image']
    fieldsets = [
        ('基本信息', {'classes': ['grp-collapse grp-open'], 'fields': ['owner', 'image']}),
    ]
