import requests

# ---------- 第1部分：把 API 调用封装成函数 ----------
def chat_with_deepseek(user_input, api_key):
    """
    调用 DeepSeek API，返回 AI 的回复
    """
    url = "https://api.deepseek.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_input}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    return result["choices"][0]["message"]["content"]


# ---------- 第2部分：真正的对话机器人 ----------
if __name__ == "__main__":
    # 把你的 API Key 填在这里（换成你昨天注册的那个）
    MY_API_KEY = "sk-abe2314ffeeb4603af60ca9de07d531b"
    
    print("🤖 DeepSeek 对话机器人已启动！")
    print("输入 'exit' 或 'quit' 退出程序\n")
    
    while True:
        # 获取用户输入
        user_input = input("你: ")
        
        # 退出条件
        if user_input.lower() in ["exit", "quit"]:
            print("👋 再见！")
            break
        
        # 调用函数，获取 AI 回复
        reply = chat_with_deepseek(user_input, MY_API_KEY)
        print(f"AI: {reply}\n")