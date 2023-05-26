from django.db import models


class Admin(models.Model):
    admin_id = models.PositiveIntegerField('Admin id',primary_key=True)
    email = models.EmailField('Email')
    password = models.CharField('Password',max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Person(models.Model):
    person_id = models.PositiveIntegerField(primary_key=True)
    rfid = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

class Actives(models.Model):
    rfid = models.CharField(primary_key=True, max_length=20, default='0')
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    start_hour = models.CharField(max_length=100, blank=True, null=True)
    finish_hour = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Reports(models.Model):
    report_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    report_date = models.CharField(max_length=100, blank=True, null=True)
    start_hour = models.CharField(max_length=100, blank=True, null=True)
    finish_hour = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
