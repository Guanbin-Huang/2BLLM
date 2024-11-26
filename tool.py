# 配置 OpenAI API 客户端
def get_completion(prompt):
    import os
    from openai import OpenAI
    client = OpenAI(
        # 使用环境变量或直接提供 API 密钥
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    try:
        # 调用聊天模型接口
        completion = client.chat.completions.create(
            model="qwen-turbo",  # 指定模型
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

# 配置 OpenAI API 客户端
def get_completion_from_messages(messages, model="qwen-turbo", base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
                                temperature=1):
    import os
    from openai import OpenAI
    
    # 初始化客户端
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=base_url,
    )
    
    try:
        # 调用聊天模型接口
        completion = client.chat.completions.create(
            model=model,  # 指定模型
            messages=messages,  # 直接使用传入的消息列表
            temperature=temperature
        )
        
        # 返回模型的输出
        return completion.choices[0].message.content
    except Exception as e:
        # 错误处理
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
        return None