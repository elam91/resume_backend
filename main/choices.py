from django.db.models import TextChoices


class ExperienceTypes(TextChoices):
    WORK = 'WORK', ('Work')
    EDUCATION = 'EDU', ('Education')


class DescriptionPages(TextChoices):
    INTRO = 'INTRO', ('Introduction')
    EXPERIENCE = 'EXP', ('Experience')
