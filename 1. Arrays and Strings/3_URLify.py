"""
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""
import pytest

"""
Time:   O(N)
Space:  O(N)
where,  N = length of s
"""


def urlify(s: str, true_len: int) -> str:
    url_list = list(s)
    space_count = url_list[:true_len].count(' ')

    end_index = end = true_len + space_count * 2
    # Iterate in reverse and replace spaces with '%20' at the end
    for i in range(true_len - 1, -1, -1):
        if url_list[i] == ' ':
            url_list[end_index - 3: end_index] = '%20'
            end_index -= 3
        else:
            url_list[end_index - 1] = url_list[i]
            end_index -= 1

    return ''.join(url_list[:end])


@pytest.mark.parametrize('s, true_len, url', [
    ('Mr John Smith      ', 13, 'Mr%20John%20Smith'),
    ('I am Batman        ', 11, 'I%20am%20Batman')
])
def test_urlify(s: str, true_len: int, url: str):
    assert urlify(s, true_len) == url
