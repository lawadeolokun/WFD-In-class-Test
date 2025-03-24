import unittest

from PartA import Staff, Doctor

class TestStaffDoctor(unittest.TestCase):
    
    def setUp(self):
        self.staff = Staff("Steven Smith", "04/12/1988", "Male", "12345", "53 Waterville Terrace")
        self.doctor = Doctor("Sandra Johnson", "17/05/1993", "Female", "90152", "4 Ballentree Lodge", "Cardiology", "21", "€123,000")

    def test_is_instance(self):
        self.assertIsInstance(self.staff,Staff)
        self.assertIsInstance(self.doctor,Doctor)
        self.assertIsInstance(self.doctor, Staff)

    def test_is_not_instance(self):
        self.assertNotIsInstance(self.staff, Doctor)

    def test_object_identify(self):
        staff2 = self.staff
        self.assertIs(self.staff, staff2)