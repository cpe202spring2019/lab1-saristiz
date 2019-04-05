
def max_list_iter(int_list):  # must use iteration not recursion
   if int_list==None:
      raise ValueError
   elif len(int_list)==0:
      return None
   else:
      max= int_list[0]
      for num in int_list:
         if num>max:
            max=num
      return max
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   

def reverse_rec(int_list):   # must use recursion
   if int_list == None:
      raise ValueError
   elif len(int_list) <= 1:
      return int_list
   return [int_list[-1]] + reverse_rec(int_list[:-1])

   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   
#ARE WE ASSUMING LOW AND HIGH ARE INTEGERS AND THE LIST IS SORTED?
def bin_search(target, low, high, int_list):  # must use recursion
   if int_list == None:
      raise ValueError
   elif low>high:
      return None
   midpoint = (low+high)//2
   if int_list[midpoint] == target:
      return midpoint 
   elif target > int_list[midpoint]:
      return bin_search(target,midpoint+1,high,int_list)
   elif target < int_list[midpoint]:
      return bin_search(target, low, midpoint-1, int_list)


      
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
