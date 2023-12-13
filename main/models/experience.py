from django.db import models
from django.db.models import CASCADE

from main.choices import ExperienceTypes


class Experience(models.Model):
    class Meta:
        ordering = ['order']

    organization_name = models.CharField(max_length=255, blank=False, null=False)
    title_name = models.CharField(max_length=255, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=False, null=False)
    experience_type = models.CharField(max_length=255, blank=False, null=False, choices=ExperienceTypes.choices)


# class ExperiencePoint(models.Model):
#     description = models.TextField(blank=True, null=True)
#     experience = models.ForeignKey("main.Experience", blank=False, null=False, on_delete=CASCADE, related_name="points")
#
#
# class ExperienceSubPoint(models.Model):
#     description = models.TextField(blank=True, null=True)
#     point = models.ForeignKey("main.ExperiencePoint", blank=False, null=False, on_delete=CASCADE,
#                               related_name="subpoints")
