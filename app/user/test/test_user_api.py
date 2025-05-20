"""
Test cases for the User API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


from rest_framework import status
from rest_framework.test import APIClient


CREATE_USER_URL = reverse("user:create")


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """
    TestCase for public user API endpoints.
    This test class covers the following scenarios:
    - Successful creation of a new user via the public API.
    - Ensuring user passwords are securely hashed and not returned in API responses.
    - Preventing duplicate user creation with the same email and returning appropriate error messages.
    Each test simulates HTTP requests to the user API endpoints and verifies both the API response and the resulting database state.
    Annotations:
    -----------
    - Uses Django's TestCase for isolated test execution.
    - Utilizes DRF's APIClient for simulating API requests.
    - Ensures compliance with security best practices (e.g., password hashing, sensitive data exclusion).
    - Validates error handling for duplicate user registration.
    """
    """Test the public features of the user API."""

    def setUp(self):
        self.client = APIClient() # Create an instance of the APIClient for making requests

    def test_create_user_success(self):
        """Test creating a user is successful."""
        payload = {
            "email": "test@example.com",
            "password": "testpass123",
            "name": "Test Name",
        }
        # Make a POST request to the user creation URL with the payload
        res = self.client.post(CREATE_USER_URL, payload) 

        # assert the response status code is 201 (created)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # assert the user is created in the database
        user = get_user_model().objects.get(email=payload["email"])
        # assert the user password is hashed
        self.assertTrue(user.check_password(payload["password"]))
        # assert the user name is set correctly
        self.assertEqual(user.name, payload["name"])
        # assert the response contains the expected user data
        self.assertNotIn("password", res.data)


    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists."""
        payload = {
            "email": "test@example.com",
            "password": "pw",
            "name": "Test Name",
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data["email"], ["user with this email already exists."]) 