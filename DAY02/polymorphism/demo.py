def myfunction(lis):
    for i in lis:
        yield(i*i)


lis = [4,5,6,8,7]

modilist = myfunction(lis)

# print(next(modilist))
# print(next(modilist))
# print(next(modilist))
# print(next(modilist))
# print(next(modilist))
# print(next(modilist))
for i in modilist:
    print(i)