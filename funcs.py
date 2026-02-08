from typing import Any
nums = ['0','1','2','3','4','5','6','7','8','9']

def toInt(n:str) -> int | None:
    isNumber:bool = True
    for chacarter in n:
        if chacarter not in nums:
            return None
    return int(n)

def removeDuplicates(l:list[Any]) -> list[Any]:
    lst = list(l)
    for i in reversed(range(len(lst) - 1)):
        if  (i != len(lst) and lst[i] in lst[:i]) or (i != 0 and lst[i] in lst[i+1:]):
            lst.pop(i)
    
    return lst

def sort(lst:list, item:str) -> list[int]:
    result:list[int] = []
    for i in range(len(lst)-1):
        if item in lst[i]:
            result.append(i)
    return result