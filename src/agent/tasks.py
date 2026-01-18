import time
import random
import os

class TaskLibrary:
    """
    AI Agent的预定义任务库
    """
    
    # 任务模板注册表
    _task_templates = {
        'default': {
            'collect_data': {
                'delay': 1,
                'message': '收集关于 {query} 的数据...',
                'sources': ['数据库', 'API', '文件系统']
            },
            'clean_data': {
                'delay': 0.5,
                'message': '清洗数据...',
                'min_duplicates': 0,
                'max_duplicates': 50,
                'min_invalid': 0,
                'max_invalid': 20
            },
            'analyze_data': {
                'delay': 1.5,
                'message': '分析数据...',
                'min_insights': 5,
                'max_insights': 15,
                'min_accuracy': 0.8,
                'max_accuracy': 0.99
            },
            'generate_report': {
                'delay': 1.5,
                'message': '生成报告...',
                'default_save_to_file': True,
                'default_output_dir': 'reports',
                'default_file_extension': '.md'
            },
            'send_email': {
                'delay': 0.8,
                'message': '发送报告到 {recipient}...',
                'default_subject': '数据分析报告'
            },
            'save_to_database': {
                'delay': 1.2,
                'message': '保存数据到 {table_name} 表...'
            },
            'learn_agent_architecture': {
                'delay': 2,
                'message': '学习 AI Agent 架构知识...',
                'components': ['感知模块', '决策模块', '执行模块', '记忆模块', '学习模块'],
                'architectures': ['分层架构', '模块化架构', '管道架构', '混合架构']
            }
        },
        # 快速处理模板 - 适合开发和测试
        'fast': {
            'collect_data': {
                'delay': 0.2,
                'message': '[快速] 收集关于 {query} 的数据...',
                'sources': ['API']
            },
            'clean_data': {
                'delay': 0.1,
                'message': '[快速] 清洗数据...',
                'min_duplicates': 0,
                'max_duplicates': 10,
                'min_invalid': 0,
                'max_invalid': 5
            },
            'analyze_data': {
                'delay': 0.3,
                'message': '[快速] 分析数据...',
                'min_insights': 3,
                'max_insights': 5,
                'min_accuracy': 0.8,
                'max_accuracy': 0.9
            },
            'generate_report': {
                'delay': 0.3,
                'message': '[快速] 生成报告...',
                'default_save_to_file': False
            },
            'send_email': {
                'delay': 0.2,
                'message': '[快速] 发送报告到 {recipient}...',
                'default_subject': '[快速] 数据分析报告'
            },
            'save_to_database': {
                'delay': 0.2,
                'message': '[快速] 保存数据到 {table_name} 表...'
            },
            'learn_agent_architecture': {
                'delay': 0.5,
                'message': '[快速] 学习 AI Agent 架构知识...',
                'components': ['感知模块', '执行模块'],
                'architectures': ['分层架构']
            }
        },
        # 详细分析模板 - 适合正式报告
        'detailed': {
            'collect_data': {
                'delay': 2,
                'message': '[详细] 收集关于 {query} 的数据...',
                'sources': ['数据库', 'API', '文件系统', '外部数据源']
            },
            'clean_data': {
                'delay': 1,
                'message': '[详细] 清洗数据...',
                'min_duplicates': 0,
                'max_duplicates': 100,
                'min_invalid': 0,
                'max_invalid': 50
            },
            'analyze_data': {
                'delay': 3,
                'message': '[详细] 深入分析数据...',
                'min_insights': 10,
                'max_insights': 25,
                'min_accuracy': 0.9,
                'max_accuracy': 0.99
            },
            'generate_report': {
                'delay': 2,
                'message': '[详细] 生成详细报告...',
                'default_save_to_file': True,
                'default_output_dir': 'detailed_reports',
                'default_file_extension': '.md'
            },
            'send_email': {
                'delay': 1,
                'message': '[详细] 发送详细报告到 {recipient}...',
                'default_subject': '[详细] 数据分析报告'
            },
            'learn_agent_architecture': {
                'delay': 4,
                'message': '[详细] 深入学习 AI Agent 架构知识...',
                'components': ['感知模块', '决策模块', '执行模块', '记忆模块', '学习模块', '元认知模块'],
                'architectures': ['分层架构', '模块化架构', '管道架构', '混合架构', '自适应架构']
            }
        },
        # 客户报告模板 - 适合客户交付
        'client': {
            'collect_data': {
                'delay': 1.5,
                'message': '收集客户数据...',
                'sources': ['客户数据库', '客户API', '客户文件']
            },
            'clean_data': {
                'delay': 0.8,
                'message': '清洗客户数据...',
                'min_duplicates': 0,
                'max_duplicates': 30,
                'min_invalid': 0,
                'max_invalid': 10
            },
            'analyze_data': {
                'delay': 2,
                'message': '分析客户数据...',
                'min_insights': 8,
                'max_insights': 15,
                'min_accuracy': 0.95,
                'max_accuracy': 0.99
            },
            'generate_report': {
                'delay': 2,
                'message': '生成客户报告...',
                'default_save_to_file': True,
                'default_output_dir': 'client_reports',
                'default_file_extension': '.md'
            },
            'send_email': {
                'delay': 1,
                'message': '发送客户报告到 {recipient}...',
                'default_subject': '客户数据分析报告'
            }
        }
    }
    
    @classmethod
    def register_template(cls, name, template):
        """
        注册任务模板
        
        Args:
            name (str): 模板名称
            template (dict): 模板配置
        """
        cls._task_templates[name] = template
    
    @classmethod
    def get_template(cls, name='default'):
        """
        获取任务模板
        
        Args:
            name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 模板配置
        """
        return cls._task_templates.get(name, cls._task_templates['default'])
    
    @classmethod
    def get_task_config(cls, task_name, template_name='default'):
        """
        获取特定任务的配置
        
        Args:
            task_name (str): 任务名称
            template_name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 任务配置
        """
        template = cls.get_template(template_name)
        return template.get(task_name, {})
    
    @classmethod
    def get_all_templates(cls):
        """
        获取所有可用的模板名称
        
        Returns:
            list: 模板名称列表
        """
        return list(cls._task_templates.keys())
    
    @classmethod
    def get_template_info(cls, template_name='default'):
        """
        获取模板的详细信息，包括包含的任务和配置
        
        Args:
            template_name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 模板详细信息
        """
        template = cls.get_template(template_name)
        return {
            'name': template_name,
            'tasks': list(template.keys()),
            'config': template
        }
    
    @classmethod
    def copy_template(cls, source_name, new_name, description=None):
        """
        复制模板，用于创建新模板
        
        Args:
            source_name (str): 源模板名称
            new_name (str): 新模板名称
            description (str, optional): 新模板描述
        
        Returns:
            bool: 是否成功复制
        """
        if source_name not in cls._task_templates:
            return False
        
        # 深拷贝模板
        import copy
        cls._task_templates[new_name] = copy.deepcopy(cls._task_templates[source_name])
        return True
    
    @classmethod
    def update_task_config(cls, template_name, task_name, config_updates):
        """
        更新特定模板中特定任务的配置
        
        Args:
            template_name (str): 模板名称
            task_name (str): 任务名称
            config_updates (dict): 要更新的配置
        
        Returns:
            bool: 是否成功更新
        """
        if template_name not in cls._task_templates:
            return False
        
        if task_name not in cls._task_templates[template_name]:
            cls._task_templates[template_name][task_name] = {}
        
        # 更新配置
        cls._task_templates[template_name][task_name].update(config_updates)
        return True
    
    @classmethod
    def delete_template(cls, template_name):
        """
        删除模板（不能删除default模板）
        
        Args:
            template_name (str): 模板名称
        
        Returns:
            bool: 是否成功删除
        """
        if template_name == 'default' or template_name not in cls._task_templates:
            return False
        
        del cls._task_templates[template_name]
        return True

    """
    AI Agent的预定义任务库
    """
    
    @staticmethod
    def collect_data(query, template_name='default'):
        """
        收集数据的任务
        
        Args:
            query (str): 查询关键词
            template_name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 收集到的数据
        """
        # 获取模板配置
        config = TaskLibrary.get_task_config('collect_data', template_name)
        
        # 使用模板参数
        time.sleep(config.get('delay', 1))
        print(config.get('message', '收集数据...').format(query=query))
        
        # 模拟收集到的数据
        data = {
            'query': query,
            'sources': config.get('sources', ['数据库', 'API', '文件系统']),
            'data_points': random.randint(100, 1000),
            'timestamp': time.time()
        }
        
        return data
    
    @staticmethod
    def clean_data(data, template_name='default'):
        """
        清洗数据的任务
        
        Args:
            data (dict): 原始数据
            template_name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 清洗后的数据
        """
        # 获取模板配置
        config = TaskLibrary.get_task_config('clean_data', template_name)
        
        # 使用模板参数
        time.sleep(config.get('delay', 0.5))
        print(config.get('message', '清洗数据...'))
        
        # 模拟数据清洗过程
        cleaned_data = {
            **data,
            'cleaned': True,
            'duplicates_removed': random.randint(
                config.get('min_duplicates', 0),
                config.get('max_duplicates', 50)
            ),
            'invalid_entries_removed': random.randint(
                config.get('min_invalid', 0),
                config.get('max_invalid', 20)
            )
        }
        
        return cleaned_data
    
    @staticmethod
    def analyze_data(data, template_name='default'):
        """
        分析数据的任务
        
        Args:
            data (dict): 清洗后的数据
            template_name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 分析结果
        """
        # 获取模板配置
        config = TaskLibrary.get_task_config('analyze_data', template_name)
        
        # 使用模板参数
        time.sleep(config.get('delay', 1.5))
        print(config.get('message', '分析数据...'))
        
        # 生成洞察数量
        insight_count = random.randint(
            config.get('min_insights', 5),
            config.get('max_insights', 15)
        )
        
        # 模拟数据分析结果
        analysis = {
            'data_summary': {
                'total_entries': data['data_points'] - data['duplicates_removed'] - data['invalid_entries_removed'],
                'sources': data['sources'],
                'query': data['query']
            },
            'insights': [
                f"{data['query']} 的数据主要来自 {random.choice(data['sources'])}",
                f"数据质量良好，仅 {data['invalid_entries_removed']} 个无效条目",
                f"发现了 {insight_count} 个关键洞察"
            ],
            'metrics': {
                'accuracy': round(random.uniform(
                    config.get('min_accuracy', 0.8),
                    config.get('max_accuracy', 0.99)
                ), 2),
                'completeness': round(random.uniform(0.7, 0.95), 2),
                'relevance': round(random.uniform(0.85, 0.98), 2)
            }
        }
        
        return analysis
    
    @staticmethod
    def generate_report(analysis, template_name='default', save_to_file=None, output_dir=None):
        """
        生成报告的任务
        
        Args:
            analysis (dict): 分析结果或学习结果
            template_name (str, optional): 模板名称，默认'default'
            save_to_file (bool, optional): 是否保存为文件，None表示使用模板配置
            output_dir (str, optional): 输出目录，None表示使用模板配置
        
        Returns:
            dict: 包含报告内容和存储信息的字典
        """
        # 获取模板配置
        config = TaskLibrary.get_task_config('generate_report', template_name)
        
        # 使用模板中的默认值（如果未提供）
        if save_to_file is None:
            save_to_file = config.get('default_save_to_file', False)
        if output_dir is None:
            output_dir = config.get('default_output_dir', 'reports')
        
        # 使用模板参数
        time.sleep(config.get('delay', 1))
        print(config.get('message', '生成报告...'))
        
        # 检查分析结果的类型
        report_title = ""
        if 'data_summary' in analysis:
            # 数据分析结果
            query = analysis['data_summary']['query']
            total_entries = analysis['data_summary']['total_entries']
            sources = ', '.join(analysis['data_summary']['sources'])
            insights = analysis['insights']
            metrics = analysis['metrics']
            report_title = query
            
            # 生成数据分析报告
            report = f"""
# {query} 数据分析报告

## 数据摘要
- 总条目数: {total_entries}
- 数据来源: {sources}
- 查询关键词: {query}

## 关键洞察
"""
            
            for i, insight in enumerate(insights, 1):
                report += f"- 洞察 {i}: {insight}\n"
            
            report += f"""

## 质量指标
- 准确率: {metrics['accuracy']:.2f}
- 完整性: {metrics['completeness']:.2f}
- 相关性: {metrics['relevance']:.2f}

## 报告生成时间
{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}
"""
        elif 'topic' in analysis:
            # 学习结果
            topic = analysis['topic']
            components = ', '.join(analysis['components'])
            architecture = analysis['architecture']
            key_concepts = analysis['key_concepts']
            sources = ', '.join(analysis['sources'])
            knowledge_level = analysis['knowledge_level']
            report_title = topic
            
            # 生成学习报告
            report = f"""
# {topic} 学习报告

## 学习摘要
- 学习主题: {topic}
- 学习的组件: {components}
- 学习的架构: {architecture}
- 知识来源: {sources}
- 知识水平: {knowledge_level}

## 关键概念
"""
            
            for i, concept in enumerate(key_concepts, 1):
                report += f"- 概念 {i}: {concept}\n"
            
            report += f"""

## 学习时间
{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(analysis['timestamp']))}
"""
        else:
            # 默认报告格式
            report_title = "任务报告"
            report = f"""
# 任务报告

## 报告摘要
执行了一个任务，返回了以下结果:
{analysis}

## 报告生成时间
{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}
"""
        
        # 准备返回结果
        result = {
            'content': report,
            'title': report_title,
            'generated_at': time.time(),
            'save_status': 'not_saved'
        }
        
        # 如果需要保存为文件
        if save_to_file:
            try:
                # 创建输出目录
                os.makedirs(output_dir, exist_ok=True)
                
                # 生成文件名
                timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
                safe_title = ''.join(c for c in report_title if c.isalnum() or c in ' -_')
                filename = f"{safe_title}_{timestamp}.md"
                filepath = os.path.join(output_dir, filename)
                
                # 写入文件
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(report)
                
                result.update({
                    'save_status': 'saved',
                    'file_path': filepath,
                    'file_size': os.path.getsize(filepath),
                    'file_name': filename
                })
                
                print(f"报告已保存到: {filepath}")
            except Exception as e:
                result.update({
                    'save_status': 'error',
                    'error_message': str(e)
                })
                
                print(f"保存报告时出错: {e}")
        
        return result
    
    @staticmethod
    def send_email(report, recipient, template_name='default'):
        """
        发送邮件的任务
        
        Args:
            report (dict or str): 报告内容（字典格式或字符串）
            recipient (str): 收件人邮箱
            template_name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 发送结果
        """
        # 获取模板配置
        config = TaskLibrary.get_task_config('send_email', template_name)
        
        # 使用模板参数
        time.sleep(config.get('delay', 0.8))
        print(config.get('message', '发送邮件...').format(recipient=recipient))
        
        # 提取报告内容（兼容旧格式和新格式）
        report_content = report['content'] if isinstance(report, dict) else report
        
        # 模拟发送邮件
        result = {
            'recipient': recipient,
            'status': 'sent',
            'timestamp': time.time(),
            'subject': config.get('default_subject', '数据分析报告'),
            'message_id': f"msg-{random.randint(10000, 99999)}"
        }
        
        return result
    
    @staticmethod
    def save_to_database(data, table_name, template_name='default'):
        """
        保存数据到数据库的任务
        
        Args:
            data (dict): 要保存的数据
            table_name (str): 表名
            template_name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 保存结果
        """
        # 获取模板配置
        config = TaskLibrary.get_task_config('save_to_database', template_name)
        
        # 使用模板参数
        time.sleep(config.get('delay', 1.2))
        print(config.get('message', '保存数据...').format(table_name=table_name))
        
        # 模拟保存数据到数据库
        result = {
            'table_name': table_name,
            'status': 'saved',
            'timestamp': time.time(),
            'record_count': 1,
            'id': f"rec-{random.randint(10000, 99999)}"
        }
        
        return result
    
    @staticmethod
    def learn_agent_architecture(topic='AI Agent架构', template_name='default'):
        """
        学习AI Agent架构知识的任务
        
        Args:
            topic (str): 学习主题
            template_name (str, optional): 模板名称，默认'default'
        
        Returns:
            dict: 学习结果
        """
        # 获取模板配置
        config = TaskLibrary.get_task_config('learn_agent_architecture', template_name)
        
        # 使用模板参数
        time.sleep(config.get('delay', 2))
        print(config.get('message', '学习...').format(topic=topic))
        
        # 随机选择组件和架构
        components = config.get('components', ['感知模块', '决策模块', '执行模块'])
        selected_components = random.sample(components, min(3, len(components)))
        
        architectures = config.get('architectures', ['分层架构', '模块化架构'])
        selected_architecture = random.choice(architectures)
        
        # 生成学习结果
        learning_result = {
            'topic': topic,
            'components': selected_components,
            'architecture': selected_architecture,
            'key_concepts': [
                f"{selected_architecture} 是目前主流的AI Agent架构之一",
                f"{selected_components[0]} 负责处理环境输入信息",
                f"{selected_components[1]} 负责制定决策策略",
                f"{selected_components[2]} 负责执行具体操作",
                "AI Agent通过学习模块不断优化自身性能"
            ],
            'timestamp': time.time(),
            'sources': ['学术论文', '技术文档', '开源项目'],
            'knowledge_level': random.choice(['基础', '进阶', '专业'])
        }
        
        return learning_result