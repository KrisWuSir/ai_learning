names = []
while True:
    name = input("你叫什么名字")
    if name == "exit":
        print("再见")
        break
    elif name == "list":
        print("目前列表里的名字有：")
        for index, value in enumerate(names, 1):
            print(f"{index},{value}")
    elif name.startswith("del"):
        name = name.replace("del ", "")
        if name in names:
            names.remove(name)
            print("以删除")
        else:
            print("列表里没有这个人")
    else:
        print("你好" + name)
        names.append(name)
