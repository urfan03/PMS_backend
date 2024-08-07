from django.contrib import admin
from .models import Post
from .models import Worker
from .models import ServiceDetail

admin.site.register(Post)


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'job', 'email')
    search_fields = ('name','surname', 'job', 'email')

admin.site.register(Worker, WorkerAdmin)

class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('LittleHeadName', 'LargeHeadName', 'DetailHead')
    search_fields = ('LittleHeadName', 'LargeHeadName', 'DetailHead')

admin.site.register(ServiceDetail, ServiceDetailAdmin)

