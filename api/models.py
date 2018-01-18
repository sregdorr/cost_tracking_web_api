import uuid

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=150, unique=True)
    project_number = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    budget = models.DecimalField(null=True, blank=True, max_digits=11, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


class Vendor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_name = models.CharField(max_length=100, unique=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    office_phone = models.CharField(max_length=20, null=True, blank=True)
    cell_phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.vendor_name


class InvoiceStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_status = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Invoice Status"
        verbose_name_plural = "Invoice Statuses"

    def __str__(self):
        return self.invoice_status


class PurchaseOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    purchase_order_no = models.CharField(max_length=100)
    po_type = models.CharField(max_length=20)
    vendor = models.ForeignKey('Vendor', related_name='purchase_orders', on_delete=models.DO_NOTHING)
    project = models.ForeignKey('Project', related_name='purchase_orders', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Purchase Order"

    def __str__(self):
        return self.project.project_name + ' - ' + self.purchase_order_no


class PORevision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    purchase_order = models.ForeignKey('PurchaseOrder', related_name='revisions', on_delete=models.DO_NOTHING)
    revision_date = models.DateField(auto_now_add=True)
    revision = models.IntegerField()
    limit = models.DecimalField(max_digits=11, decimal_places=2)
    action = models.CharField(max_length=20)

    class Meta:
        verbose_name = "PO Revision"

    def __str__(self):
        return self.purchase_order.purchase_order_no + ' - Rev' + str(self.revision)


class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_no = models.CharField(max_length=50)
    document_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    status = models.ForeignKey('InvoiceStatus', related_name='invoices', on_delete=models.DO_NOTHING)
    post_date = models.DateField()
    purchase_order = models.ForeignKey('PurchaseOrder', related_name='invoices', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.invoice_no