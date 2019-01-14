def find_ssm(DNA1, DNA2):
    lst = []
    for _ in range(len(DNA1)+1):
        lst2 = []
        lst.append(lst2)
        for _ in range(len(DNA2)+1):
            lst2.append(0)
    for i in range(1, len(DNA1)+1):
        for j in range(1, len(DNA2)+1):
            if DNA1[i-1] == DNA2[j-1]:
                lst[i][j] = lst[i-1][j-1]+1
            else:
                lst[i][j] = max(lst[i-1][j], lst[i][j-1])

    m, n, x = len(DNA1), len(DNA2), ''
    while lst[m][n] != 0:

        if lst[m][n] == lst[m-1][n]:
            m -= 1
        elif lst[m][n] == lst[m][n-1]:
            n -= 1
        else:
            x += DNA1[m-1]
            m -= 1
            n -= 1
    x = list(x)
    x.reverse()
    x = ''.join(x)
    return x


with open('/Users/matteocanegallo/PycharmProjects/Rosalind/rosalind_lcsq.txt', 'r') as file:
    content = file.read()
DNAs_number, lines, line_number, DNAs = content.count('>'), content.splitlines(), 0, []
for i in range(DNAs_number):
    DNA = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA += lines[line_number]
        line_number += 1
        if line_number+1 > len(lines):
            break
    DNAs.append(DNA)
print(find_ssm(DNAs[0], DNAs[1]))