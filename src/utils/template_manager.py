#!/usr/bin/env python3
"""
AI Agent 模板管理工具

这个工具允许产品经理和非技术人员管理任务模板，无需编写Python代码。
"""

import sys
import os
import argparse

# 添加项目根目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.agent.tasks import TaskLibrary

def list_templates():
    """列出所有可用模板"""
    print("\n可用模板列表:")
    print("-" * 50)
    templates = TaskLibrary.get_all_templates()
    for template in templates:
        template_info = TaskLibrary.get_template_info(template)
        print(f"✓ {template}")
        print(f"  任务数量: {len(template_info['tasks'])}")
        print(f"  包含任务: {', '.join(template_info['tasks'])}")
        print()

def show_template(template_name):
    """显示模板详情"""
    template_info = TaskLibrary.get_template_info(template_name)
    print(f"\n模板详情: {template_name}")
    print("-" * 50)
    print(f"模板名称: {template_info['name']}")
    print(f"包含任务: {', '.join(template_info['tasks'])}")
    print()
    print("任务配置:")
    for task_name, task_config in template_info['config'].items():
        print(f"\n  {task_name}:")
        for key, value in task_config.items():
            print(f"    {key}: {value}")

def load_template(file_path):
    """从JSON文件加载模板"""
    if TaskLibrary.load_template_from_file(file_path):
        print(f"\n✓ 模板加载成功!")
    else:
        print(f"\n✗ 模板加载失败!")
        sys.exit(1)

def save_template(template_name, file_path):
    """将模板保存为JSON文件"""
    if TaskLibrary.save_template_to_file(template_name, file_path):
        print(f"\n✓ 模板保存成功!")
    else:
        print(f"\n✗ 模板保存失败!")
        sys.exit(1)

def copy_template(source_name, new_name):
    """复制模板创建新模板"""
    if TaskLibrary.copy_template(source_name, new_name):
        print(f"\n✓ 模板复制成功! 新模板: {new_name}")
    else:
        print(f"\n✗ 模板复制失败! 源模板可能不存在.")
        sys.exit(1)

def delete_template(template_name):
    """删除模板"""
    if TaskLibrary.delete_template(template_name):
        print(f"\n✓ 模板 {template_name} 删除成功!")
    else:
        print(f"\n✗ 模板删除失败! 模板可能不存在或为默认模板.")
        sys.exit(1)

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='AI Agent 模板管理工具')
    
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # 列出模板命令
    subparsers.add_parser('list', help='列出所有可用模板')
    
    # 显示模板命令
    show_parser = subparsers.add_parser('show', help='显示模板详情')
    show_parser.add_argument('template_name', help='模板名称')
    
    # 加载模板命令
    load_parser = subparsers.add_parser('load', help='从JSON文件加载模板')
    load_parser.add_argument('file_path', help='JSON文件路径')
    
    # 保存模板命令
    save_parser = subparsers.add_parser('save', help='将模板保存为JSON文件')
    save_parser.add_argument('template_name', help='模板名称')
    save_parser.add_argument('file_path', help='输出文件路径')
    
    # 复制模板命令
    copy_parser = subparsers.add_parser('copy', help='复制模板创建新模板')
    copy_parser.add_argument('source_name', help='源模板名称')
    copy_parser.add_argument('new_name', help='新模板名称')
    
    # 删除模板命令
    delete_parser = subparsers.add_parser('delete', help='删除模板')
    delete_parser.add_argument('template_name', help='模板名称')
    
    # 加载默认模板目录
    template_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'templates')
    if os.path.exists(template_dir):
        TaskLibrary.load_templates_from_directory(template_dir)
    
    # 解析参数
    args = parser.parse_args()
    
    # 执行命令
    if args.command == 'list':
        list_templates()
    elif args.command == 'show':
        show_template(args.template_name)
    elif args.command == 'load':
        load_template(args.file_path)
    elif args.command == 'save':
        save_template(args.template_name, args.file_path)
    elif args.command == 'copy':
        copy_template(args.source_name, args.new_name)
    elif args.command == 'delete':
        delete_template(args.template_name)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()