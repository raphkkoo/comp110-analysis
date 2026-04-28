"""Dictionary Unit Tests."""

__author__: str = "730748337"

import pytest
from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)

"""Tests for invert."""


def test_invert_use_case_1():
    """Test invert with dictionary of single characters."""
    test_dict = {"a": "z", "b": "y", "c": "x"}
    assert invert(test_dict) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_case_2():
    """Test invert with dictionary of words."""
    test_dict = {"apple": "cat", "banana": "dog"}
    assert invert(test_dict) == {"cat": "apple", "dog": "banana"}


def test_invert_edge_case_keyerror():
    """Test that invert raises a KeyError when duplicates."""
    with pytest.raises(KeyError):
        my_dictionary = {"alyssa": "byrnes", "adam": "byrnes"}
        invert(my_dictionary)


"""Tests for favorite_color."""


def test_favorite_color_use_case_1():
    """Test favorite_color with clear majority color."""
    test_dict = {"Marc": "yellow", "Ezri": "blue", "Krisi": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_use_case_2():
    """Test favorite_color with different set of majority colors."""
    test_dict = {"Alice": "red", "Bob": "red", "Charlie": "green", "Dave": "red"}
    assert favorite_color(test_dict) == "red"


def test_favorite_color_edge_case():
    """Test favorite_color with tie."""
    test_dict = {"Marc": "yellow", "Ezri": "blue", "Krisi": "blue", "John": "yellow"}
    assert favorite_color(test_dict) == "yellow"


"""Tests for count."""


def test_count_use_case_1():
    """Test count with list containing multiple duplicate strings."""
    test_list = ["apple", "apple", "banana", "apple", "cherry"]
    assert count(test_list) == {"apple": 3, "banana": 1, "cherry": 1}


def test_count_use_case_2():
    """Test count with list of unique strings."""
    test_list = ["cat", "dog", "bird"]
    assert count(test_list) == {"cat": 1, "dog": 1, "bird": 1}


def test_count_edge_case():
    """Test count with empty list."""
    test_list = []
    assert count(test_list) == {}


"""Tests for alphabetizer."""


def test_alphabetizer_use_case_1():
    """Test alphabetizer with a standard list of lowercase words."""
    test_list = ["cat", "apple", "boy", "angry", "bad", "car"]
    expected = {"c": ["cat", "car"], "a": ["apple", "angry"], "b": ["boy", "bad"]}
    assert alphabetizer(test_list) == expected


def test_alphabetizer_use_case_2():
    """Test alphabetizer handles capitalization by converting to lowercase keys."""
    test_list = ["Python", "sugar", "Turtle", "party", "taco"]
    expected = {"p": ["Python", "party"], "s": ["sugar"], "t": ["Turtle", "taco"]}
    assert alphabetizer(test_list) == expected


def test_alphabetizer_edge_case():
    """Test alphabetizer with an empty list."""
    test_list = []
    assert alphabetizer(test_list) == {}


"""Tests for update_attendance."""


def test_update_attendance_use_case_1():
    """Test by adding student to existing day."""
    attendance = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance, "Tuesday", "Vrinda")
    assert attendance == {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa", "Vrinda"],
    }


def test_update_attendance_use_case_2():
    """Test update_attendance by adding a completely new day."""
    attendance = {"Monday": ["Vrinda"]}
    update_attendance(attendance, "Wednesday", "Kaleb")
    assert attendance == {"Monday": ["Vrinda"], "Wednesday": ["Kaleb"]}


def test_update_attendance_edge_case():
    """Test update_attendance when adding a student who is already marked present (should not duplicate)."""
    attendance = {"Monday": ["Vrinda"]}
    update_attendance(attendance, "Monday", "Vrinda")
    assert attendance == {"Monday": ["Vrinda"]}
