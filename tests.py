from django.test import TestCase
from django.contrib.auth.models import User
from .models import BloodGroup, RequestBlood, Donor

class BloodGroupTestCase(TestCase):
    def setUp(self):
        self.blood_group = BloodGroup.objects.create(name="A+")

    def test_str_method(self):
        self.assertEqual(str(self.blood_group), "A+")

class RequestBloodTestCase(TestCase):
    def setUp(self):
        self.blood_group = BloodGroup.objects.create(name="B-")
        self.request_blood = RequestBlood.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            state="California",
            city="Los Angeles",
            address="123 Main St",
            blood_group=self.blood_group,
            date="2023-09-13",
        )

    def test_str_method(self):
        self.assertEqual(str(self.request_blood), "John Doe")

class DonorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="donoruser", password="password")
        self.blood_group = BloodGroup.objects.create(name="AB+")
        self.donor = Donor.objects.create(
            donor=self.user,
            date_of_birth="1990-01-01",
            phone="9876543210",
            city="New York",
            state="New York",
            address="456 Elm St",
            blood_group=self.blood_group,
            gender="Male",
            ready_to_donate=True,
        )

    def test_str_method(self):
        self.assertEqual(str(self.donor), "AB+")

    def test_donor_relationship(self):
        self.assertEqual(self.donor.donor.username, "donoruser")

    def test_ready_to_donate_default(self):
        self.assertTrue(self.donor.ready_to_donate)
