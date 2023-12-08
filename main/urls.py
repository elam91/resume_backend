from django.urls import path, include
from rest_framework.routers import SimpleRouter
from main import views

router = SimpleRouter()
router.register("experiences", viewset=views.ExperienceView, basename="experiences")
router.register("long_descriptions", viewset=views.LongDescriptionView, basename="long_descriptions")
router.register("personal_info", viewset=views.PersonalInfoView, basename="personal_info")
router.register("projects", viewset=views.ProjectView, basename="projects")
router.register('skills', viewset=views.SkillView, basename="skills")
router.register('socials', viewset=views.SocialView, basename="socials")

urlpatterns = [
    path('', include(router.urls))]
