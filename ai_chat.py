import requests  #用来发送http请求
import os
import json
api_key=os.environ.get("DEEPSEEK_API_KEY")
#检查是否读取成功
if not api_key:
    print("错误，没找到环境变量 DEEPSEEK_API_KEY")
    exit()
print("api_key读取成功")
# 调用 DeepSeek API
url = "https://api.deepseek.com/chat/completions"
messages=[ {"role":"system","content":"你是一个有用的助手"}]
headers={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {api_key}"
}

while True:
    question=input("你想要问什么(输入exit退出)")
    if question=="exit":
        print("再见")
        break
    messages.append({"role":"user","content":question})
    data={
        "model":"deepseek-flash",
        "messages":messages,
        "stream":True
}
    
    response=requests.post(url,headers=headers,json=data,stream=True)

    if response.status_code!=200:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)
        continue

    print("Ai:",end="",flush=True) #打印前缀，不换行
    answer=""
    for line in response.iter_lines():
        if line:        #line不为空
            line_str=line.decode("utf-8") #将bytes字节解码成字符串
            if line_str.startswith("data: "):
                chunk=line_str[6:]
                if chunk=="[DONE]":
                    break
                chunk_data=json.loads(chunk)
                content=chunk_data["choices"][0]["delta"].get("content","")
                if content:
                    print(content,end="",flush=True)
                    answer+=content
    print() #流式输出结束后换行
    messages.append({"role":"assistant","content":answer})
    #result=response.json()
    #answer=result["choices"][0]["message"]["content"]
    #print(f"Ai:{answer}")
    #messages.append({"role":"assistant","content":answer})