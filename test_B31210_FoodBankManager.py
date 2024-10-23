# Unit tests for B31210_FoodBankManager.py

import unittest
import datetime
import uuid
from B31210_FoodBankManager import Person, Refugee, Donor, Unit, Food, Supply, Donation, Distribution, Inventory

class TestPerson(unittest.TestCase):
    def setUp(self):
        """setting up a Person instance"""
        self.person = Person("Robin", "0750111222", "Mukono 1st str")

    def test_get_details(self):
        details = self.person.get_details()
        self.assertIn("Robin", details)

class TestDonor(unittest.TestCase):

    def setUp(self):
        """Setting a Donor instance"""
        self.donor = Donor("Robin", "0750111222", "Mukono 1st st", True)

    def test_initialization(self):
        """Testing that Donor is initialized properly"""
        self.assertEqual(self.donor.name, "Robin")
        self.assertEqual(self.donor.contact, "0750111222")
        self.assertEqual(self.donor.address, "Mukono 1st st")
        self.assertTrue(self.donor.is_organisation)

    def test_get_details(self):
        """Test the get_details method of the Donor class."""
        expected = "Name: Robin, Contact No: 0750111222, Address: Mukono 1st st, Is Organisation: True"
        # ID exlcluded from the assertion because it is dynamically assigned
        self.assertIn(expected, self.donor.get_details())

class TestRefugee(unittest.TestCase):

    def setUp(self):
        """Setting up Refugee instance for unittesing"""
        self.refugee = Refugee("Herbert B", "0788776655", "madi okollo camp", 7, "DRC")

    def test_initialization(self):
        """Testing that Refugge is initialized properly"""
        self.assertEqual(self.refugee.name, "Herbert B")
        self.assertEqual(self.refugee.contact, "0788776655")
        self.assertEqual(self.refugee.address, "madi okollo camp")
        self.assertEqual(self.refugee.family_size, 7)
        self.assertEqual(self.refugee.origin_country, "DRC")

    def test_get_details(self):
        """Test the get_details method of the Refugee class."""
        expected = "Name: Herbert B, Contact No: 0788776655, Address: madi okollo camp, Family size: 7, Origin Country: DRC"
        self.assertIn(expected, self.refugee.get_details())

if __name__ == '__main__':
    unittest.main()