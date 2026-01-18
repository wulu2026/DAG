# DAG-based AI Agent

一个使用有向无环图(DAG)技术实现的概念级AI Agent，用于展示DAG在任务调度和工作流管理中的应用。

## 项目概述

这个项目实现了一个简单的DAG库和基于该库的AI Agent，用于演示DAG技术的基本原理和应用场景。AI Agent可以接收用户请求，将其分解为多个子任务，并按照依赖关系形成DAG，然后有序执行这些任务。

## 核心概念

### DAG (有向无环图)
- 由节点(任务)和有向边(依赖关系)组成
- 没有循环路径，确保任务执行顺序的确定性
- 支持并行执行不相关的任务

### AI Agent
- 接收用户请求并解析
- 将请求分解为多个子任务
- 构建任务依赖关系DAG
- 执行任务并收集结果
- 返回最终结果给用户

## 目录结构

```
├── src/
│   ├── dag/
│   │   ├── node.py      # DAG节点类
│   │   ├── edge.py      # DAG边类
│   │   ├── dag.py       # DAG核心类
│   │   └── executor.py  # DAG执行器
│   ├── agent/
│   │   ├── agent.py     # AI Agent核心类
│   │   └── tasks.py     # 预定义任务集
│   └── examples/
│       └── example.py   # 使用示例
├── tests/
│   └── test_dag.py      # DAG测试用例
├── README.md
└── LICENSE
```

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行示例

```bash
python src/examples/example.py
```

## 项目目标

1. 用通俗的方式展示DAG技术的基本原理
2. 实现一个可扩展的AI Agent框架
3. 提供清晰的示例，说明如何使用DAG管理复杂任务

## 技术特点

- 简单易懂的DAG实现
- 灵活的任务调度系统
- 支持并行任务执行
- 可扩展的任务定义
- 清晰的错误处理机制