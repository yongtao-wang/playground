# -*- coding: utf-8 -*-

# implement KMP pattern matching algorithm


def kmp(text, pattern):
    """
    :param text:
    :param pattern:
    :return:
    """
    if not text or not pattern:
        return 0 if text == pattern or not pattern else -1

    # pre-process. O(len(pattern))
    i, j = -1, 0
    t = [0] * len(pattern)
    t[0] = -1
    while j < len(pattern) - 1:
        if pattern[i] == pattern[j] or i == -1:
            i += 1
            j += 1
            t[j] = i
        else:
            i = t[i]
    i = j = 0

    # matching. O(len(text))
    while i < len(text) and j < len(pattern):
        # 简单来说，如果j不为-1，表示并非从头开始寻找，此时i不需要+1
        if text[i] == pattern[j] or j == -1:
            j += 1
            i += 1
        else:
            j = t[j]
    return i - j if j == len(pattern) else -1


if __name__ == '__main__':
    # test
    print kmp('mississippi', 'issi')
    print kmp('mississippi', 'issip')
    print kmp('aabaaabaaac', 'aabaaac')
