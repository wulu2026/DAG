# 产品经理模板使用指南

## 1. 模板简介

已为您创建了以下7个覆盖产品经理典型工作场景的模板：

- `requirements_analysis`：需求分析模板
- `user_research`：用户研究模板
- `competitor_analysis`：竞品分析模板
- `product_planning`：产品规划模板
- `data_analysis`：数据分析模板
- `customer_feedback`：客户反馈模板
- `product_launch`：产品发布模板

每个模板都包含以下5个标准任务：
- `collect_data`：数据收集
- `clean_data`：数据清洗
- `analyze_data`：数据分析
- `generate_report`：生成报告
- `send_email`：发送邮件

## 2. 如何加载和使用模板

### 2.1 查看可用模板

```bash
python -m src.utils.template_manager list
```

### 2.2 加载模板

```bash
# 加载单个模板
python -m src.utils.template_manager load templates/requirements_analysis.json

# 加载所有模板
python -m src.utils.template_manager load templates/
```

### 2.3 使用模板创建任务

```python
from src.agent.tasks import TaskLibrary

# 使用需求分析模板创建任务
task_library = TaskLibrary()
requirements_task = task_library.create_task("analyze_data", {
    "query": "分析2026年Q1的产品需求",
    "template_name": "requirements_analysis"
})

# 执行任务
requirements_task.run()
```

## 3. 模板使用示例

### 3.1 需求分析模板

**场景**：分析2026年Q2的新功能需求

**使用步骤**：

1. **复制并修改模板**：
   ```bash
   python -m src.utils.template_manager copy requirements_analysis q2_requirements
   ```

2. **导出为JSON**：
   ```bash
   python -m src.utils.template_manager save q2_requirements templates/q2_requirements.json
   ```

3. **编辑模板**：
   ```json
   {
     "name": "q2_requirements",
     "description": "2026年Q2需求分析",
     "tasks": {
       "collect_data": {
         "delay": 2.5,
         "message": "收集2026年Q2需求...",
         "sources": ["产品团队", "销售部门", "用户调研"]
       }
     }
   }
   ```

4. **使用模板**：
   ```python
   from src.agent.tasks import TaskLibrary

   task_library = TaskLibrary()
   task = task_library.create_task("generate_report", {
       "query": "2026年Q2产品功能需求",
       "template_name": "q2_requirements"
   })
   task.run()
   ```

### 3.2 用户研究模板

**场景**：了解用户对新功能的反馈

**使用示例**：

```python
from src.agent.tasks import TaskLibrary

# 使用用户研究模板创建任务
task_library = TaskLibrary()
task = task_library.create_task("analyze_data", {
    "query": "用户对新搜索功能的反馈",
    "template_name": "user_research",
    "additional_sources": ["用户访谈记录", "应用商店评论"]
})

# 执行任务
task.run()
```

### 3.3 竞品分析模板

**场景**：分析主要竞品的市场策略

**使用示例**：

```python
from src.agent.tasks import TaskLibrary

# 使用竞品分析模板创建任务
task_library = TaskLibrary()
task = task_library.create_task("generate_report", {
    "query": "主要竞品的市场策略分析",
    "template_name": "competitor_analysis",
    "competitors": ["竞品A", "竞品B", "竞品C"]
})

# 执行任务
task.run()
```

## 4. 自定义模板

### 4.1 修改现有模板

```bash
# 显示模板内容
python -m src.utils.template_manager show requirements_analysis

# 更新任务配置
python -m src.utils.template_manager update requirements_analysis collect_data '{"delay": 3.0}'

# 保存修改
python -m src.utils.template_manager save requirements_analysis templates/requirements_analysis.json
```

### 4.2 创建新模板

```json
{
  "name": "custom_template",
  "description": "自定义模板",
  "tasks": {
    "collect_data": {
      "delay": 2.0,
      "message": "收集数据...",
      "sources": ["自定义数据源"]
    },
    "generate_report": {
      "default_save_to_file": true,
      "default_output_dir": "custom_reports"
    }
  }
}
```

## 5. 最佳实践

### 5.1 模板管理

- **命名规范**：使用清晰的命名，如 `q2_2026_requirements.json`
- **版本控制**：对模板文件进行版本控制，记录修改历史
- **定期更新**：根据业务需求定期更新模板参数

### 5.2 报告生成

- **输出目录**：为不同类型的报告设置不同的输出目录
- **文件命名**：使用包含日期的命名，如 `requirements_analysis_20260415.md`
- **共享方式**：通过邮件或团队协作平台共享报告

### 5.3 效率提升

- **批量处理**：使用批量加载功能一次性加载所有模板
- **参数复用**：在不同模板中复用相似的配置参数
- **自动化**：结合调度系统定期执行模板任务

## 6. 常见问题

### Q: 如何修改模板中的任务参数？
A: 使用命令行工具或直接编辑JSON文件修改参数。

### Q: 如何创建包含新任务的模板？
A: 先修改TaskLibrary添加新任务类型，然后在模板中使用。

### Q: 模板生成的报告保存在哪里？
A: 默认保存在模板配置的输出目录中，如 `requirements_reports/`。

### Q: 如何与开发团队共享分析结果？
A: 使用 `send_email` 任务自动发送报告，或直接共享报告文件。

## 7. 联系信息

如果您有任何问题或需要进一步的帮助，请联系技术团队。
