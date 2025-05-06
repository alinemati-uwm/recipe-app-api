"""
Tests for the models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = "test@example.com"
        password = "testpassword123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_emails = [
            ("test1@EXAMPLE.COM", "test1@example.com"),
            ("Test2@Example.COM", "test2@example.com"),
            ("TEST3@EXAMPLE.COM", "test3@example.com"),
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email=email,
                                                        password='sample123')
            self.assertEqual(user.email, expected)
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, \
                                                    password='sample123')
            
    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser( 
            email="test@example.com",
            password="testpassword123"
        )
        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)
        