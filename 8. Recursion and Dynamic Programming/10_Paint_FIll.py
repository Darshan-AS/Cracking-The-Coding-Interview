"""
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
"""
from enum import Enum

import pytest


class Color(Enum):
    RED = 10
    GREEN = 20
    BLUE = 30
    YELLOW = 40


def paint_fill(image, point, new_color):
    if point[0] < 0 or point[1] < 0 or len(image) <= point[0] or len(image[0]) <= point[1]:
        return
    
    new_image = image.copy()
    old_color = image[point[0]][point[1]]
    
    if old_color == new_color:
        return new_image
    
    # Use Depth First Search to fill the neighbours
    def paint_fill_helper(current_point):
        if new_image[current_point[0]][current_point[1]] != old_color:
            return
        
        new_image[current_point[0]][current_point[1]] = new_color
        
        if current_point[0] > 0:
            paint_fill_helper((current_point[0] - 1, current_point[1]))
        if current_point[0] < len(image) - 1:
            paint_fill_helper((current_point[0] + 1, current_point[1]))
        if current_point[1] > 0:
            paint_fill_helper((current_point[0], current_point[1] - 1))
        if current_point[1] < len(image[0]) - 1:
            paint_fill_helper((current_point[0], current_point[1] + 1))
    
    paint_fill_helper(point)
    return new_image


@pytest.mark.parametrize('image, point, new_color, paint_filled_image', [
    ([[Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.YELLOW],
      [Color.BLUE, Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.YELLOW, Color.YELLOW, Color.YELLOW],
      [Color.RED, Color.RED, Color.GREEN, Color.GREEN, Color.RED, Color.RED, Color.RED, Color.RED],
      [Color.RED, Color.RED, Color.BLUE, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.RED],
      [Color.YELLOW, Color.YELLOW, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED, Color.RED]],
     (1, 3),
     Color.BLUE,
     [[Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.YELLOW],
      [Color.BLUE, Color.GREEN, Color.GREEN, Color.BLUE, Color.BLUE, Color.YELLOW, Color.YELLOW, Color.YELLOW],
      [Color.RED, Color.RED, Color.GREEN, Color.GREEN, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
      [Color.RED, Color.RED, Color.BLUE, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.BLUE],
      [Color.YELLOW, Color.YELLOW, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]]
     )
])
def test_paint_fill(image, point, new_color, paint_filled_image):
    assert paint_fill(image, point, new_color) == paint_filled_image
