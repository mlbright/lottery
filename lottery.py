#!/usr/bin/python

import sys
from math import factorial, ceil
from decimal import Decimal

def ncr(n,r):
    # n choose r
    n = Decimal(n)
    r = Decimal(r)
    return Decimal(factorial(n) / factorial(n - r) / factorial(r))

def hypergeometric(N,m,n,k):
    """
    N is the population size
    m is the number of success states in the population
    n is the number of draws
    k is the number of successes
    """
    if k > m:
        return 0
    if (n - k) > (N - m):
        return 0
    return Decimal(ncr(m,k) * ncr(N-m,n-k) / ncr(N,n))

def solve(M,N,T,P):
    """
    1 <= M <= 1000: the total number of people who entered the lottery.
    1 <= N <= M: the total number of winners drawn.
    1 <= T <= 100: the number of tickets each winner is allowed to buy.
    1 <= P <= M: the number of people in your group.
    """
    print M
    print N
    print T
    print P
    min_required_wins = Decimal(ceil(P/T))
    if min_required_wins > N:
        return 0
    prob = Decimal(0)
    for k in xrange(min_required_wins,N+1):
        prob += hypergeometric(M,N,N,k)
    
    print '{0:.10f}'.format(prob)
    

if __name__ == "__main__":
    solve(*map(int,sys.stdin.readline().strip().split()))
