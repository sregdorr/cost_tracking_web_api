from django.contrib import admin
from api import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.InvoiceStatus)
class InvoiceStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PORevision)
class PORevision(admin.ModelAdmin):
    pass


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass