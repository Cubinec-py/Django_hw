from django.contrib import admin
from triangle.models import Logs, Person


class LogsAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp')


admin.site.register(Logs, LogsAdmin)
