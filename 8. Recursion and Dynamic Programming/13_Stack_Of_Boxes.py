"""
Stack of Boxes: You have a stack of n boxes, with widths w, heights h, and depths d.
The boxes cannot be rotated and can only be stacked on top of one another
if each box in the stack is strictly larger than the box above it in width, height, and depth.
Implement a method to compute the height of the tallest possible stack.
The height of a stack is the sum of the heights of each box.
"""
import pytest


class Box:
    def __init__(self, height, width, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    def __gt__(self, other):
        return self.height > other.height and self.width > other.width and self.depth > other.depth


def stack_boxes(boxes):
    # Sort in descending order by height
    sorted_boxes = sorted(boxes, key=lambda box: box.height, reverse=True)
    memo = {}
    
    def stack_boxes_helper(index=None):
        # Get box at index if index is not None
        bottom_box, index = (None, 0) if index is None else (sorted_boxes[index], index)
        
        if index in memo:
            return memo[index]
        
        max_height = 0
        for i in range(index, len(sorted_boxes)):
            # If box at i is strictly larger than bottom box then recurse
            if bottom_box is None or bottom_box > sorted_boxes[i]:
                height = stack_boxes_helper(i)
                max_height = max(max_height, height)
        
        memo[index] = max_height + bottom_box.height if bottom_box else max_height
        return memo[index]
    
    return stack_boxes_helper()


@pytest.mark.parametrize('boxes, max_height_expected', [
    ([
         Box(100, 100, 100)
     ], 100),
    ([
         Box(100, 100, 100),
         Box(25, 25, 25)
     ], 125),
    ([
         Box(20, 5, 30),
         Box(100, 100, 100),
         Box(25, 25, 25),
         Box(17, 4, 28)
     ], 137),
    ([
         Box(30, 10, 10),
         Box(25, 50, 25),
         Box(20, 5, 30),
         Box(17, 4, 20)
     ], 42)
])
def test_stack_boxes(boxes, max_height_expected):
    assert stack_boxes(boxes) == max_height_expected
