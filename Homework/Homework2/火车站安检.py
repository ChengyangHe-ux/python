has_ticket = input("请问是否有车票？（是/否）：") == "是"# 定义布尔类型变量 has_ticket 表示是否有车票
if has_ticket:# 如果有车票，继续检查刀的长度
    knife_length = int(input("请输入刀的长度（厘米）："))#定义变量knife_length储存变量刀的长度
    if knife_length > 20: #如果超过 20 厘米，不允许上车
        print(f"刀的长度为 {knife_length} 厘米，不允许上车")
    else:#如果不超过 20 厘米，安检通过
        print("安检通过")
else:
    print("不允许进门")#如果没有车票，不允许进门
