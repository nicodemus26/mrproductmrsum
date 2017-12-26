#!/usr/bin/env python3
import itertools

print("""
    There are two unknown whole numbers, m and n, both greater than 1,
    and less than 100. One mathematician, Mr. Product is given the product
    of these two numbers, while another mathematician,
    Mr. Sum is given the sum of these two numbers.

    The following conversation takes place:

    Mr. Product: I do not know the numbers.
    Mr. Sum: I knew you didn't know the numbers.
    Mr. Product: Now I know the numbers.
    Mr. Sum: Now I know the numbers, too.
""")


MIN = 2
MAX = 99

pairs = list(itertools.combinations_with_replacement(range(MIN, MAX+1), 2))
candidates = [(a, b, a*b, a+b) for a, b in pairs]

print("0: Game setup: Min: %d, Max: %d, possible pairs: %d" % (MIN, MAX, len(pairs)))
print("Ex: %s ..." % (pairs[:4]))
print(pairs[-4:])

print("""
================================================================================
1: Mr. Product: I do not know the numbers.
This indicates the product of the pair has ambiguous factorization.
Some examples:

  2 * 3 = 6
6 is ruled out because Mr. Product knows the pair without ambiguity due to
two prime factors

  99 * 99 = 9801
Mr. Product knows 9801 then there are only two possible numbers in range, even
though the factors are not prime.

  2 * 6 = 12 AND 3 * 4 = 12
Given 12, Mr. Product is unable to discern the pair because there are two possible
factorizations.

To contract the solution space we find all products with ambiguous factorizations.
""")

factorizations = [0]*(MAX**2+1)
for a, b, p, _ in candidates:
  factorizations[p] = factorizations[p] + 1
candidates = [(a, b, p, s) for a, b, p, s in candidates if factorizations[p] > 1]
print("Pairs with ambiguous factorization: %d" % (len(candidates)))
print("Ex: %s ..." % (candidates[:4]))
print(candidates[-4:])

print("""
================================================================================
2: Mr. Sum: I knew you didn't know the numbers.
This indicates that all possible sums of terms must have ambiguous factorization.
Some examples:

  3 + 4 = 7
Above 12 is establisthed as having ambiguous factorization. We can sum terms to
12 the following unique ways: 2 + 5, 3 + 4
We can rule product 12, sum 7 out because 10 may only be the product of 2, 5.

  2 + 9 = 11
2 * 9 = 18 has ambiguous factorization (3 * 6 also multiply to 18), but so do all
pairs that sum to 11: 2 + 9, 3 + 8 (24), 4 + 7 (28), 5 + 6 (30). Because of this,
Mr. Sum can know from sum 11 that all factorizations are ambiguous.
""")

def sum_knows_you_didnt(cand):
  _, _, _, s = cand
  for i in range(MIN, (s+1-MIN)):
    possible_product = i*(s-i)
    if factorizations[possible_product] <= 1:
      return False
  return True

candidates = [cand for cand in candidates if sum_knows_you_didnt(cand)]
print("Pairs with sums with terms with ambiguous factorization: %d" % (len(candidates)))
print("Ex: %s ..." % (candidates[:4]))
print(candidates[-4:])

safe_sums = set([s for a, b, p, s in candidates])
print("Safe sums: %s" % sorted(list(safe_sums)))

print("""
================================================================================
3: Mr. Product: Now I know the numbers.
Mr. Product has resolved his ambiguous factorizations by finding one and only one
pair of factors sum to a safe sum.
""")
safe_factorizations = [0]*(MAX**2+1)
unsafe_factorizations = [0]*(MAX**2+1)
for a, b, p, s in [(a, b, a*b, a+b) for a, b in pairs]:
  if s in safe_sums:
    safe_factorizations[p] = safe_factorizations[p] + 1
  else:
    unsafe_factorizations[p] = unsafe_factorizations[p] + 1
candidates = [(a, b, p, s) for a, b, p, s in candidates if safe_factorizations[p] == 1]
print("Pairs with only one safe-summing factorization: %d" % len(candidates))

print("""
================================================================================
4: Mr. Sum: Now I know the numbers, too.
Knowing the sum, Mr. Sum has exactly one candidate.
""")
cands_by_sum = {}
for a, b, p, s in candidates:
  if s in cands_by_sum:
    cands_by_sum[s].append((a, b, p, s))
  else:
    cands_by_sum[s] = [(a, b, p, s)]
print("Unambiguous candidate pairs:")
for s in cands_by_sum.keys():
  if len(cands_by_sum[s]) == 1:
    a, b, p, s = cands_by_sum[s][0]
    print("%d * %d = %d, %d + %d = %d" % (a, b, p, a, b, s))
