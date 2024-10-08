has_ticket=True
knife_length=int(input("请输入刀的长度（厘米）："))
if True :
    if knife_length<20:
        print("安检通过")
    else:
        print(f"刀的长度为{knife_length}厘米，不允许上车")
else:
    print("不允许进门")