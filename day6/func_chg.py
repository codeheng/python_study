#改进,利用模块

def fac(num):
    #求阶乘
    result = 1
    for i in range(1,num + 1):
        result *= i
    return result

m = int(input("m = "))
n = int(input("n = "))

print(fac(m) // fac(n) // fac(m - n))