from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name


class Project(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=150)
    project_number = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
