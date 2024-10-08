number=int(input("请输入一个五位数："))#定义number储存整型五位数
unit=number%10#依次计算各个位的数字
myriabit=number//10000
Ten=(number//10)%10
kilobit=(number//1000)%10
if Ten==kilobit and unit==myriabit:#判断十位和千位是否相等 万位和个位是否相等 判断是否是回文数
    print("是回文数")
else:
    print("不是回文数")