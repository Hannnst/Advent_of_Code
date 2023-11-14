from typing import Dict, List, Sequence, Tuple

import numpy as np


INPUT_FILE = "Files/day4.txt"
GRID_LEN = 5


class BingoBoard:
    """Class representing a bingo board.
    Parameters
    ----------
    grid
        An array with shape (`GRID_LEN`, `GRID_LEN`), representing the 
        number-grid on the board.
    """

    def __init__(self, grid: np.ndarray) -> None:
        if not grid.shape == (GRID_LEN, GRID_LEN):
            raise ValueError(f"BingoBoard grid must have shape {(GRID_LEN, GRID_LEN)}.")

        self.grid = grid
        self.marked = np.zeros_like(grid, dtype=bool)

    def mark_number(self, number: int) -> None:
        """Marks a number if it is on the boards."""

        self.marked = np.add(self.marked, self.grid == number)

    def has_bingo(self) -> bool:
        """Returns True if the the board has a bingo, and False if not."""

        bingo_rows = any(row.sum() == GRID_LEN for row in self.marked)
        bingo_cols = any(col.sum() == GRID_LEN for col in self.marked.transpose())

        return np.add(bingo_cols, bingo_rows)

    def get_unmarked_sum(self) -> int:
        """Returns the sum of all unmarked numbers"""

        return self.grid[self.marked == False].sum(dtype=int)


def get_numbers(filename: str) -> List[int]:
    """Returns the bingo number sequence."""

    numbers = np.loadtxt(filename, delimiter=",", max_rows=1, dtype=int)

    return numbers.tolist()


def get_boards(filename: str) -> Dict[int, BingoBoard]:
    """Returns a dictionary of IDs and BingoBoard's."""

    bingo_data = np.loadtxt(filename, skiprows=2)
    n_boards = int(len(bingo_data) / GRID_LEN)
    bingo_data = bingo_data.reshape((n_boards, 5, 5))

    boards: Dict[int, BingoBoard] = {}
    for id, bingo_grid in enumerate(bingo_data, start=1):
        boards[id] = BingoBoard(grid=bingo_grid)

    return boards


def play_bingo(
    boards: Dict[int, BingoBoard], numbers: Sequence[int]
) -> Tuple[int, int]:
    """Returns the ID and score of the board that finished first.
    Parameters
    ----------
    boards
        Dictionary of BingoBoard's and associated IDs.
    numbers
        Sequence of numbers to play bingo with.
    Returns
    -------
        ID and score of the board that gets the first bingo.
    """

    for number in numbers:
        for id, board in boards.items():
            board.mark_number(number)
            if board.has_bingo():
                score = board.get_unmarked_sum() * number

                return id, score
    else:
        raise ValueError("no boards won.")


def play_losing_bingo(
    boards: Dict[int, BingoBoard], numbers: Sequence[int]
) -> Tuple[int, int]:
    """Returns the ID and score of the board that finished last.
    Parameters
    ----------
    boards
        Dictionary of BingoBoard's and associated IDs.
    numbers
        Sequence of numbers to play bingo with.
    Returns
    -------
        ID and score of the board that gets the last bingo.
    """

    for number in numbers:
        remaining_boards = boards.copy()

        if len(remaining_boards) == 1:
            break

        for id, board in remaining_boards.items():
            board.mark_number(number)
            if board.has_bingo():
                boards.pop(id)

    return play_bingo(boards=boards, numbers=numbers)


if __name__ == "__main__":
    numbers = get_numbers(INPUT_FILE)
    boards = get_boards(INPUT_FILE)

    print("part 1:")
    winning_id, winning_score = play_bingo(boards=boards, numbers=numbers)
    print(f"Bingo for board {winning_id}! The score was: {winning_score}")

    print("part 2:")
    losing_id, losing_score = play_losing_bingo(boards=boards, numbers=numbers)
    print(f"Last board to get a Bingo was {losing_id}! The score was: {losing_score}")