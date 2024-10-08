number=int(input("请输入一个五位数："))
unit=number%10
myriabit=number//10000
Ten=(number//10)%10
kilobit=(number//1000)%10
if Ten==kilobit and unit==myriabit:
    print("是回文数")
else:
    print("不是回文数")