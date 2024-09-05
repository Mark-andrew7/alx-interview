#!/usr/bin/python3
"""
Prime game algorithm
"""


def isWinner(x, nums):
    """
    Determine who the winner of the game is after x rounds
    """
    if not nums or x < 1:
        return None

    n = max(nums)
    prime = [True for _ in range(max(n + 1, 2))]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = prime[1] = False
    c = 0
    for i in range(len(prime)):
        if prime[i]:
            c += 1
        prime[i] = c

    player1 = 0
    for n in nums:
        player1 += prime[n] % 2 == 1

    if player1 * 2 == len(nums):
        return None

    if player1 * 2 == len(nums):
        return None

    if player1 * 2 > len(nums):
        return "Maria"

    return "Ben"
