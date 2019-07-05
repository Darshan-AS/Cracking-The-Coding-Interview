"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which
can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom
(i.e., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using stacks.
"""
import pytest


def towers_of_hanoi(source, buffer, destination, n=None):
    if n is None:
        n = len(source)
    if n <= 0:
        return
    
    towers_of_hanoi(source, destination, buffer, n - 1)
    destination.append(source.pop())
    towers_of_hanoi(buffer, source, destination, n - 1)


@pytest.mark.parametrize('source, buffer, destination', [
    ([], [], []),
    ([1], [], []),
    ([2, 1], [], []),
    ([3, 2, 1], [], []),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [], [])
])
def test_towers_of_hanoi(source, buffer, destination):
    destination_expected = source.copy()
    towers_of_hanoi(source, buffer, destination)
    assert destination == destination_expected
