from django.urls import reverse

from main.choices import ExperienceTypes
from main.tests.base import BaseAPITestCase


class GeneralAPITestCase(BaseAPITestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_experience_api(self):
        experience = self.given_experience_exists()
        detail_target_url = reverse('experiences-detail', args=[experience.id])
        list_target_url = reverse('experiences-list')
        # single item get
        res = self.client.get(detail_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['id'], experience.id)
        #list get
        res = self.client.get(list_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['count'], 1)

    def test_experience_filter(self):
        edu_experience = self.given_experience_exists(experience_type=ExperienceTypes.EDUCATION)
        work_experience = self.given_experience_exists(experience_type=ExperienceTypes.WORK)
        list_target_url = reverse('experiences-list')
        # list get with filter
        res = self.client.get(list_target_url, dict(experience_type=ExperienceTypes.WORK))
        self.verify_ok_status(res)
        self.assertEqual(res.data['count'], 1)
        returned_ids = [experience.get('id') for experience in res.data['results']]
        self.assertNotIn(edu_experience.id, returned_ids)
        self.assertIn(work_experience.id, returned_ids)


    def test_long_description_api(self):
        long_description = self.given_long_description_exists()
        detail_target_url = reverse('long_descriptions-detail', args=[long_description.page])
        list_target_url = reverse('long_descriptions-list')
        # single item get
        res = self.client.get(detail_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['id'], long_description.id)
        #list get
        res = self.client.get(list_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['count'], 1)



    def test_personal_info_api(self):
        personal_info = self.given_personal_info_exists()
        target_url = reverse('personal_info-latest')
        # latest item get
        res = self.client.get(target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['id'], personal_info.id)

        newer_personal_info = self.given_personal_info_exists(first_name="NEWER")

        # latest item get
        res = self.client.get(target_url)
        self.verify_ok_status(res)
        self.assertNotEqual(res.data['id'], personal_info.id)
        self.assertEqual(res.data['id'], newer_personal_info.id)

    def test_project_api(self):
        project = self.given_project_exists()
        detail_target_url = reverse('projects-detail', args=[project.id])
        list_target_url = reverse('projects-list')
        # single item get
        res = self.client.get(detail_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['id'], project.id)
        #list get
        res = self.client.get(list_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['count'], 1)


    def test_skill_api(self):
        skill = self.given_skill_exists()
        detail_target_url = reverse('skills-detail', args=[skill.id])
        list_target_url = reverse('skills-list')
        # single item get
        res = self.client.get(detail_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['id'], skill.id)
        #list get
        res = self.client.get(list_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['count'], 1)

    def test_social_api(self):
        social = self.given_social_exists()
        detail_target_url = reverse('socials-detail', args=[social.id])
        list_target_url = reverse('socials-list')
        # single item get
        res = self.client.get(detail_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['id'], social.id)
        #list get
        res = self.client.get(list_target_url)
        self.verify_ok_status(res)
        self.assertEqual(res.data['count'], 1)

