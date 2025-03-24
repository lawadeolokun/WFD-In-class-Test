import unittest

from PartA import Staff, Doctor

class TestStaffDoctor(unittest.TestCase):
    
    def setUp(self):
        self.staff = Staff("Steven Smith", "04/12/1988", "Male", "12345", "53 Waterville Terrace")
        self.doctor = Doctor("Sandra Johnson", "17/05/1993", "Female", "90152", "4 Ballentree Lodge", "Cardiology", 123000, 21)

    def test_is_instance(self):
        self.assertIsInstance(self.staff,Staff)
        self.assertIsInstance(self.doctor,Doctor)
        self.assertIsInstance(self.doctor, Staff)

    def test_is_not_instance(self):
        self.assertNotIsInstance(self.staff, Doctor)

    def test_object_identify(self):
        staff2 = self.staff
        self.assertIs(self.staff, staff2)

    def test_update_name(self):
        self.staff.update_name("Robert")
        self.assertEqual(self.staff.name, "Robert")

    def test_update_DoB(self):
        self.staff.update_DoB("11/11/2000")
        self.assertEqual(self.staff.DoB, "11/11/2000")

    def test_update_sex(self):
        self.staff.update_sex("Female")
        self.assertEqual(self.staff.sex, "Female")

    def test_update_staffID(self):
        self.staff.update_staffID("B1003847")
        self.assertEqual(self.staff.staffID, "B1003847")

    def test_update_address(self):
        self.staff.update_address("1230 NewTown Road")
        self.assertEqual(self.staff.address, "1230 NewTown Road")

    def test_update_specialisation(self):
        self.doctor.update_specialisation("anesthesiology")
        self.assertEqual(self.doctor.specialisation, "anesthesiology")

    def test_update_salary(self):
        self.doctor.update_salary(100000)
        self.assertEqual(self.doctor.salary, 100000)

    def test_update_years_experience(self):
        self.doctor.update_years_experience(25)
        self.assertEqual(self.doctor.years_experience, 25)

if __name__ == '__main__':
    unittest.main()