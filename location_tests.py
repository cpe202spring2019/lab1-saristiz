import unittest
from location import *

class TestLab1(unittest.TestCase):
    #The first test cases make sure repr is returning the correct string
    def test_repr_1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr_2(self):
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc), "Location('Paris', 48.9, 2.4)")

    def test_repr_3(self):
        loc = Location("Medellin",3.4,-140)
        self.assertEqual(repr(loc),"Location('Medellin', 3.4, -140)")
    
    def test_repr_4(self):
        loc = Location("Slo", 11.45, 7.622)
        self.assertEqual(repr(loc), "Location('Slo', 11.45, 7.622)")

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

    def test_equality_same_type_different_last_attribute_by_decimal_place(self):
        loc1 = Location("New York", 56.7, -76.56)
        loc2 = Location("New York", 56.7, -76.567)
        self.assertFalse(loc1==loc2)
        loc1 = Location("New York", 56.7, -76.56)
        loc2 = Location("New York", 56.7, -76.57)
        self.assertFalse(loc1==loc2)
        loc1 = Location("New York", 56.7, -76)
        loc2 = Location("New York", 56.7, -76.0)
        self.assertTrue(loc1==loc2)
    
    def test_equality_same_type_different_2_last_attributes(self):
        loc1 = Location("Bogota", -89, 100)
        loc2 = Location("Bogota", -88, 99)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_two_different_last_attributes_by_decimal(self):
        loc1 = Location("Bogota", -89.1, 100)
        loc2 = Location("Bogota", -89, 99)
        self.assertFalse(loc1==loc2)
        loc1 = Location("Bogota", -89, 100.11)
        loc2 = Location("Bogota", -89, 100.12)
        self.assertFalse(loc1==loc2)
        loc1 = Location("Bogota", -89.1, 100)
        loc2 = Location("Bogota", -89, 100.1)
        self.assertFalse(loc1==loc2)
        loc1 = Location("Bogota", -89.10, 99.200)
        loc2 = Location("Bogota", -89.1, 99.2)
        self.assertTrue(loc1==loc2)

    def test_equality_same_type_different_3_attributes(self):
        loc1 = Location("San Andres", -9, 8)
        loc2 = Location("Bucaramanga", 10, 2)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_3_attributes_by_decimal(self):
        loc1 = Location("San Andres", -9.1, 8)
        loc2 = Location("Bucaramanga", -9, 2)
        self.assertFalse(loc1==loc2)
        loc1 = Location("San Andres", -9, 8.1)
        loc2 = Location("Bucaramanga", 10, 8)
        self.assertFalse(loc1==loc2)
        loc1 = Location("San Andres", -9.1, 8.21)
        loc2 = Location("Bucaramanga", -9.2, 8.2)
        self.assertFalse(loc1==loc2)

    def test_equality_different_type_same_name(self):
        loc1 = Location("San Francisco", 10, 179)
        loc2 = "San Francisco"
        self.assertFalse(loc1==loc2)

    def test_equality_different_type(self):
        loc1 = Location("San Francisco", 10, 179)
        loc2 = 1
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_middle_attribute(self):
        loc1 = Location("Leticia", -70, 100)
        loc2 = Location("Leticia", -10, 100)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_middle_attribute_by_decimal(self):
        loc1 = Location("Leticia", -70, 100)
        loc2 = Location("Leticia", -70.1, 100)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_middle_and_first_attributes(self):
        loc1 = Location("Miami",56.4,-33.2)
        loc2 = Location("San Luis Obispo", 34.5, -33.2)
        self.assertFalse(loc1==loc2)
    
    def test_equality_same_type_different_middle_and_first_attributes_by_decimal(self):
        loc1 = Location("Miami",56.4,-33.2)
        loc2 = Location("San Luis Obispo", 56.41, -33.2)
        self.assertFalse(loc1==loc2)
  
    def test_equality_same_type_different_case_in_first_attribute(self):
        loc1 = Location("Medellin", 34, 70)
        loc2 = Location("medellin", 34, 70)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_first_attribute(self):
        loc1 = Location("Medellin", 34, -20)
        loc2 = Location("Cali", 34, -20)
        self.assertFalse(loc1==loc2)

    def test_equality_same_type_different_ending_first_attribute(self):
        loc1 = Location("San Luis Obispo", 34.5, -33.2)
        loc2 = Location("San Luis", 34.5, -33.2)
        self.assertFalse(loc1==loc2)

    def test_init_name(self):
        loc1 = Location("San Luis Obispo", 34.5, -33.2)
        self.assertEqual(loc1.name, "San Luis Obispo")

    def test_init_lat(self):
        loc1 = Location("San Luis Obispo", 34.5, -33.2)
        self.assertEqual(loc1.lat, 34.5)
        
    def test_init_lon(self):
        loc1 = Location("San Luis Obispo", 34.5, -33.2)
        self.assertEqual(loc1.lon, -33.2)
    

if __name__ == "__main__":
        unittest.main()
#V7
