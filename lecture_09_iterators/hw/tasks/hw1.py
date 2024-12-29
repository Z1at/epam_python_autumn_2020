"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]

"""
import heapq
from pathlib import Path
from typing import Iterator, List, Union


def func_for_getting_the_file_object(path: Union[Path, str]) -> Iterator:
    """Gets the path to the file and returns the file object.

    Args:
        path: Path to file.

    Returns:
        The file object.

    """
    with open(path) as data:
        yield from data


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Merges integers in non-decreasing order from sorted files.

    Args:
        file_list: A list containing file paths.

    Returns:
        Generator.

    """
    numbers = []
    heapq.heapify(numbers)
    open_files = []

    for file_number, path in enumerate(file_list):
        open_files.append(func_for_getting_the_file_object(path))
        heapq.heappush(numbers, [int(next(open_files[-1])), file_number])

    while numbers:
        min_value, file_number = heapq.heappop(numbers)
        yield min_value

        try:
            next_num = next(open_files[file_number])
            heapq.heappush(numbers, [int(next_num), file_number])
        except StopIteration:
            pass
