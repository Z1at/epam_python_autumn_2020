import os

import pytest

from lecture_09_iterators.hw.tasks.hw1 import merge_sorted_files


@pytest.fixture(scope="module")
def directory_path():
    return os.path.abspath(os.path.dirname(__file__))


def test_the_files_are_located_in_the_same_dir_and_the_func_returns_a_generator(
    directory_path,
):
    list_of_paths = [directory_path + "/file1.txt", directory_path + "/file2.txt"]

    assert next(merge_sorted_files(list_of_paths)) == 1


def test_the_files_are_located_in_the_same_dir_and_the_func_returns_all_integers(
    directory_path,
):
    list_of_paths = [
        directory_path + "/files_for_task_1/file1.txt",
        directory_path + "/files_for_task_1/file2.txt",
    ]

    assert [i for i in merge_sorted_files(list_of_paths)] == [
        i for i in range(10, 50, 10)
    ]


def test_the_files_are_located_in_different_dirs_and_the_func_returns_a_generator(
    directory_path,
):
    list_of_paths = [
        directory_path + "/file1.txt",
        directory_path + "/files_for_task_1/file1.txt",
    ]

    assert next(merge_sorted_files(list_of_paths)) == 1


def test_the_files_are_located_in_different_dirs_and_the_func_returns_all_integers(
    directory_path,
):
    list_of_paths = [
        directory_path + "/file2.txt",
        directory_path + "/files_for_task_1/file2.txt",
    ]

    assert [i for i in merge_sorted_files(list_of_paths)] == [2, 4, 6, 30, 40]


def test_duplicate_values(directory_path):
    list_of_paths = [
        directory_path + "/files_for_task_1/file2.txt",
        directory_path + "/files_for_task_1/file3.txt",
    ]

    assert [i for i in merge_sorted_files(list_of_paths)] == [1, 1, 1, 2, 3, 30, 40]


def test_duplicate_values_in_multiple_files(directory_path):
    list_of_paths = [
        directory_path + "/files_for_task_1/file3.txt",
        directory_path + "/files_for_task_1/file4.txt",
    ]

    assert [i for i in merge_sorted_files(list_of_paths)] == [
        1,
        1,
        1,
        1,
        1,
        2,
        3,
        4,
        5,
        5,
    ]
