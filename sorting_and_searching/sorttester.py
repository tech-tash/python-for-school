# Programme sorting random numbers based on the size entered by user
# Author: Natasha Mazibuko
# Date: 06-10-2024

import sortsearch, random
from time import perf_counter

def main():
  size = int(input("Enter the size of the list:\n"))
  method = int(input("Choose the sort method:\n1. Selection Sort.\n2. Merge Sort. \n"))
  
  numbers = sortsearch.generate_number_list(size)    #generate list
  print("Before:", numbers)
  
  if method == 1:             #selection sort 
    start_time = perf_counter()     #start timer before sorting
    sort_num = sortsearch.selection_sort(numbers)
    end_time = perf_counter()        #stop timer after sorting
    time_taken = end_time - start_time
    
    print("After:", sort_num)
    print("Time: {:.9f}".format(time_taken))    #round to 9 decimal places
    
  elif method == 2:           #merge sort
    start_time = perf_counter()     #start timer before sorting
    sort_num = sortsearch.merge_sort(numbers)
    end_time = perf_counter()      #stop timer after sorting
    time_taken = end_time - start_time
    
    print("After:", sort_num)  
    print("Time: {:.9f}".format(time_taken))

  
if __name__== "__main__":
  main()