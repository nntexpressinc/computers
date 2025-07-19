from django.contrib import admin
from .models import Computer

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'monitors_count', 'computers_count', 'keyboards_count', 'mice_count', 'created_by', 'created_at']
    list_filter = ['created_at', 'created_by', 'monitors_count', 'computers_count', 'keyboards_count', 'mice_count']
    search_fields = ['name', 'surname']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'surname', 'monitors_count', 'computers_count', 'keyboards_count', 'mice_count', 'image', 'signature')
        }),
        ('Tizim ma\'lumotlari', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # Yangi obyekt yaratilayotgan bo'lsa
            obj.created_by = request.user
        super().save_model(request, obj, form, change)