"""finds the max of a list of numbers and returns the value (not the index)
If int_list is empty, returns None. If list is None, raises ValueError"""
#list -> int
def max_list_iter(int_list):  # must use iteration not recursion
   if int_list==None: 
      raise ValueError
   elif len(int_list)==0: #If the list is empty, returns None.
      return None
   else:
      max= int_list[0]
      for num in int_list: #Checks every number in the list.
         if num>max: #If the number is greater than the current maximum, it becomes the maximum.
            max=num
      return max

   
"""recursively reverses a list of numbers and returns the reversed list
If list is None, raises ValueError"""
#list -> list
def reverse_rec(int_list):   # must use recursion
   if int_list == None:
      raise ValueError
   elif len(int_list) <= 1: #If the list is empty or has one term, it will look the same when reversed. Base case.
      return int_list
   return [int_list[-1]] + reverse_rec(int_list[:-1]) #Creates a list with the last term of int_list and adds a recursive call to this function with a new list (int_list excluding the last term).


'''searches for target in int_list[low..high] and returns index if found
If target is not found returns None. If list is None, raises ValueError'''
#list -> int    
def bin_search(target, low, high, int_list):  # must use recursion
   if int_list == None: 
      raise ValueError
   elif low>high: #This means the target is not in the list.
      return None
   midpoint = (low+high)//2
   if int_list[midpoint] == target: #Checks if the term in the middle of the list equals the target.
      return midpoint 
   elif target > int_list[midpoint]: #If the target is greater than the midpoint term, it searches only the terms between the midpoint (excluding the midpoint) and high (including high).
      return bin_search(target,midpoint+1,high,int_list)
   elif target < int_list[midpoint]: #If the target is smaller than the midpoint term, it searches only the terms between the low (including low) and the midpoint (excluding the midpoint). 
      return bin_search(target, low, midpoint-1, int_list)
#V7


      

   
