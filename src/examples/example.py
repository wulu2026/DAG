from ..agent.agent import AIAgent

# 初始化AI Agent
agent = AIAgent()

# 示例1: 数据分析请求 (带可视化)
print("=" * 60)
print("示例1: 数据分析请求 (带可视化)")
print("=" * 60)

request1 = {
    'type': 'analyze_data',
    'params': {
        'query': '用户行为分析'
    }
}

result1 = agent.process_request(request1, parallel=True, visualize=True, visualize_filename="analyze_data_example")
print("\n最终结果:")
print(result1['final_result'])

# 示例2: 发送报告请求
print("\n" + "=" * 60)
print("示例2: 发送报告请求")
print("=" * 60)

request2 = {
    'type': 'send_report',
    'params': {
        'query': '产品销售分析',
        'recipient': 'manager@example.com'
    }
}

result2 = agent.process_request(request2, parallel=True)
print("\n最终结果:")
print(f"报告已发送到 {result2['final_result']['recipient']}")
print(f"发送状态: {result2['final_result']['status']}")
print(f"消息ID: {result2['final_result']['message_id']}")

# 示例3: 串行执行对比
print("\n" + "=" * 60)
print("示例3: 串行执行对比")
print("=" * 60)

request3 = {
    'type': 'send_report',
    'params': {
        'query': '市场趋势分析',
        'recipient': 'analyst@example.com'
    }
}

result3 = agent.process_request(request3, parallel=False)
print("\n最终结果:")
print(f"报告已发送到 {result3['final_result']['recipient']}")
print(f"发送状态: {result3['final_result']['status']}")