"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"


>>> tic_tac_toe_checker([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]])
'unfinished!'
>>> tic_tac_toe_checker([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]])
'x wins!'
>>> tic_tac_toe_checker([["-", "-", "o"], ["o", "o", "o"], ["x", "-", "x"]])
'o wins!'
"""
from collections import Counter
from typing import List, Union


def checker(cells_to_check: list, num_of_cells: int) -> Union[str, None]:
    """Checks whether all passed cells are equal.

    Args:
        cells_to_check: Cells that need to be checked.
        num_of_cells: Number of cells.

    Returns:
        Winner if successful, None otherwise.

    """
    cells_to_check = Counter(cells_to_check)
    if cells_to_check.get("x") and cells_to_check["x"] == num_of_cells:
        return "x wins!"
    elif cells_to_check.get("o") and cells_to_check["o"] == num_of_cells:
        return "o wins!"


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks if there are some winners.

    Args:
        board: Tic-Tac-Toe 3x3 board.

    Returns:
        Game outcome.

    """
    num_of_rows_on_board = len(board)

    for row in board:
        result = checker(row, num_of_rows_on_board)
        if result:
            return result

    there_are_empty_cells = False
    for j in range(num_of_rows_on_board):
        cells_in_the_column = []
        for i in range(num_of_rows_on_board):
            cells_in_the_column.append(board[i][j])

            if board[i][j] == "-":
                there_are_empty_cells = True

        result = checker(cells_in_the_column, num_of_rows_on_board)
        if result:
            return result

    cells_in_the_main_diagonal = [board[i][i] for i in range(num_of_rows_on_board)]
    result = checker(cells_in_the_main_diagonal, num_of_rows_on_board)
    if result:
        return result

    cells_in_the_side_diagonal = [
        board[i][num_of_rows_on_board - i - 1] for i in range(num_of_rows_on_board)
    ]
    result = checker(cells_in_the_side_diagonal, num_of_rows_on_board)
    if result:
        return result

    if there_are_empty_cells:
        return "unfinished!"

    return "draw!"
