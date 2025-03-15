from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'experience', 'posted_on')
    list_filter = ('company', 'location', 'posted_on')
    search_fields = ('title', 'company', 'location')
    date_hierarchy = 'posted_on'