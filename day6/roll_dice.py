from random import randint

def roll_dice(n = 2):
    #摇色子
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

'''
def add(a = 0, b = 0,c = 0):
    #三个数相加
    return a + b + c
'''

#参数名前加*表示args是一个可变参数
def add(*args):
    total = 0
    for i in args:
        total += i
    return total

#默认摇两个色子
print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
#print(add(c = 50,a = 100,b = 200))
print(add(1,3,5,7,9))