== Markdown'd Execution Transcript ==

    There are two unknown whole numbers, m and n, both greater than 1,
    and less than 100. One mathematician, Mr. Product is given the product
    of these two numbers, while another mathematician,
    Mr. Sum is given the sum of these two numbers.

    The following conversation takes place:

    Mr. Product: I do not know the numbers.
    Mr. Sum: I knew you didn't know the numbers.
    Mr. Product: Now I know the numbers.
    Mr. Sum: Now I know the numbers, too.

0: Game setup: Min: 2, Max: 99, possible pairs: 4851
Ex: [(2, 2), (2, 3), (2, 4), (2, 5)] ...
[(97, 99), (98, 98), (98, 99), (99, 99)]

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

Pairs with ambiguous factorization: 3076
Ex: [(2, 6, 12, 8), (2, 8, 16, 10), (2, 9, 18, 11), (2, 10, 20, 12)] ...
[(84, 84, 7056, 168), (84, 88, 7392, 172), (84, 91, 7644, 175), (88, 90, 7920, 178)]

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

Pairs with sums with terms with ambiguous factorization: 145
Ex: [(2, 9, 18, 11), (2, 15, 30, 17), (2, 21, 42, 23), (2, 25, 50, 27)] ...
[(23, 30, 690, 53), (24, 29, 696, 53), (25, 28, 700, 53), (26, 27, 702, 53)]
Safe sums: [11, 17, 23, 27, 29, 35, 37, 41, 47, 53]

    3: Mr. Product: Now I know the numbers.
    Mr. Product has resolved his ambiguous factorizations by finding one and only one
    pair of factors sum to a safe sum.

Pairs with only one safe-summing factorization: 86

    4: Mr. Sum: Now I know the numbers, too.
    Knowing the sum, Mr. Sum has exactly one candidate.

Unambiguous candidate pairs:
4 * 13 = 52, 4 + 13 = 17

