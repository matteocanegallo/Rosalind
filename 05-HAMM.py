def hamming(s,t):
    distance = 0
    for i, j in enumerate(s):
        if j != t[i]:
            distance += 1
    print (distance)


