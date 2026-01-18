from ..dag.dag import DAG
from ..dag.executor import DAGExecutor
from .tasks import TaskLibrary

class AIAgent:
    """
    AI Agent核心类，负责接收用户请求，构建DAG，并执行任务
    
    Attributes:
        name (str): Agent名称
        task_library (TaskLibrary): 任务库对象
    """
    
    def __init__(self, name="DAG AI Agent"):
        """
        初始化AI Agent
        
        Args:
            name (str, optional): Agent名称，默认"DAG AI Agent"
        """
        self.name = name
        self.task_library = TaskLibrary()
    
    def process_request(self, request, parallel=True):
        """
        处理用户请求
        
        Args:
            request (dict): 用户请求，包含请求类型和参数
            parallel (bool, optional): 是否并行执行任务，默认True
        
        Returns:
            dict: 处理结果
        """
        print(f"\n{self.name} 接收到请求: {request}")
        
        # 解析请求
        request_type = request.get('type', 'analyze_data')
        params = request.get('params', {})
        
        # 根据请求类型构建DAG
        if request_type == 'analyze_data':
            dag, final_node_id = self._build_analyze_data_dag(params)
        elif request_type == 'send_report':
            dag, final_node_id = self._build_send_report_dag(params)
        else:
            raise ValueError(f"不支持的请求类型: {request_type}")
        
        # 执行DAG
        executor = DAGExecutor(dag)
        results = executor.execute(parallel=parallel)
        
        # 返回最终结果
        final_result = results.get(final_node_id)
        return {
            'request': request,
            'results': results,
            'final_result': final_result
        }
    
    def _build_analyze_data_dag(self, params):
        """
        构建数据分析请求的DAG
        
        Args:
            params (dict): 请求参数，包含query等
        
        Returns:
            tuple: (DAG对象, 最终节点ID)
        """
        query = params.get('query', '示例查询')
        
        # 创建DAG
        dag = DAG()
        
        # 添加节点
        collect_node = dag.add_node(
            'collect_data',
            data={
                'func': self.task_library.collect_data,
                'args': (query,)
            }
        )
        
        clean_node = dag.add_node(
            'clean_data',
            data={
                'func': self.task_library.clean_data,
                'args': (None,)  # 将在执行时从依赖节点获取
            }
        )
        
        analyze_node = dag.add_node(
            'analyze_data',
            data={
                'func': self.task_library.analyze_data,
                'args': (None,)  # 将在执行时从依赖节点获取
            }
        )
        
        report_node = dag.add_node(
            'generate_report',
            data={
                'func': self.task_library.generate_report,
                'args': (None,)  # 将在执行时从依赖节点获取
            }
        )
        
        # 添加边（依赖关系）
        dag.add_edge('collect_data', 'clean_data')
        dag.add_edge('clean_data', 'analyze_data')
        dag.add_edge('analyze_data', 'generate_report')
        
        return dag, 'generate_report'
    
    def _build_send_report_dag(self, params):
        """
        构建发送报告请求的DAG
        
        Args:
            params (dict): 请求参数，包含query和recipient等
        
        Returns:
            tuple: (DAG对象, 最终节点ID)
        """
        query = params.get('query', '示例查询')
        recipient = params.get('recipient', 'user@example.com')
        
        # 创建DAG
        dag = DAG()
        
        # 添加节点
        collect_node = dag.add_node(
            'collect_data',
            data={
                'func': self.task_library.collect_data,
                'args': (query,)
            }
        )
        
        clean_node = dag.add_node(
            'clean_data',
            data={
                'func': self.task_library.clean_data,
                'args': (None,)  # 将在执行时从依赖节点获取
            }
        )
        
        analyze_node = dag.add_node(
            'analyze_data',
            data={
                'func': self.task_library.analyze_data,
                'args': (None,)  # 将在执行时从依赖节点获取
            }
        )
        
        report_node = dag.add_node(
            'generate_report',
            data={
                'func': self.task_library.generate_report,
                'args': (None,)  # 将在执行时从依赖节点获取
            }
        )
        
        send_email_node = dag.add_node(
            'send_email',
            data={
                'func': self.task_library.send_email,
                'args': (None, recipient)  # 将在执行时从依赖节点获取报告
            }
        )
        
        save_db_node = dag.add_node(
            'save_to_database',
            data={
                'func': self.task_library.save_to_database,
                'args': (None, 'analysis_results')  # 将在执行时从依赖节点获取分析结果
            }
        )
        
        # 添加边（依赖关系）
        dag.add_edge('collect_data', 'clean_data')
        dag.add_edge('clean_data', 'analyze_data')
        dag.add_edge('analyze_data', 'generate_report')
        dag.add_edge('analyze_data', 'save_to_database')  # 分析结果可以并行保存到数据库
        dag.add_edge('generate_report', 'send_email')  # 报告生成后发送邮件
        
        return dag, 'send_email'