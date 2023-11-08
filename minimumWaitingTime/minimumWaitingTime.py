### For problem look at the video

# O(nlogn) time b/c of sort

def minimumWaitingTime(queries):
    queries.sort()
    total = 0
    length = len(queries) - 1
    for i in range(len(queries) - 1):
        total += queries[i] * length
        length -= 1
        
    return total

print(minimumWaitingTime([2,2,3,6,1]))    