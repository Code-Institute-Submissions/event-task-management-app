from django.contrib import admin
from .models import Event, Category

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)