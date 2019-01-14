def fib(month, age):
    generation = [0]*age
    generation[0], generation[1] = 0,1
    for x in range(2,month):
        temp = list(generation)
        generation[0] = sum(generation[1:])
        for i in range(1,age):
            generation[i] = temp[i-1]
    return sum(generation)


print (fib(81,19))