from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ test create user """
        email = 'WBM@qq.com'
        password = '517438'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''test the email for user is normalized'''
        email = 'wbm@QQ.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='12456'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_eamil(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'TEst123')

    def test_create_new_super_user(self):
        '''test creating new super user'''
        user = get_user_model().objects.create_superuser(
            email='wbm@qq.com',
            password='123456'
        )
        self.assertTrue(user.is_staff)
