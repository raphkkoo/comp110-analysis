"""While Loops Challenge"""

__author__: str = "730748337"

def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count

def get_evens(numbers: str) -> str:
    evens: str = ""
    index: int = 0
    
    while index < len(numbers):
        if int(numbers[index]) % 2 == 0:
            evens += numbers[index]
        index += 1
        
    return evens
    