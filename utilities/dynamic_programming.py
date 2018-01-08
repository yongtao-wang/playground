
def coins(amount):
    """
    return the number of coins needed for a certain amount
    :param amount:
    :return:
    """
    # suppose valid coins are 1, 2, 5
    memo = {1: 1, 2: 1, 5: 1}
    for i in xrange(1, amount+1):
        if i not in memo:
            checklist = [memo[i-1]+1]
            if i - 2 > 0:
                checklist.append(memo[i-2]+1)
            if i - 5 > 0:
                checklist.append(memo[i-5]+1)

            memo[i] = min(checklist)
    return memo[amount]


def coin_combo(amount):
    """
    show the actual combination of coins
    :param amount:
    :return:
    """
    # suppose valid coins are 1, 2, 5
    memo = {1: [1, 0, 0], 2: [0, 1, 0], 3: [1, 1, 0], 4: [0, 2, 0], 5: [0, 0, 1]}
    for i in xrange(1, amount+1):
        if i not in memo:
            minus_1 = sum(memo[i-1])
            minus_2 = sum(memo[i-2])
            minus_5 = sum(memo[i-5])
            check = [minus_1, minus_2, minus_5]
            if minus_1 == min(check):
                memo[i] = [memo[i-1][0]+1, memo[i-1][1], memo[i-1][2]]
            elif minus_2 == min(check):
                memo[i] = [memo[i-2][0], memo[i-2][1]+1, memo[i-2][2]]
            else:
                memo[i] = [memo[i-5][0], memo[i-5][1], memo[i-5][2]+1]
    return memo[amount]


def scalable_coins(coins, amount):
    """
    now allow user-defined valid coins (leetcode 322)
    :param target:
    :param valid_coins:
    :return:
    """
    memo = {0: 0}
    for c in coins:
        memo[c] = 1
    for i in xrange(1, amount + 1):
        if i not in memo:
            checklist = []
            for c in coins:
                if i > c and i - c in memo:
                    checklist.append(memo[i - c])
            if not checklist:
                continue
            memo[i] = min(checklist) + 1
    return memo[amount] if amount in memo else -1


if __name__ == '__main__':
    print coins(99)
    print coin_combo(99)
    print scalable_coins([1, 2, 5], 99)

