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

# 非技术人员模板使用指南

如果您是产品经理或非技术人员，您可以使用以下方式管理和使用模板，无需编写任何Python代码。

## 1. 使用模板管理命令行工具

我们提供了一个简单的命令行工具，让您可以轻松管理模板：

```bash
# 查看所有可用命令
python -m src.utils.template_manager --help
```

### 1.1 列出所有模板

```bash
python -m src.utils.template_manager list
```

### 1.2 查看模板详情

```bash
python -m src.utils.template_manager show default
```

### 1.3 复制模板

```bash
python -m src.utils.template_manager copy client client_satisfaction
```

### 1.4 保存模板为JSON文件

```bash
python -m src.utils.template_manager save client_satisfaction templates/client_satisfaction.json
```

### 1.5 从JSON文件加载模板

```bash
python -m src.utils.template_manager load templates/client_satisfaction.json
```

### 1.6 删除模板

```bash
python -m src.utils.template_manager delete old_template
```

## 2. 编辑JSON模板文件

您可以使用任何文本编辑器（如记事本、TextEdit、VS Code等）编辑JSON模板文件。

### 2.1 JSON模板结构

```json
{
  "name": "模板名称",
  "description": "模板描述",
  "tasks": {
    "任务名称": {
      "参数1": "值1",
      "参数2": "值2"
    }
  }
}
```

### 2.2 常用任务参数

#### collect_data（收集数据）
- `delay`: 延迟时间（秒）
- `message`: 执行消息
- `sources`: 数据源列表

#### clean_data（清洗数据）
- `delay`: 延迟时间（秒）
- `message`: 执行消息
- `min_duplicates`: 最少重复数据量
- `max_duplicates`: 最多重复数据量

#### analyze_data（分析数据）
- `delay`: 延迟时间（秒）
- `message`: 执行消息
- `min_insights`: 最少洞察数量
- `max_insights`: 最多洞察数量
- `min_accuracy`: 最低准确率

#### generate_report（生成报告）
- `delay`: 延迟时间（秒）
- `message`: 执行消息
- `default_save_to_file`: 是否自动保存
- `default_output_dir`: 保存目录
- `default_file_extension`: 文件扩展名

## 3. 产品经理快速入门指南

### 场景：创建季度销售报告模板

1. **复制基础模板**
   ```bash
   python -m src.utils.template_manager copy detailed quarterly_sales_report
   ```

2. **导出为JSON文件**
   ```bash
   python -m src.utils.template_manager save quarterly_sales_report templates/quarterly_sales_report.json
   ```

3. **编辑JSON文件**
   使用文本编辑器打开 `templates/quarterly_sales_report.json`，修改配置：

   ```json
   {
     "name": "quarterly_sales_report",
     "description": "季度销售报告模板",
     "tasks": {
       "collect_data": {
         "delay": 2.0,
         "message": "收集季度销售数据...",
         "sources": ["销售数据库", "CRM系统", "ERP系统"]
       },
       "analyze_data": {
         "delay": 3.0,
         "message": "分析季度销售趋势...",
         "min_insights": 10,
         "max_insights": 20,
         "min_accuracy": 0.95
       },
       "generate_report": {
         "delay": 2.0,
         "message": "生成季度销售报告...",
         "default_save_to_file": true,
         "default_output_dir": "quarterly_reports",
         "default_file_extension": ".md"
       }
     }
   }
   ```

4. **加载修改后的模板**
   ```bash
   python -m src.utils.template_manager load templates/quarterly_sales_report.json
   ```

5. **使用模板执行任务**
   请开发人员使用以下参数调用AI Agent：
   ```json
   {
     "type": "analyze_data",
     "params": {
       "query": "2024年Q3销售分析",
       "template_name": "quarterly_sales_report"
     }
   }
   ```

## 4. 模板最佳实践（产品经理版）

### 4.1 模板命名规范
- 使用清晰的业务术语（如 `monthly_marketing_report`）
- 包含时间维度（如 `weekly_performance`）
- 区分受众（如 `internal_analysis`, `client_presentation`）

### 4.2 配置建议
- **数据收集**：根据数据源的复杂度调整延迟时间
- **数据分析**：为正式报告设置更高的洞察数量和准确率要求
- **报告生成**：开启自动保存功能，设置合理的保存目录

### 4.3 版本管理
- 定期备份模板文件
- 在文件名中包含版本号（如 `client_template_v2.json`）
- 记录模板的变更历史

### 4.4 协作建议
- 与开发人员共同确定模板的基础结构
- 定期与团队成员 review 模板配置
- 为复杂模板编写使用说明

## 5. 常见问题解答（产品经理版）

### Q: 我需要安装什么软件才能编辑JSON文件？
A: 您可以使用任何文本编辑器，如记事本（Windows）、TextEdit（Mac）或免费的VS Code编辑器。

### Q: 如何测试我的模板是否正常工作？
A: 请开发人员使用少量测试数据运行您的模板，确认输出结果符合预期。

### Q: 我可以在模板中添加新的任务吗？
A: 目前模板只能配置现有任务的参数，如果需要添加新任务，请联系开发人员。

### Q: 模板文件应该保存在哪里？
A: 建议将模板文件保存在项目的 `templates` 目录中，便于统一管理。

### Q: 如何与团队成员共享模板？
A: 您可以将JSON模板文件通过邮件、文档系统或版本控制系统（如Git）与团队共享。

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