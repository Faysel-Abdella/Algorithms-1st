### The problem
# Given an array and a number(k) find two numbers from array that give k when submission

### Solution

## With Time complexity O(n^2) and space Com O(1)

# def twoNumberSum(array, targetNumber):
#     for i in range(len(array) -1):
#         for j in range(i+1, len(array)):
#             if(array[i] + array[j] == targetNumber):
#                 return [array[i], array[j]]
#     return []
# print(twoNumberSum([-2,3,9,3,-1], 8))        
  
## With Time complexity O(n) and space Com O(n)  <--- More Efficient that the above

# def twoNumberSum(array, targetNumber):
#     nums = {}
#     for number in array:
#         y = targetNumber - number
#         if y in nums:
#             return [y, number]
#         else:
#             nums[number] = True
#     return []    
# print(twoNumberSum([-2,3,9,3,-1], 1)) 

## USING TWO POINTERS- With Time complexity O(1) and space Com O(1)  <--- More Efficient that the above

# HOW?
#-Sort the array
#-Use two pointers. assign initially the first and the last element (right and left )
#-add the value of the two pointers, if the value is greater than the targeted value move the right pointer one step to the left
#-if the value is less than the targeted value move the right pointer one step to the left

def twoNumberSum(array, targetNumber):
    array.sort()
    left = 0
    right = len(array)-1
    
    while left < right: #While the two pointer doesn't intersect
        sum = array[left] + array[right]
        if(sum == targetNumber):
            return [array[left], array[right]]
        elif (sum < targetNumber):
            left += 1
        elif (sum > targetNumber):
            right -= 1
    return []            
print(twoNumberSum([-2,3,9,3,-1,4], 8))