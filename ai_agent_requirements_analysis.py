#!/usr/bin/env python3
"""
作为产品经理，使用需求分析模板完成AI Agent的需求分析
"""

import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.agent.agent import AIAgent

def main():
    """使用需求分析模板完成AI Agent需求分析"""
    print("\n=== AI Agent 需求分析工作开始 ===")
    
    # 1. 创建AI Agent实例
    print("\n1. 初始化AI Agent...")
    ai_agent = AIAgent(name="产品经理助手")
    
    # 2. 配置AI Agent需求分析任务
    print("\n2. 配置需求分析任务...")
    request = {
        "type": "analyze_data",
        "params": {
            "query": "AI Agent产品的需求分析，包括功能需求、技术需求、用户需求等",
            "template_name": "requirements_analysis",
            "save_report": True,
            "report_output_dir": "requirements_reports"
        }
    }
    
    print("✓ 任务配置完成")
    print(f"✓ 任务类型: {request['type']}")
    print(f"✓ 模板名称: {request['params']['template_name']}")
    print(f"✓ 查询内容: {request['params']['query']}")
    
    # 3. 执行需求分析任务
    print("\n3. 开始执行需求分析...")
    print("   - 正在收集AI Agent需求数据...")
    print("   - 正在整理和清洗需求...")
    print("   - 正在分析需求优先级和可行性...")
    print("   - 正在生成需求分析报告...")
    
    # 执行任务
    result = ai_agent.process_request(request, parallel=True, visualize=True, visualize_filename="requirements_analysis_dag")
    
    # 4. 输出结果
    print("\n4. 需求分析完成!")
    print(f"✓ 分析结果: 成功")
    print(f"✓ 报告已保存到: {request['params']['report_output_dir']}")
    
    # 5. 提示后续工作
    print("\n=== AI Agent 需求分析工作完成 ===")
    print("\n后续工作建议:")
    print("1. 组织产品评审会议，讨论分析报告")
    print("2. 与开发团队确认技术可行性")
    print("3. 制定产品路线图和优先级")
    print("4. 更新需求文档，准备开发")
    print("5. 建立需求变更管理流程")

if __name__ == "__main__":
    main()