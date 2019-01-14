def spliced(s, t):
    elements = list(t)
    indexes = []
    j = 0
    for i, letter in enumerate(s):
        if letter == elements[j]:
            indexes.append(str(i + 1))
            if j < len(elements) - 1:
                j += 1
            else:
                break

    print (' '.join(indexes))

