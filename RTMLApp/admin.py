from django.contrib import admin
from .models import rtm_comment, Service,WorkingDays


# Register your models here.
admin.site.register(rtm_comment)
admin.site.register(Service)
admin.site.register(WorkingDays)
