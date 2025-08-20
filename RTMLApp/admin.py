from django.contrib import admin
from .models import rtm_comment, Service,WorkingDays


# Register your models here.
@admin.register(rtm_comment)
class rtm_commentAdmin(admin.ModelAdmin):
    list_display = ('comm_service','comm_body','comm_author','comm_timestamp',)



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'target')       # Shows key fields in the admin list
    filter_horizontal = ('working_schedule',)  # Dual-list selector for ManyToManyField

@admin.register(WorkingDays)
class WorkingDaysAdmin(admin.ModelAdmin):
    list_display = ('day', 'startHour', 'endHour')