from django.db import models


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=25, blank=False, null=False)
    residence = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    birthdate = models.DateField()
