from collections import defaultdict

def topKFrequent(nums: list[int], k: int) -> list[int]:
    hash = defaultdict(int)
    
    for i in nums:
        if i in hash.keys():
            hash[i] += 1
        else:
            hash[i] = 1

    hash = dict(sorted(hash.items(), key = lambda x:x[1], reverse=True))
    
    return list(hash.items())[0:k]