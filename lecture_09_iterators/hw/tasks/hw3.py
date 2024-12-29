"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import glob
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """Counts the number of lines in all files
    with received extension if there is no tokenizer.
    If the tokenizer is not none, it will count tokens.

    Args:
        dir_path: Directory path.
        file_extension: File extension.
        tokenizer: Tokenizer.

    Returns:
        The number of lines if there is no tokenizer, the number of tokens otherwise.

    """
    num_of_lines_or_tokens = 0
    if tokenizer is None:
        for path_to_file in glob.iglob(
            str(dir_path) + "/*." + file_extension, recursive=False
        ):
            with open(path_to_file) as data:
                num_of_lines_or_tokens += sum(1 for _ in data)
    else:
        for path_to_file in glob.iglob(
            str(dir_path) + "/*." + file_extension, recursive=False
        ):
            with open(path_to_file) as data:
                for line in data:
                    num_of_lines_or_tokens += sum(1 for _ in tokenizer(line))

    return num_of_lines_or_tokens
