import unittest
from location import *

class TestLab1(unittest.TestCase):
    #what other types of tests do we need to add here?
    def test_repr_1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr_2(self):
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc), "Location('Paris', 48.9, 2.4)")

    '''def test_repr_3(self):
        loc = Location("Medellin",3.4,-140)
        self.assertEqual(repr(loc),"Location('Medellin', 3.4, -140)")'''

    def test_equality_same_object(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = loc1
        self.assertTrue(loc1==loc2)
    
    def test_equality_same_type_same_attributes(self):
        loc1 = Location("Toronto", 40.1, 23)
        loc2 = Location("Toronto", 40.1, 23)
        self.assertTrue(loc1==loc2)

    def test_equality_same_type_different_last_attribute(self):
        loc1 = Location("Cali", 3.4, -120)
        loc2 = Location("Cali", 3.4, -119)
        self.assertFalse(loc1==loc2)
    
    def test_equality_same_type_different_2_last_attributes(self):
        loc1 = Location("Bogota", -89, 100)
        loc2 = Location("Bogota", -88, 99)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_3_attributes(self):
        loc1 = Location("San Andres", -9, 8)
        loc2 = Location("Bucaramanga", 10, 2)
        self.assertFalse(loc1==loc2)

    def test_equality_different_type(self):
        loc1 = Location("San Francisco", 10, 180)
        loc2 = "San Francisco"
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_middle_attribute(self):
        loc1 = Location("Leticia", -70, 100)
        loc2 = Location("Leticia", -70.1, 100)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_middle_and_first_attributes(self):
        loc1 = Location("Miami",56.4,-33.2)
        loc2 = Location("San Luis Obispo", 34.5, -33.2)
        self.assertFalse(loc1==loc2)

    #Should this be true or false?    
    def test_equality_same_type_different_case_in_first_attribute(self):
        loc1 = Location("Medellin", 34, 70)
        loc2 = Location("medellin", 34, 70)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_first_attribute(self):
        loc1 = Location("Medellin", 34, -20)
        loc2 = Location("Cali", 34, -20)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_ending_middle_attribute(self):
        loc1 = Location("San Luis Obispo", 34.5, -33.2)
        loc2 = Location("San Luis", 34.5, -33.2)
        self.assertFalse(loc1==loc2)

    

    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
