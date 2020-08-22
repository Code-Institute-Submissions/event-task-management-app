from django.contrib import admin
from .models import Staff

# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'role',
        'name',
        'bibliography',
        'image',
    )

    ordering = ('name',)


admin.site.register(Staff, StaffAdmin)
