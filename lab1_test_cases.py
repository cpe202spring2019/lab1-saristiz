import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    #TEST MAX_LIST_ITER
    def test_max_list_iter(self):
        """Checks for raising ValueError when the list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        """Checks if function returns None when the list is empty"""
        tlist=[]
        self.assertEqual(max_list_iter(tlist),None)
        """Checks if it returns the max value when it is the first value in the list"""
        tlist= [20,2,3,19]
        self.assertEqual(max_list_iter(tlist),20)
        """Checks if it returns the maximum value when the maximum value is in the middle of the list"""
        tlist=[9,8,10,2,9]
        self.assertEqual(max_list_iter(tlist),10)
        """Checks if it returns the max value when it is the last value in the list"""
        tlist=[9,11,2,3,8,1,12]
        self.assertEqual(max_list_iter(tlist),12)
        """Checks if it returns the correct value when there is only one value in the list"""
        tlist = [9]
        self.assertEqual(max_list_iter(tlist),9)
        """Checks if it returns the maximum value when using some negative and some positive values"""
        tlist=[2,-9,0,10,-23,11]
        self.assertEqual(max_list_iter(tlist),11)
        """Checks if it returns the maximum value when using all negative values"""
        tlist=[-20,-23,-3,-4,-9,-8]
        self.assertEqual(max_list_iter(tlist),-3)
        """Checks if it returns the maximum value when the maximum value is zero"""
        tlist=[-3,0,-1,-100,-9,-4,-35]
        self.assertEqual(max_list_iter(tlist),0)
        """Checks if it returns the maximum value when the maximum value is positive and repeated"""
        tlist=[4,5,-9,11,8,11,-2]
        self.assertEqual(max_list_iter(tlist),11)
        """Checks if it returns the maximum value when the maximum value is negative and repeated"""
        tlist = [-9,-90,-45,-31,-10,-9,-11]
        self.assertEqual(max_list_iter(tlist),-9)
        """Checks if it returns the correct value when all values in the list are the same and positive"""
        tlist = [10,10,10,10]
        self.assertEqual(max_list_iter(tlist),10)
        """Checks if it returns the correct value when all values in the list are the same and negative"""
        tlist = [-4, -4, -4, -4]
        self.assertEqual(max_list_iter(tlist),-4)
        """Checks if it returns the correct value when all values in the list are zero"""
        tlist = [0,0,0,0,0]
        self.assertEqual(max_list_iter(tlist),0)
        """Checks if it returns the correct value when the maximum value is zero"""
        tlist = [-2,-1,-9,-10,0]
        self.assertEqual(max_list_iter(tlist),0)


    #TEST REVERSE_REC    
    def test_reverse_rec_when_list_is_None(self):
        l=None
        with self.assertRaises(ValueError):
            reverse_rec(l)

    def test_reverse_rec_with_all_different_values(self):    
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([3,6,1,7,9,-1,-3,]),[-3,-1,9,7,1,6,3])

    def test_reverse_rec_when_length_of_list_equals_one(self):
        self.assertEqual(reverse_rec([9]),[9])

    def test_reverse_rec_list_of_length_2(self):
        self.assertEqual(reverse_rec([1,2]), [2,1])

    def test_reverse_rec_empty_list(self):
        self.assertEqual(reverse_rec([]),[])

    def test_reverse_rec_all_terms_same_number(self):
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])

    def test_reverse_rec_first_two_same_number(self):
        self.assertEqual(reverse_rec([1,1,2,3]),[3,2,1,1])
        self.assertEqual(reverse_rec([1,1,2,2]),[2,2,1,1])

    def test_reverse_rec_first_three_same_number(self):
        self.assertEqual(reverse_rec([1,1,1,2]),[2,1,1,1])

    def test_reverse_middle_two_same_number(self):
        self.assertEqual(reverse_rec([4,2,2,4]), [4,2,2,4])
        self.assertEqual(reverse_rec([1,2,2,5]),[5,2,2,1])
    
    def test_reverse_last_three_same_number(self):
        self.assertEqual(reverse_rec([1,2,2,2]), [2,2,2,1])

    
    #TEST BIN_SEARCH
    def test_bin_search_target_in_the_middle(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        list_val = [-1,2,3,7,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, low, high, list_val), 2)

    def test_bin_search_target_is_first_number(self):
        list_val = [-2,3,4,5,6,9,23]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-2, low, high, list_val),0)

    def test_bin_search_target_at_the_end(self):
        list_val = [-10,-8,-7,0,1,2,3,4,6]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(6, low, high, list_val), 8)

    def test_bin_search_target_not_found_in_the_middle_of_the_list(self):
        #Target is positive
        list_val = [-1,0,3,4,5,8,9,10]
        low = 0 
        high = len(list_val)-1
        self.assertEqual(bin_search(2, low, high, list_val), None)
        #Target is zero
        list_val = [-10, -8, -1, 3, 4, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0,low,high,list_val), None)
        #Target is negative
        list_val = [-10, -8, -7, -5, -1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-6, low, high, list_val), None)
    
    def test_bin_search_target_not_found_at_the_end_of_the_list(self):
        #Target is positive
        list_val = [-1,2,3,4,6,10]
        low=0
        high=len(list_val)-1
        self.assertEqual(bin_search(12, low, high, list_val), None)
        #Target is zero
        list_val = [-10, -9, -8, -6]
        low=0
        high=len(list_val)-1
        self.assertEqual(bin_search(0, low, high, list_val), None)
        #Target is negative
        list_val = [-10, -9, -8, -7]
        low=0
        high=len(list_val)-1
        self.assertEqual(bin_search(-6, low, high, list_val), None)

    def test_bin_search_target_not_found_in_the_beginning_of_the_list(self):
        #Target is zero
        list_val = [1,2,3,4]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, low, high, list_val), None)
        #Target is negative
        list_val = [-10, -9, -8, -7, -1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-12, low, high, list_val), None)
        #Target is positive
        list_val = [2,3,4,5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), None)

    def test_bin_search_empty_list(self):
        list_val = []
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(8, low, high, list_val), None)

    def test_bin_search_list_is_None(self):
        list_val = None
        low=0
        high=10
        with self.assertRaises(ValueError):
            bin_search(9, low, high, list_val)

    def test_bin_search_when_repeated_numbers(self):
        #Repeated values are in the middle
        list_val = [1,2,2,2,4,5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, low, high, list_val),2)
        #Repeated values are at the beginning
        list_val = [2,2,3,4,5,6]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, low, high, list_val), 0)
        #Repeated values are at the end
        list_val = [-10,-9,-8,-5,0,2,2]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, low, high, list_val), 5)


if __name__ == "__main__":
        unittest.main()
#V7
    
