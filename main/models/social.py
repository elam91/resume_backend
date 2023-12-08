from django.db import models



class Social(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    icon = models.URLField(blank=True, null=True)