from django.contrib import admin
from api import models


class ClientAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Project, ProjectAdmin)
