from django.db import models


class Project(models.Model):
    class Meta:
        ordering = ['order']
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=False, null=False)
    website_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    github_link2 = models.URLField(blank=True, null=True)
