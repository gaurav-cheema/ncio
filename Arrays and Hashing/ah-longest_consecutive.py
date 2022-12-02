# def longestConsecutive(nums: list[int]) -> int:
#     hash = dict.fromkeys(nums, 1)
    
import math
def solution(a):
    temp = 1
    res = 0
    for i in a:
        for j in a:
            res += (i*(10^helper(j))+j)
        
    return res

def helper(n):
    res = 0
    while n > 0:
        res += 1
        n = math.floor(n / 10)
    return res