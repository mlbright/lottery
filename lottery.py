#!/usr/bin/python

import sys
import math

def output(number):
    print "%.10f" % (number)
    sys.exit()

def bc(n, k):
    # binomial coefficient
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - (k - (i+1)))
        c = c // (i+1)
    return c

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
    return float(bc(m,k)) * bc(N-m,n-k) / bc(N,n)

def solve(M,N,T,P):
    """
    1 <= M <= 1000: the total number of people who entered the lottery.
    1 <= N <= M: the total number of winners drawn.
    1 <= T <= 100: the number of tickets each winner is allowed to buy.
    1 <= P <= M: the number of people in your group.
    """
    min_required_wins = int(math.ceil(float(P)/float(T)))
    if min_required_wins > N:
        output(0.0)
    prob = 0.0
    for k in xrange(min_required_wins,min(N,P)+1):
        prob += hypergeometric(M,P,N,k)
    output(prob)
    

if __name__ == "__main__":
    solve(*map(int,sys.stdin.readline().strip().split()))
