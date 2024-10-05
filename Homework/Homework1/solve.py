a=float(input("请输入二次项的系数a："))
b=float(input("请输入一次项的系数b："))
c=float(input("请输入常数项的系数c："))
if a==0:
    if b==0:
        if c!=0:
            print("该方程不成立")
        else:
            print(" 该方程有无穷多解")
    else:
        x=-c/b
        print(f"x={x}")
else:
    d=b**2-4*a*c
    if d<0:
        print("该方程无解")
    elif d==0:
        x=-b/(2*a)
        print(f"该方程有唯一解 x = {x}")
    else:
        x1=(-b+d**0.5)/(2*a)
        x2=(-b-d**0.5)/(2*a)
        print(f"该方程有两个不同的实数解：x1 = {x1}, x2 = {x2}")




