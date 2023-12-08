from django.db import models

from main.choices import DescriptionPages


class LongDescription(models.Model):
    body = models.TextField(blank=False, null=False)
    page = models.CharField(max_length=255, blank=False, null=False, choices=DescriptionPages.choices)
    image = models.URLField(blank=True, null=True)

