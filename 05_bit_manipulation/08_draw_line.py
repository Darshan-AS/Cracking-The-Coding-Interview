"""
Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
be split across rows). The height of the screen, of course, can be derived from the length of the array
and the width. Implement a function that draws a horizontal line from ( x1, y) to ( x2, y).
The method signature should look something like:
drawline(byte[] screen, int width, int x1, int x2, int y)
"""
import pytest


def draw_line(screen, width, x1, x2, y):
    start_offset, end_offset = x1 % 8, x2 % 8
    start_full_byte, end_full_byte = x1 // 8, x2 // 8
    
    if start_full_byte == end_full_byte:
        screen[(width // 8) * y + (x1 // 8)] |= ((1 << (end_offset - start_offset + 1)) - 1) << (8 - end_offset - 1)
        return screen
    
    for i in range(start_full_byte + 1, end_full_byte):
        screen[(width // 8) * y + i] = 255
    
    screen[(width // 8) * y + start_full_byte] |= ((1 << (8 - start_offset)) - 1)
    screen[(width // 8) * y + end_full_byte] |= 255 ^ ((1 << (8 - end_offset - 1)) - 1)
    return screen


@pytest.mark.parametrize('screen, width, x1, x2, y, expected', [
    ([0] * 24,
     64, 20, 42, 1,
     [0] * 8 + [0, 0, 15, 255, 255, 224, 0, 0] + [0] * 8),
    ([0] * 24,
     64, 2, 5, 0,
     [0b00111100] + [0] * 23),
    ([0] * 24,
     64, 2, 9, 0,
     [0b00111111, 0b11000000] + [0] * 22),
])
def test_draw_line(screen, width, x1, x2, y, expected):
    assert draw_line(screen, width, x1, x2, y) == expected
