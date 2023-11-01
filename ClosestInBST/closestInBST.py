### PROBLEM
# Find the closest value for a given value in BST

## Time:
# Average -> O(log(n)) , since most of BST operation are O(log(n))
# Worst -> O(N) , if the tree is street and we can't , when we have only one branch



##### RECURSIVELY APPROACH
def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float("inf"))

def findClosestValueInBSTHelper(tree, target, closest):
    if tree is None: # If we reach the bottom(leaf) of the BST
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target == tree.value:
        return closest    
    elif target < tree.value:
        return findClosestValueInBSTHelper(tree.left, target, closest)
    else:
        return findClosestValueInBSTHelper(tree.right, target, closest)    
            
#### ITERATIVE APPROACH  (The Easy) 
def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float("inf"))

def findClosestValueInBSTHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if currentNode.value > target:
            currentNode = currentNode.left
        elif currentNode.value < target:
            currentNode = currentNode.right
        else: #if equal
            break
    return closest    
                                 