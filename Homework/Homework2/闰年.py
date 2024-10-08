year=int(input("请输入年份："))#定义变量year储存整型年份
if (year%4==0 and year%100!=0)or (year%400==0):#如果year整除400或者整除4且不被100整除
    print(f"{year}是闰年")
else:print(f"{year}不是闰年")