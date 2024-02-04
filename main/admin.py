from django.contrib import admin
from django.db import models
from import_export.admin import ImportExportModelAdmin
from tinymce.widgets import TinyMCE

from main.models import Experience, LongDescription, PersonalInfo, Project, Skill, Social


# Register your models here.π
@admin.register(Experience)
class ExperienceAdmin(ImportExportModelAdmin):
    list_display = ['title_name', 'organization_name', 'start_date', 'end_date', 'order']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


@admin.register(LongDescription)
class LongDescriptionAdmin(ImportExportModelAdmin):
    list_display = ['body', 'page']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


@admin.register(PersonalInfo)
class PersonalInfoAdmin(ImportExportModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'residence', 'email', 'birthdate', 'created_at']


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    list_display = ['name', 'description', 'order', 'website_link', 'github_link']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }



@admin.register(Skill)
class SkillAdmin(ImportExportModelAdmin):
    list_display = ['name', 'description', 'order']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


@admin.register(Social)
class SocialAdmin(ImportExportModelAdmin):
    list_display = ['name', 'description', 'order', 'url']

