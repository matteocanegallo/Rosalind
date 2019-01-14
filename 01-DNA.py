def dna(s):
    a = 0
    c = 0
    g = 0
    t = 0
    for letter in s:
        if letter == 'A':
            a += 1
        if letter == 'C':
            c += 1
        if letter == 'G':
            g += 1
        if letter == 'T':
            t += 1
    print (a, c, g, t)


