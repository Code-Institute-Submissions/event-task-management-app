from django.contrib import admin
from .models import Venues

# Register your models here.


class VenuesAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'name',
        'size',
        'image',
    )

    ordering = ('name',)


admin.site.register(Venues, VenuesAdmin)
