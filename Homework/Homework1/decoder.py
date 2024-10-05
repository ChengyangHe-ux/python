answer=int(input("请输入加密后的数字："))
key=int(input("请输入密钥："))
numbers=answer^key
print(numbers)
