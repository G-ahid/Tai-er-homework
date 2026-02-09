from typing import Any
nums = ['0','1','2','3','4','5','6','7','8','9']

def toInt(n:str) -> int | None:
    """
        Turns a **string** into a **number**,
        if it cannot be turned, it returns **None**
    """
    for chacarter in n:
        if chacarter not in nums:
            return None
    return int(n)

def removeDuplicates(l:list[Any]) -> list[Any]:
    """
        Return **a copy of the list** that does not have any **duplicates**
    """
    lst = list(l)
    # It is reversed so when we remove an element, the for loop still works
    for i in reversed(range(len(lst) - 1)):
        if  (i != len(lst) and lst[i] in lst[:i]) or (i != 0 and lst[i] in lst[i+1:]):
            lst.pop(i)
    
    return lst

def sort(lst:list[str], item:str) -> list[int]:
    """
        sorts a list, and returns the indicies of the found elements
    """
    result:list[int] = []
    for i in range(len(lst)):
        if item.lower() in lst[i].lower():
            result.append(i)
    return result