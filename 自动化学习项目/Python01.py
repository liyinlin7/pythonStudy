#十进制精确计算
from decimal import Decimal
#设置精度
from decimal import getcontext

print("hello word")  #TODO  在TODO窗口可以快速找到这行代码

a = 6.99
b = 3.4
print(a * b)
#a*b=23.766000000000002
print(round(a * b, 4),)
#23.766
getcontext().prec = 10 #设置精度,所有的数字有10个
print(Decimal(a) * Decimal(b))
#23.76600000
a = "6.99"
b = "3.4"
print(Decimal(a) * Decimal(b))
#23.766
