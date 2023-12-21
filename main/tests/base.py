import json
from typing import Dict

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from model_bakery import baker

from main.models import Experience, LongDescription, PersonalInfo, Project, Skill, Social


class BaseAPITestCase(APITestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        super().setUp()
        self.strong_password = 'AkujoErutho187!'

    def tearDown(self):
        super().tearDown()

    def given_user_exists(self, **kw):
        user = get_user_model().objects.create_user(username='tester1234', email=kw.get('email', "test@test.com"),
                                                    is_staff=False,
                                                    is_superuser=False,
                                                    password=kw.get('password', self.strong_password),
                                                    first_name="Test", last_name="Tester")
        return user

    def given_admin_user_exists(self, **kw):
        user = get_user_model().objects.create_user(user='admintester1234', email=kw.get('email', "admin@test.com"),
                                                    is_staff=False,
                                                    is_superuser=True,
                                                    password=kw.get('password', self.strong_password),
                                                    first_name="Test", last_name="Tester")
        return user

    def verify_ok_status(self, res):
        self.assertIn(res.status_code, [200, 201])

    def given_user_unauthenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION="")

    def given_user_authenticated(self, email='test_user@test.com', password=None):
        if not password:
            password = self.strong_password
        auth_url = reverse("token-obtain-pair")
        res = self.client.post(auth_url, data=dict(email=email, password=password))
        access_token = res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

    def verify_user_can_authenticate(self, email='test_user@test.com', password='Test1Test2'):
        auth_url = reverse("token-obtain-pair")
        res = self.client.post(auth_url, data=dict(email=email, password=password))
        self.verify_ok_status(res)

    def when_user_is_created_via_api(self, **params):
        url = reverse('users-list')
        user_dict = dict(
            password=params.get('password', self.strong_password),
            confirm_password=params.get('password', self.strong_password),
            email=params.get('email', 'test_user@test.com'),
            first_name=params.get('first_name', 'test'),
            last_name=params.get('last_name', 'user'),
        )
        res = self.client.post(url, json.dumps(user_dict), content_type="application/json")
        return res

    def given_experience_exists(self, **kwargs):
        return baker.make(Experience, **kwargs)

    def given_long_description_exists(self, **kwargs):
        return baker.make(LongDescription, **kwargs)

    def given_personal_info_exists(self, **kwargs):
        return baker.make(PersonalInfo, **kwargs)

    def given_project_exists(self, **kwargs):
        return baker.make(Project, **kwargs)

    def given_skill_exists(self, **kwargs):
        return baker.make(Skill, **kwargs)

    def given_social_exists(self, **kwargs):
        return baker.make(Social, **kwargs)
