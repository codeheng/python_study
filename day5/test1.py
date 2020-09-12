#找水仙花数
#该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

for i in range(100,1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    if  i == low**3 + mid**3 + high**3:
        print(i)