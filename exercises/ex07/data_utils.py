"""Dictionary related utility functions."""

__author__ = "730531052"


from csv import DictReader
import re


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of a csv file into a table."""
    lines: list[dict[str, str]] = []
    file = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file)
    for row in csv_reader:
        lines.append(row)  
    file.close()
    return lines


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
          item: str = row[column]
          result.append(item)
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Translate a row oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}

    name: dict[str, str] = table[0]
    for column in name:
        result[column] = column_values(table, column)
   
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Present the first n rows of the data table."""
    result: dict[str, list[str]] = {}

    for key in table:
        values: list[str] = []
        i: int = 0
        while i < n:
            values.append(key[i])
            i += 1
        result[key] = values
    
    return result


def select(table: dict[str, list[str]], column_name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for item in column_name:
        result[item] = table[item]

    return result


def concat(table_1: dict[str, list[str]], table_2:dict[str, list[str]]) -> dict[str, list[str]]：
    result: dict[str, list[str]] = {}
    
    for key_1 in table_1:
        result[key_1] = table_1[key_1]
    
    for key_2 in table_2:
        if key_2 in result:
            result[key_2].append(table_2[key_2])
        else:
            result[key_2] = table_2[key_2]
    
    return result


def count(lst: list[str]) -> dict[str, int]:
    d: dict[str, int] = {}
    
    for item in lst:
        if item in lst:
            d[item] += 1
        else:
            d[item] == 1
        
    return d