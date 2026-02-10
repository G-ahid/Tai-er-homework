from typing import Any
nums:list[str] = ['0','1','2','3','4','5','6','7','8','9']
powers:list[str] = [
    "thousand",
    "million",
    "billion"
]

def toInt(n:str) -> int | None:
    """
        Turns a **string** into a **number**,
        if it cannot be turned, it returns **None**
    """
    for chacarter in n:
        if chacarter not in nums:
            return None
    return int(n)

def toIntForce(n:str, Default:int = 0) -> int:
    """
        Unlike toInt this function will not return a None
        if the string cannot be turned into a number,
        it would ignore all the characters, that
        aren't digits, and return them as an int.
    """
    result:str = ''
    for character in n:
        if character in nums:
            result += character
    
    return int(result) if len(result) != 0 else Default

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

def find(lst:list[str], item:str) -> list[int]:
    """
        Returns the indicies of the found elements
    """
    result:list[int] = []
    for i in range(len(lst)):
        if item.lower() in lst[i].lower():
            result.append(i)
    return result

def StringToNum(n:str) -> int:
    """
        Gets a String like _"100 million"_
        and turns it into an actual integer
    """
    n:str = n.lower()
    for i,power in enumerate(powers):
        if power in n:
            return toIntForce(n.replace(power,'')) * 10 ** (3 * (i+1))
    return toIntForce(n)

def NumToString(n:int) -> str:
    i = -1
    while n > 1000:
        n /= 1000
        i += 1
    return f"{n:.0f}{(" "+str(powers[i])) if i >= 0 else ''}"