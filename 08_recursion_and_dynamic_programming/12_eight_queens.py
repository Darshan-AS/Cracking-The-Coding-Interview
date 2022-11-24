"""
Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them
share the same row, column, or diagonal. In this case, "diagonal" means all diagonals,
not just the two that bisect the board.
"""
import pytest


def is_valid(state, row, col):
    for i in range(len(state)):
        # If same column or None, skip
        if i == col or state[i] is None:
            continue
        # If same row or in diagonal return False
        if state[i] == row or abs(row - state[i]) == abs(col - i):
            return False
    return True


def queens(n_queens):
    valid_states = []
    
    def queens_helper(n, state, col):
        # Found valid state, add to valid_states
        if col >= n_queens:
            valid_states.append(state.copy())
        
        for row in range(n_queens):
            # If row, col position is valid, place queen and recurse else backtrack
            if is_valid(state, row, col):
                state[col] = row
                queens_helper(n - 1, state, col + 1)
                state[col] = None
    
    queens_helper(n_queens, [None] * n_queens, 0)
    
    return valid_states


@pytest.mark.parametrize('n, states_count_expected', [
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (8, 92)
])
def test_queens(n, states_count_expected):
    states = queens(n)
    assert len(states) == states_count_expected
    
    def is_valid_state(state):
        for col, row in enumerate(state):
            if not is_valid(state, row, col):
                return False
        return True
    
    for state_ in states:
        assert is_valid_state(state_)
