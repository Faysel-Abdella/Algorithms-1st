### Problem
# Given a sorted array return a new sorted array that contains the square of the first array elements

### Solution
# The simple(but no optimal) way is to create an empty array and append to it the 
# Square of the given array and finally sort it by saying .sort(). But this approach
# takes nlog(n) time complexity b/c of using .sort()

# So that the more optimal approach, which takes O(n) time complexity, is to use the following 
# FOR DESCRIPTION SEE THE VIDEO

def sortedSquared(array):
    newArray = [0 for _ in array] # create an array of size of 'array' and assign 0 to all indexes
    first = 0
    end = len(array) - 1
    
    for i in reversed(range(len(array))): # Start from back

        if( abs(array[first]) > abs(array[end]) ):
            newArray[i] = array[first] * array[first]
            first += 1   
        else:
            newArray[i] = array[end] * array[end]
            end -= 1
                  
    return newArray

print(sortedSquared([-3,-2,0,2,3,4,6]))              