from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=False, null=False)
