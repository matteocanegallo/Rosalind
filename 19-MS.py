def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while len(left) > 0:
        result.append(left.pop(0))

    while len(right) > 0:
        result.append(right.pop(0))

    return result


def mergesort(list):
    if len(list) == 1:
        return list

    left = list[0: len(list) // 2]
    right = list[len(list) // 2:]

    left = mergesort(left)
    right = mergesort(right)

    return  merge(left, right)

with open('/Users/matteocanegallo/PycharmProjects/Rosalind/rosalind_ms.txt','r') as file:
    content = file.read().splitlines()
lst = content[1].split(' ')
for i in range(len(lst)):
    lst[i] = int(lst[i])
sorted = mergesort(lst)
for i in range(len(sorted)):
    sorted[i] = str(sorted[i])
print(' '.join(sorted))