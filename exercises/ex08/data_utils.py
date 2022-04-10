"""EX08 - Analysis for Continuous Improvement."""

__author__ = "730531052"


from csv import DictReader


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
        if n > len(table[key]):
            result[key] = table[key]
        else:
            i: int = 0
            values: list[str] = []
            while i < n:
                values.append(table[key][i])
                i += 1
            result[key] = values
    
    return result


def select(table: dict[str, list[str]], column_name: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for item in column_name:
        result[item] = table[item]

    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    
    for key_1 in table_1:
        result[key_1] = table_1[key_1]
    
    for key_2 in table_2:
        if key_2 in result:
            for item in table_2[key_2]:
                if item not in result[key_2]:
                    result[key_2].append(item)
        else:
            result[key_2] = table_2[key_2]
    
    return result


def count(lst: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value in the given list and each value associated is the number of times that value appeared in the input list."""
    d: dict[str, int] = {}
    
    for item in lst:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
        
    return d


def omit(d: dict[str, int]) -> dict[str, int]: 
    """Omit the count of the empty answers in questions that are optional."""
    result: dict[str, int] = {}
    for key in d:
        if key != "":
            result[key] = d[key]
    
    return result
