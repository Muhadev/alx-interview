#!/usr/bin/python3
"""
Main file for Module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed
    to meet a given amount total.

    :param coins: List of the values of the coins
    in your possession
    :param total: Total amount to meet
    :return: Fewest number of coins needed to meet
    total, or -1 if total cannot be met
    """
    if total <= 0:
        return 0
    # Initialize DP array with infinity, looks for min
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to meet total 0

    # Fill the DP array
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
