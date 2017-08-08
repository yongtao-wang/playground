# -*- coding: utf-8 -*-

# implement KMP pattern matching algorithm


def kmp(text, pattern):
    """

    :param text:
    :param pattern:
    :return:
    """
    if text is None or pattern is None:
        return -1

    # pre-process. O(len(pattern))
    i, j = -1, 0
    t = [0] * len(pattern)
    while j < len(pattern) - 1:
        if pattern[i] == pattern[j] or i == -1:
            t[j + 1] = i + 1
            i += 1
        else:
            i = 0
        j += 1
    i = j = 0

    # matching. O(len(text))
    while i < len(text) and j < len(pattern):
        if text[i] != pattern[j]:
            j = t[j]
        else:
            j += 1
        i += 1
    return i - j if j == len(pattern) else -1


if __name__ == '__main__':
    # test
    print kmp('abcdeabcabcdffabc', 'abcabcd')
