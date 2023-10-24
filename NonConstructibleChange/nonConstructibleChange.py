#### PROBLEM
### The minimum number that can't be made by adding some elements of an array
### using one item twice is not allowed

#### SOLUTION
# For the explanation see the video
# O(nlogn) time | O(1) space
def findMinimumCant(coins):
    coins.sort()
    minimumCant = 0
    for coin in coins:
        if(coin <= minimumCant + 1):
            minimumCant += coin
    return minimumCant + 1

print(findMinimumCant([5,7,1,1,2,3,22]))        
        
