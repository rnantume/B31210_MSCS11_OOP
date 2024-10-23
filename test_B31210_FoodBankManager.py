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
        self.assertIsNotNone(self.id)  # Ensure an ID is generated
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

    def test_get_details(self):
        """Test the get_details method of the Refugee class."""
        expected = "Name: Herbert B, Contact No: 0788776655, Address: madi okollo camp, Family size: 7, Origin Country: DRC"
        self.assertIn(expected, self.refugee.get_details())

class TestFoodandUnitClasses(unittest.TestCase):
    def setUp(self):
        """Setting up test cases with sample data."""
        self.unit = Unit("Rice", 10)
        self.food = Food("Rice", self.unit)

    def test_unit_initialization(self):
        """Test initialization of Unit."""
        self.assertIsInstance(self.unit, Unit)
        self.assertEqual(self.unit.name, "Rice")
        self.assertNotEqual(self.unit.name, "Beans")
        self.assertEqual(self.unit.quantity_per_family_member, 10)
        self.assertIsNotNone(self.unit.id)

    def test_get_unit_cap(self):
        """Test get_unit_cap method of Unit."""
        self.assertEqual(self.unit.get_unit_cap(), 10)

    def test_food_initialization(self):
        """Test initialization of Food."""
        self.assertIsInstance(self.food, Food)
        self.assertEqual(self.food.name, "Rice")
        self.assertIs(self.food.unit, self.unit)  # Check if both evaluate to the same object
        self.assertIsNotNone(self.food.id)  # Ensure an ID is generated

    def test_food_unit_type_check(self):
        """Test Food initialization with invalid unit type."""
        with self.assertRaises(TypeError):
            Food("Flour", "Six")

    def test_setter_valid_unit(self):
        """Test setter for valid unit."""
        new_unit = Unit("Flour", 8)
        self.food.unit = new_unit
        self.assertIs(self.food.unit, new_unit)

    def test_setter_invalid_unit(self):
        """Test setter for invalid unit type."""
        with self.assertRaises(TypeError):
            self.food.unit = "Eight"

    def test_get_details(self):
        """Test get_details() of Food."""
        expected = f"Food ID: {self.food.id}, Food Name: Rice, Unit of Release: 10"
        self.assertEqual(self.food.get_details(), expected)


if __name__ == '__main__':
    unittest.main()