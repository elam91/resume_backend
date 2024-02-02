from datetime import datetime

import discord
from django.conf import settings
from django.utils import timezone

from main import renderers
from main.choices import ExperienceTypes
from main.models import PersonalInfo, Experience, Project, Skill



def send_to_discord():
    embed = discord.Embed(title="🚨Resume downloaded!🚨",
                          description=datetime.now().date().strftime('%d/%m/%Y'))
    embed.add_field(name=f"**Someone downloaded your resume!** 🧑🏼‍💻", value=f"hurray! 🥳")

    webhook_url = settings.DISCORD_WEBHOOK
    if webhook_url:
        webhook = discord.SyncWebhook.from_url(webhook_url)
        webhook.send(embed=embed)
    return

def pdf_view(request, *args, **kwargs):
    personal_info = PersonalInfo.objects.order_by('-created_at').first()
    experiences = Experience.objects.all()
    education = experiences.filter(experience_type=ExperienceTypes.EDUCATION).all()
    work = experiences.filter(experience_type=ExperienceTypes.WORK)
    projects = Project.objects.all()
    skills = Skill.objects.all()
    configuration_name = settings.CONFIGURATION.split(".")[-1]
    if configuration_name == 'Production':
        send_to_discord()


    data = {
        'date': timezone.now().date(),
        'personal_info': personal_info,
        'work_experience': work,
        'education': education,
        'skills': skills

    }

    return renderers.render_to_pdf('main/resume_export.html', data)