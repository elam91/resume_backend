from http.client import HTTPResponse

from django.template.response import TemplateResponse
from django.utils import timezone
from django.views import View

from main import renderers
from main.choices import ExperienceTypes
from main.models import PersonalInfo, Experience, Project, Skill
from main.serializers import PersonalInfoSerializer, ExperienceSerializer, SkillSerializer
from main.serializers.experience_serializer import PDFExperienceSerializer


def pdf_view(request, *args, **kwargs):
    personal_info = PersonalInfo.objects.order_by('-created_at').first()
    experiences = Experience.objects.all()
    education = experiences.filter(experience_type=ExperienceTypes.EDUCATION).all()
    work = experiences.filter(experience_type=ExperienceTypes.WORK)
    projects = Project.objects.all()
    skills = Skill.objects.all()


    data = {
        'date': timezone.now().date(),
        'personal_info': personal_info,
        'work_experience': work,
        'education': education,
        'skills': skills

    }

    return renderers.render_to_pdf('main/resume_export.html', data)