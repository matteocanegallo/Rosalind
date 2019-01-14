def revc(s):
    s = s[::-1]
    s2= []
    for letter in s:
        if letter == 'A':
            s2.append('T')
        elif letter == 'C':
            s2.append('G')
        elif letter == 'G':
            s2.append('C')
        elif letter == 'T':
            s2.append('A')
    reverse = ''.join(s2)
    print (reverse)






