from sys import stdin
from math import ceil
from string import split

def binomialCoefficient(n, k): # "n choose k", multiplicative formula
  if(n-k < k): # use the symmetry-rule to minimize looping
    k = n-k
  
  coeff = 1.0
  for i in xrange(1, k+1):
    coeff *= (n-(k-i))/float(i)
  return coeff

def calc(m, n, t, p):
  if p > (n*t): # Given that the people in the group exceed the amount of winning tickets, it will be impossible
    return 0.0
  
  k = int(ceil(p/float(t)))
  if m == n or ((n + p) >= (m + k)): # Given m >= 1, m == n and n+p >= m+k always yields 1 since each individual can only win once
    return 1.0
  
  prob = 0.0
  mn = binomialCoefficient(m, n)
  for i in xrange(k, min(p, n)+1): # Calculating added probability to win k (minimum amount) up to n (maximum amount) of times within the group
    prob += (binomialCoefficient(p, i) * binomialCoefficient(m-p, n-i)) / mn
  return prob

if __name__ == "__main__":
  for line in stdin:
    input = split(line)
    print calc(int(input[0]), int(input[1]), int(input[2]), int(input[3]))
