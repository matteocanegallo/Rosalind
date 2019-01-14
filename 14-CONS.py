def Consensus(DNA):
    profile = []
    for i in range(len(DNA[0])):
        A,C,T,G = 0, 0, 0, 0
        for j in range(len(DNA)):
            if DNA[j][i] == 'A':
                A += 1
            elif DNA[j][i] == 'C':
                C += 1
            elif DNA[j][i] == 'T':
                T += 1
            elif DNA[j][i] == 'G':
                G += 1
        profile.append([[A,'A'],[C,'C'],[G,'G'],[T,'T']])

    consensus = ''
    for row in profile:
        common = max(row)
        consensus += common[1]
    print(consensus)
    for i in range(4):
        record = profile[0][i][1] + ': '
        for j in range(len(profile)):
            record += str(profile[j][i][0]) + ' '
        print(record)



with open('rosalind_cons2.txt','r') as file:
    content = file.read()
DNA_number, lines, line_number, DNA = content.count('>'), content.splitlines(), 0, []
for i in range(DNA_number):
    DNA2 = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA2 += lines[line_number]
        line_number += 1
        if line_number+1 > len(lines):
            break
    DNA.append(DNA2)

Consensus(DNA)