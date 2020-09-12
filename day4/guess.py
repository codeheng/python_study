#计算机出一个1到100之间的随机数，玩家输入自己猜的数字，
#计算机给出对应的提示信息（大一点、小一点或猜对了），
#如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
#while的使用

import random

answer = random.randint(1,100)
counter = 0

while True:
    counter += 1
    number =int (input("please input int number: "))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print("Great!ok")
        break
print('你总共猜了%d次' % counter)
if( counter > 7):
    print(" too low ")