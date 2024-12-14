import os

import pytest

from lecture_04_test.hw.tasks.task_1_read_file import read_magic_number


@pytest.fixture()
def path_to_dir():
    return os.path.abspath(os.path.dirname(__file__)) + "/dir_for_test_number_1"


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (
            "/file.txt",
            True,
        ),
        (
            "/file2.txt",
            True,
        ),
    ],
)
def test_read_magic_number_positive(path_to_dir, file_name: str, expected_result: bool):
    file_path = path_to_dir + file_name
    actual_result = read_magic_number(file_path)

    assert actual_result is expected_result


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (
            "/file3.txt",
            False,
        ),
        (
            "/file4.txt",
            False,
        ),
    ],
)
def test_read_magic_number_negative(path_to_dir, file_name: str, expected_result: bool):
    file_path = path_to_dir + file_name
    actual_result = read_magic_number(file_path)

    assert actual_result is expected_result


@pytest.mark.parametrize(
    ["file_name"],
    [
        ("/file5.txt",),
        ("/file6.txt",),
        ("/file7.txt",),
    ],
)
def test_read_magic_number_exception(path_to_dir, file_name: str):
    with pytest.raises(ValueError) as info:
        file_path = path_to_dir + file_name
        read_magic_number(file_path)

    assert "A number is required." in str(info.value)
