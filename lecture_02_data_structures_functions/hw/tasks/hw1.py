"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
from typing import Dict


def get_longest_diverse_words(file_path: str) -> List[str]:
    ...


def get_rarest_char(file_path: str) -> str:
    res = {}
    with open(file_path, "r") as f:
        for i in f.readlines():
            for j in i.split():
                for k in j:
                    if k not in res:
                        res[k] = 1
                    else:
                        res[k] += 1
    ans = [1e15, ""]
    for i in res:
        if res[i] < ans[0]:
            ans[0] = res[i]
            ans[1] = i

    return ans[1]


def count_punctuation_chars(file_path: str) -> Dict[str, int]:
    punctuation = {"!", "'", '"', ",", ".", "?", ":", ";", "-"}
    ans = dict.fromkeys(punctuation, 0)
    with open(file_path, "r") as f:
        for i in f.readlines():
            for j in i.split():
                for k in j:
                    if k in punctuation:
                        ans[k] += 1

    return ans

def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...
