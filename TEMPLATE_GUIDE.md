# AI Agent 任务模板使用指南

本指南介绍了如何使用 AI Agent 系统的任务模板功能，帮助产品经理和开发人员更好地配置和管理 AI Agent 的任务执行流程。

## 什么是任务模板？

任务模板是预定义的任务配置集合，它允许您：

- 统一管理不同场景下的任务执行参数
- 快速切换任务的执行模式（如快速测试、详细分析）
- 自定义任务的行为，无需修改代码
- 为不同角色（开发、产品、运营）提供专用配置

## 现有模板介绍

系统内置了以下几种常用模板：

### 1. 默认模板 (default)
- **用途**：标准的任务执行流程
- **特点**：平衡了执行速度和结果质量
- **适用场景**：日常数据分析和报告生成

### 2. 快速处理模板 (fast)
- **用途**：快速开发和测试
- **特点**：执行速度快，输出结果简洁
- **适用场景**：开发调试、功能验证

### 3. 详细分析模板 (detailed)
- **用途**：生成详细的分析报告
- **特点**：执行时间较长，结果更全面深入
- **适用场景**：正式报告、深度分析

### 4. 客户报告模板 (client)
- **用途**：生成面向客户的报告
- **特点**：结果质量高，输出格式规范
- **适用场景**：客户交付、对外展示

## 如何使用模板？

### 1. 在代码中使用模板

```python
from src.agent.agent import AIAgent

# 创建 AI Agent 实例
agent = AIAgent()

# 使用默认模板执行数据分析任务
result = agent.process_request({
    "type": "analyze_data",
    "params": {
        "query": "客户满意度分析",
        "template_name": "default"  # 指定模板名称
    }
})

# 使用快速模板执行学习任务
result = agent.process_request({
    "type": "learn_agent_architecture",
    "params": {
        "topic": "AI Agent 架构",
        "template_name": "fast"  # 使用快速模板
    }
})

# 使用详细模板执行任务
result = agent.process_request({
    "type": "analyze_data",
    "params": {
        "query": "销售数据趋势分析",
        "template_name": "detailed"  # 使用详细分析模板
    }
})
```

### 2. 查看可用模板

```python
from src.agent.tasks import TaskLibrary

# 获取所有可用模板
all_templates = TaskLibrary.get_all_templates()
print("可用模板:", all_templates)
```

### 3. 查看模板详情

```python
# 查看默认模板的详细信息
default_template_info = TaskLibrary.get_template_info("default")
print("默认模板详情:", default_template_info)

# 查看快速模板的详细信息
fast_template_info = TaskLibrary.get_template_info("fast")
print("快速模板详情:", fast_template_info)
```

### 4. 创建自定义模板

```python
# 复制现有模板作为基础
TaskLibrary.copy_template("default", "my_custom_template")

# 更新模板中的任务配置
TaskLibrary.update_task_config(
    "my_custom_template",  # 模板名称
    "collect_data",        # 任务名称
    {
        "delay": 0.8,                   # 更新延迟时间
        "message": "自定义收集数据...",  # 更新执行消息
        "sources": ["数据库", "API"]    # 更新数据源
    }
)

# 更新报告生成任务配置
TaskLibrary.update_task_config(
    "my_custom_template",
    "generate_report",
    {
        "default_save_to_file": True,
        "default_output_dir": "my_reports",
        "default_file_extension": ".md"
    }
)
```

### 5. 删除自定义模板

```python
# 删除自定义模板（不能删除默认模板）
TaskLibrary.delete_template("my_custom_template")
```

## 模板配置详解

每个模板包含多个任务的配置，以下是常用任务的配置说明：

### 1. collect_data（收集数据）
- `delay`: 执行延迟时间（秒）
- `message`: 执行时显示的消息
- `sources`: 数据源列表

### 2. clean_data（清洗数据）
- `delay`: 执行延迟时间（秒）
- `message`: 执行时显示的消息
- `min_duplicates`: 最少重复数据量
- `max_duplicates`: 最多重复数据量
- `min_invalid`: 最少无效数据量
- `max_invalid`: 最多无效数据量

### 3. analyze_data（分析数据）
- `delay`: 执行延迟时间（秒）
- `message`: 执行时显示的消息
- `min_insights`: 最少洞察数量
- `max_insights`: 最多洞察数量
- `min_accuracy`: 最低准确率
- `max_accuracy`: 最高准确率

### 4. generate_report（生成报告）
- `delay`: 执行延迟时间（秒）
- `message`: 执行时显示的消息
- `default_save_to_file`: 是否默认保存为文件
- `default_output_dir`: 默认输出目录
- `default_file_extension`: 默认文件扩展名

### 5. send_email（发送邮件）
- `delay`: 执行延迟时间（秒）
- `message`: 执行时显示的消息
- `default_subject`: 默认邮件主题

## 模板设计最佳实践

### 1. 针对不同角色设计模板

- **开发人员**：使用 `fast` 模板进行快速测试
- **产品经理**：使用 `detailed` 模板生成详细报告
- **运营人员**：使用 `client` 模板生成客户报告

### 2. 模板命名规范

- 使用清晰、描述性的名称
- 避免使用特殊字符
- 可以包含场景信息（如 `daily_report`、`monthly_analysis`）

### 3. 配置管理建议

- 定期备份自定义模板配置
- 为模板添加文档说明其用途
- 避免在生产环境中频繁修改模板

## 示例：产品经理如何使用模板？

### 场景：设计客户满意度分析流程

1. **选择基础模板**：使用 `client` 模板作为基础
2. **复制模板**：创建名为 `client_satisfaction` 的自定义模板
3. **调整配置**：
   - 增加数据收集的延迟时间
   - 设置更多的数据源
   - 调整分析的洞察数量
   - 配置报告自动保存
4. **测试模板**：使用少量数据测试模板效果
5. **正式使用**：将模板应用到实际的客户满意度分析流程

```python
# 产品经理创建客户满意度分析专用模板
TaskLibrary.copy_template("client", "client_satisfaction")

# 调整数据收集配置
TaskLibrary.update_task_config(
    "client_satisfaction",
    "collect_data",
    {
        "delay": 2.0,
        "message": "收集客户满意度数据...",
        "sources": ["CRM系统", "客户调查", "在线评论"]
    }
)

# 调整分析配置
TaskLibrary.update_task_config(
    "client_satisfaction",
    "analyze_data",
    {
        "min_insights": 10,
        "max_insights": 20,
        "min_accuracy": 0.95
    }
)

# 配置报告保存
TaskLibrary.update_task_config(
    "client_satisfaction",
    "generate_report",
    {
        "default_save_to_file": True,
        "default_output_dir": "client_satisfaction_reports"
    }
)

# 使用自定义模板执行任务
agent = AIAgent()
result = agent.process_request({
    "type": "analyze_data",
    "params": {
        "query": "2024年Q3客户满意度分析",
        "template_name": "client_satisfaction"
    }
})
```

## 常见问题

### Q: 我可以创建多少个自定义模板？
A: 系统没有限制模板数量，但建议根据实际需要创建，避免模板过多导致管理困难。

### Q: 修改模板会影响正在执行的任务吗？
A: 不会，模板修改只影响后续执行的任务，不影响正在执行的任务。

### Q: 如何恢复默认模板？
A: 默认模板是系统内置的，无法删除或修改。如果您需要恢复默认配置，可以重新启动系统或使用 `copy_template` 方法从默认模板复制新的模板。

### Q: 模板配置保存在哪里？
A: 模板配置保存在内存中，系统重启后会恢复到默认状态。如果需要持久化保存自定义模板，建议将配置导出到文件中。

## 总结

任务模板是 AI Agent 系统中非常强大的功能，它允许您灵活地配置和管理任务执行流程。通过合理使用模板，您可以：

- 提高工作效率
- 统一任务执行标准
- 降低配置管理的复杂度
- 为不同角色提供定制化的解决方案

希望本指南能帮助您更好地使用任务模板功能！