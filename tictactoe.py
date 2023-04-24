"""
Tic Tac Toe Player
"""

import copy
from typing import List, Tuple, Set
import random

X = "X"
O = "O"
EMPTY = None


def initial_state() -> List[List[str]]:
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board: List[List[str]]) -> str:
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for cell in row:
            if cell != EMPTY:
                count += 1
    if count % 2 == 0:
        return X
    else:
        return O

    # raise NotImplementedError


def actions(board: List[List[str]]) -> Set[Tuple[int, int]]:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
    return actions

    # raise NotImplementedError


def result(board: List[List[str]], action: Tuple[int, int]) -> List[List[str]]:
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None:
        new_board = copy.deepcopy(board)
        return new_board
    if action not in actions(board):
        raise ValueError
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
    return new_board
    # raise NotImplementedError


def winner(board: List[List[str]]) -> str:
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None
    # raise NotImplementedError


def terminal(board: List[List[str]]) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if winner(board) is None and not actions(board):
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    # raise NotImplementedError


def utility(board: List[List[str]]) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board: List[List[str]]) -> Tuple[int, int]:
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    possible_actions = actions(board)
    if not possible_actions:
        return None
    # X wants to maximize the utility
    # O wants to minimize the utility

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -1
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = 1
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if player(board) == X:
        best_score = 1
        best_actions = []
        for action in actions(board):
            score = max_value(result(board, action))
            if score == best_score:
                best_actions.append(action)

        if len(best_actions) >= 1:
            print(best_actions)
            return random.choice(best_actions)
        else:
            action_list = list(actions(board))
            return random.choice(action_list)

    else:
        best_score = -1
        best_actions = []
        for action in actions(board):
            score = min_value(result(board, action))
            if score == best_score:
                best_actions.append(action)

        if len(best_actions) >= 1:
            return random.choice(best_actions)
        else:
            action_list = list(actions(board))
            return random.choice(action_list)
