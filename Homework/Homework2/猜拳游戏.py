import random
options=["剪刀","石头","布"]# 定义游戏选项，包括 "剪刀", "石头", "布" 三种选项
user_choice=input("请输入剪刀，石头或布：")# 用户输入自己选择的选项
number_choice=random.choice(options)#随机选择一个选项作为电脑的出拳结果
print(user_choice)
print(number_choice)
if user_choice==number_choice:print("平局")#如果相同则为平局
#如果 1. 用户选择“石头”且程序选择“剪刀”
# 2. 用户选择“剪刀”且程序选择“布”
# 3. 用户选择“布”且程序选择“石头”
#这三种情况下用户赢
elif (user_choice=="石头"and number_choice=="剪刀")or (user_choice=="剪刀"and number_choice=="布")or (user_choice=="布"and number_choice=="石头"):print("你赢了")
else:print("你输了")#其他情况电脑赢