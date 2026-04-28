"""List Utility Functions"""

__author__: str = "730748337"


def all(ints: list[int], target: int) -> bool:
    if len(ints) == 0:
        return False

    for num in ints:
        if num != target:
            return False  # Short-circuit and return immediately

    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    # Start by assuming the first item is the largest
    current_max = input[0]

    for num in input:
        if num > current_max:
            current_max = num

    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False

    # use a while loop to track the index
    i = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for num in list2:
        list1.append(num)
