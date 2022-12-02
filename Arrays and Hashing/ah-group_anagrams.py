from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    
    hash = defaultdict(list)
    
    for i in strs:
        temp = ''.join(sorted(i))
        hash.get(temp)
        
        if temp in hash.keys():
            hash[temp].append(i)
        else:
            hash[temp] = [i]

    return list(hash.values())
