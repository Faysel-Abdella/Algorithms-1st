### PROBLEM
# Create a function that that takes a root node of a BT and returns a list of all of the branch sums in this BT.
# Branch sum is a sum of all of the values in a particular branch, where branch is a path in a BT that starts at the root node and end at one of the leaf nodes

### SOLUTION
# Time: O(N), where N is the total items in the BT


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
####
def branchSums(root):
    sums = []        
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None: #if the node does't exist 
        return
    
    newRunningSum = runningSum + node.value
    if node.left is not None and node.right is not None: #If we reach the leaf(Bottom)
        sums.append(newRunningSum)
        return
    
    #IF there is still brach call the function in both branch
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
        