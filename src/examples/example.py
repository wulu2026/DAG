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

# 示例4: 学习AI Agent架构知识 (带可视化)
print("\n" + "=" * 60)
print("示例4: 学习AI Agent架构知识 (带可视化)")
print("=" * 60)

request4 = {
    'type': 'learn_agent_architecture',
    'params': {
        'topic': '先进AI Agent架构',
        'template_name': 'default'
    }
}

result4 = agent.process_request(request4, parallel=True, visualize=True, visualize_filename="learn_agent_architecture_example")
print("\n最终结果:")
print(f"学习主题: {result4['results']['learn_agent_architecture']['topic']}")
print(f"学习的组件: {', '.join(result4['results']['learn_agent_architecture']['components'])}")
print(f"学习的架构: {result4['results']['learn_agent_architecture']['architecture']}")
print("关键概念:")
for i, concept in enumerate(result4['results']['learn_agent_architecture']['key_concepts'], 1):
    print(f"{i}. {concept}")

# 示例5: 使用自定义模板
print("\n" + "=" * 60)
print("示例5: 使用自定义模板")
print("=" * 60)

# 注册自定义模板
from src.agent.tasks import TaskLibrary
custom_template = {
    'learn_agent_architecture': {
        'delay': 1,
        'message': '快速学习 {topic}...',
        'components': ['智能感知', '自主决策', '高效执行'],
        'architectures': ['轻量级架构', '分布式架构']
    }
}
TaskLibrary.register_template('custom', custom_template)

request5 = {
    'type': 'learn_agent_architecture',
    'params': {
        'topic': '轻量级AI Agent架构',
        'template_name': 'custom'
    }
}

result5 = agent.process_request(request5, parallel=True)
print("\n最终结果:")
print(f"学习主题: {result5['results']['learn_agent_architecture']['topic']}")
print(f"学习的组件: {', '.join(result5['results']['learn_agent_architecture']['components'])}")
print(f"学习的架构: {result5['results']['learn_agent_architecture']['architecture']}")
print("关键概念:")
for i, concept in enumerate(result5['results']['learn_agent_architecture']['key_concepts'], 1):
    print(f"{i}. {concept}")

# 示例6: 保存报告到文件
print("\n" + "=" * 60)
print("示例6: 保存报告到文件")
print("=" * 60)

request6 = {
    'type': 'analyze_data',
    'params': {
        'query': '客户满意度分析'
    }
}

result6 = agent.process_request(request6, parallel=True, save_report=True, report_output_dir='custom_reports')
print("\n最终结果:")
print(f"报告生成状态: {result6['results']['generate_report']['save_status']}")
if result6['results']['generate_report']['save_status'] == 'saved':
    print(f"报告文件路径: {result6['results']['generate_report']['file_path']}")
    print(f"报告文件大小: {result6['results']['generate_report']['file_size']} 字节")

# 示例7: 学习任务并保存报告
print("\n" + "=" * 60)
print("示例7: 学习任务并保存报告")
print("=" * 60)

request7 = {
    'type': 'learn_agent_architecture',
    'params': {
        'topic': 'AI Agent架构设计模式',
        'template_name': 'default'
    }
}

result7 = agent.process_request(request7, parallel=True, save_report=True)
print("\n最终结果:")
print(f"学习主题: {result7['results']['learn_agent_architecture']['topic']}")
print(f"报告生成状态: {result7['results']['generate_report']['save_status']}")
if result7['results']['generate_report']['save_status'] == 'saved':
    print(f"报告文件路径: {result7['results']['generate_report']['file_path']}")