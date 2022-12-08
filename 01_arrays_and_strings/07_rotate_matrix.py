"""
Rotate Matrix: Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
"""

from typing import Any
import pytest


def rotate_matrix(image: list[list[Any]]) -> list[list[Any]]:
    """
    Time:   O(N²)
    Space:  O(1)
    where,  N = size of square image
    """
    N = len(image) - 1
    for i in range((N + 1) // 2):
        for j in range(i, N - i):
            image[j][N - i], image[N - i][N - j], image[N - j][i], image[i][j] = (
                image[i][j],
                image[j][N - i],
                image[N - i][N - j],
                image[N - j][i],
            )
    return image


# (0, 0) -> (0, 4) -> (4, 4) -> (4, 0)
# (1, 2) -> (2, 3) -> (3, 2) -> (2, 1)
# (i, j) -> (j, N - i) -> (N - i, N - j), (N - j, i)


@pytest.mark.parametrize(
    "image, rotated_image",
    [
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
        (
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30],
                [31, 32, 33, 34, 35, 36],
            ],
            [
                [31, 25, 19, 13, 7, 1],
                [32, 26, 20, 14, 8, 2],
                [33, 27, 21, 15, 9, 3],
                [34, 28, 22, 16, 10, 4],
                [35, 29, 23, 17, 11, 5],
                [36, 30, 24, 18, 12, 6],
            ],
        ),
    ],
)
def test_rotate_matrix(image: list, rotated_image: list):
    assert rotate_matrix(image) == rotated_image
