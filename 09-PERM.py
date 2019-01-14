from itertools import permutations


def permutation(n):

    count = 0
    number = list(permutations(range(1, n + 1)))

    for i in number:
        count += 1
    print(count)

    for i in number:
        print(' '.join(map(str, i)))