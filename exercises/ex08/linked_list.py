"""Linked List Utils."""

from __future__ import annotations

__author__ = "730748337"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialize a Node object."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the Node stored at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    if index == 0:
        return head.value

    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")

    if head.next is None:
        return head.value

    max_of_rest = max(head.next)

    if head.value > max_of_rest:
        return head.value
    else:
        return max_of_rest


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of Nodes with the same values, in the same order, as the input list."""
    if len(items) == 0:
        return None

    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list where each value is multiplied by the scaling factor."""
    if head is None:
        return None

    return Node(head.value * factor, scale(head.next, factor))
