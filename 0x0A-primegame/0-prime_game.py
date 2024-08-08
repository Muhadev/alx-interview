#!/usr/bin/python3


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to sieve primes up to this number
    max_num = max(nums)
    # Sieve of Eratosthenes to determine primes up to max_num
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= max_num:
        if primes[p]:
            for i in range(p * p, max_num + 1, p):
                primes[i] = False
        p += 1
    # Count the number of prime removals up to each number in nums
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1]
        if primes[i]:
            prime_count[i] += 1
    # Determine the winner for each game
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
