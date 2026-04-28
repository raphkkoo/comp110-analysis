"""Data related utility functions."""

__author__ = ["730748337"]

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    data_converted: dict[str, list[int | str]] = {}

    for col_name in data:
        data_converted[col_name] = []
        converted_value: int | str

        for value in data[col_name]:
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            data_converted[col_name].append(converted_value)

    return data_converted


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        first_n: list[str] = []
        limit = N
        if len(column_table[column]) < N:
            limit = len(column_table[column])

        for i in range(limit):
            first_n.append(column_table[column][i])
        result[column] = first_n
    return result


def select(
    column_table: dict[str, list[str]], names: list[str]
) -> dict[str, list[str]]:
    """Produce a table with only a specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = column_table[column]
    return result


def concat(
    table1: dict[str, list[str]], table2: dict[str, list[str]]
) -> dict[str, list[str]]:
    """Produce a new column-based table with two tables combined."""
    result: dict[str, list[str]] = {}

    for column in table1:
        result[column] = table1[column]

    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Produce a dict counting the frequencies of unique values."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
