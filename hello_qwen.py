from openai import OpenAI
import os

# 配置 OpenAI API 客户端
def get_completion(prompt):
    client = OpenAI(
        # 使用环境变量或直接提供 API 密钥
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    try:
        # 调用聊天模型接口
        completion = client.chat.completions.create(
            model="qwen-plus",  # 指定模型
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt}
            ]
        )
        # 返回模型的输出
        return completion.choices[0].message.content
    except Exception as e:
        # 错误处理
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
        return None

# 示例使用
prompt = "你是谁？中国的首都在哪里"
response = get_completion(prompt)
if response:
    print(response)
