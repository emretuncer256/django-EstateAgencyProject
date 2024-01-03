from django.contrib import admin

from .models import Agent


@admin.register(Agent)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
