year=int(input("请输入年份："))#定义year储存整型变量年份
month=int(input("请输入月份："))#定义month储存整型变量月份
months=[31,28,31,30,31,30,31,31,30,31,30,31]#定义数组储存每个月份的天数
if (year%4==0 and year%100!=0)or (year%400==0):#如果是闰年 则2月变为29天
    months[1]=29
print(f"{year}年{month}月有{months[month-1]}天")


