import json
import os

os.makedirs("data", exist_ok=True)
try:  # 文件判空
    with open("data/names.json", "r", encoding="utf-8") as f:
        names = json.load(f)
except FileNotFoundError:
    names = []
while True:
    name = input("你叫什么名字")
    if name == "exit":
        print("再见")
        break
    elif name == "list":
        print("目前列表中的名字有：")
        for index, value in enumerate(names, 1):
            print(f"{index}.{value}")
    elif name == "help":
        print("可用命令：")
        print("  list       - 查看所有名字")
        print("  del 名字   - 删除指定名字")
        print("  exit       - 退出程序")
        print("  其他输入   - 添加名字")
        print("  help       - 查看帮助")
    elif name.startswith("del "):
        target = name.replace("del ", "").strip()  # 去掉首位空格
        if not target:
            print("请指定要删除的名字，例如：del 阿强")
        elif target in names:
            names.remove(target)
            print("已删除")
            with open(
                "data/names.json", "w", encoding="utf-8"
            ) as f:  # 将修改后的列表覆盖写入json文件
                json.dump(names, f, ensure_ascii=False)
        else:
            print("列表里没有这个人")
    else:
        if name in names:
            print(f"{name}已在列表中")
        else:
            print("你好" + name)
            names.append(name)
            with open("data/names.json", "w", encoding="utf-8") as f:
                json.dump(names, f, ensure_ascii=False)
