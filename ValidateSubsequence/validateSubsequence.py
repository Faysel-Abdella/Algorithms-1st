### Problem
# Given two arrays write a function that check if the second array is a valid subsequence of the first one
# subsequence is the sequence that result by removing some element of another sequence
# for example [1,6,-1,10] is subsequence of [5,1,22,25,6,-1,8,10], the order is must 



def validateSubsequence(originalSequence, subSequence):
    originalPointer = 0
    subSequencePointer= 0
    while subSequencePointer < len(subSequence) and originalPointer < len(originalSequence):
        if(subSequence[subSequencePointer] == originalSequence[originalPointer]):
            originalPointer += 1
            subSequencePointer += 1
        else:
            originalPointer += 1    
        if(subSequencePointer == len(subSequence)):
            return True
    return False

print(validateSubsequence([5,1,22,25,6,-1,8,10], [1,6,-1,0]))        