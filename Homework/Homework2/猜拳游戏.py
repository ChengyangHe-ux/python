import random
options=["剪刀","石头","布"]
user_choice=input("请输入剪刀，石头或布：")
number_choice=random.choice(options)
print(user_choice)
print(number_choice)
if user_choice==number_choice:print("平局")
elif (user_choice=="石头"and number_choice=="剪刀")or (user_choice=="剪刀"and number_choice=="布")or (user_choice=="布"and number_choice=="石头"):print("你赢了")
else:print("你输了")