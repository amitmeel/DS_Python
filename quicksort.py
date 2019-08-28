# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:44:02 2018

@author: amit
"""

def partition(arr,low,high):
    """ this function return the partitioning index of an array.
    
        this function take last element as pivot, placed the pivot elemtnt in its correct
        position in sorted array and place all smaller element then pivot to left of pivot
        and all greater elements to right of pivot.
    Args:
        arr: array.
        low: starting index of array.
        high: last index of array.
    Returns:
        partitioning index. 
    """
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
  
def quickSort(arr,low,high):
    """This function will sort the given array using Quicksort approach.
    
    Args:
        arr : array that need to be sorted.
        low : starting index of array.
        high : last index of array.
    Returns:
        Sorted array.
    """
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr,low,high)
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr
 
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print(quickSort(arr,0,n-1))
#print ("Sorted array is: ",arr)






"""
import random  
def quicksort(array):
    if not array:
        return array # in case fo empty array
    pivot = array[random.choice(range(0, len(array)))] #to chosse any random number from array as pivot

    lefthalf = quicksort([elem for elem in array if elem < pivot]) #array elements that are less then pivot element
    righthalf = quicksort([elem for elem in array if elem > pivot]) #array element that are greater than pivot element
    return lefthalf + [elem for elem in array if elem == pivot] + righthalf

print(quicksort([1,5,2,7,4,3,9]))
"""


#is just for understanding approach not the memory efficient approach
"""
def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
        
print(sort([3,42,4,2,5]))
"""