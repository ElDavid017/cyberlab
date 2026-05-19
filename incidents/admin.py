from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('title', 'reported_at')
    search_fields = ('title', 'description')