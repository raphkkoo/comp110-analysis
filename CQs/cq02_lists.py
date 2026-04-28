"""Mutating functions."""

__author__: str = "730748337"


def manual_append(a_list: list[int], number: int) -> None:
    """Mutates a list by appending an integer to the end."""
    a_list.append(number)


def double(a_list: list[int]) -> None:
    """Mutates a list by multiplying every element by 2."""
    index: int = 0
    while index < len(a_list):
        a_list[index] = a_list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
