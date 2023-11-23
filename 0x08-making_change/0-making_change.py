#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest number
 of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """ Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins, return -1
    """
    if total <= 0:
        return 0
    if coins is None or len(coins) == 0:
        return -1
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            count += 1
    if total != 0:
        return -1
    return count
