import requests

# 替换成你自己的 API Key
api_key = "sk-abe2314ffeeb4603af60ca9de07d531b"

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "你好，请用一句话介绍你自己"}]
}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])