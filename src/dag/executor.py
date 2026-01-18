import threading
import time
from .dag import DAG

class DAGExecutor:
    """
    DAG执行器，负责执行DAG中的任务
    
    Attributes:
        dag (DAG): 要执行的DAG对象
        results (dict): 任务执行结果，key为节点ID，value为执行结果
        lock (threading.Lock): 线程锁，用于保护共享资源
    """
    
    def __init__(self, dag):
        """
        初始化DAG执行器
        
        Args:
            dag (DAG): 要执行的DAG对象
        """
        self.dag = dag
        self.results = {}
        self.lock = threading.Lock()
    
    def execute(self, parallel=True):
        """
        执行DAG中的所有任务
        
        Args:
            parallel (bool, optional): 是否并行执行不相关的任务，默认True
        
        Returns:
            dict: 所有任务的执行结果
        """
        # 获取拓扑排序
        topological_order = self.dag.topological_sort()
        
        if parallel:
            return self._execute_parallel(topological_order)
        else:
            return self._execute_serial(topological_order)
    
    def _execute_serial(self, topological_order):
        """
        串行执行DAG中的任务
        
        Args:
            topological_order (list): 拓扑排序后的节点ID列表
        
        Returns:
            dict: 所有任务的执行结果
        """
        print("开始串行执行DAG...")
        start_time = time.time()
        
        for node_id in topological_order:
            result = self._execute_node(node_id)
            self.results[node_id] = result
            print(f"节点 {node_id} 执行完成，结果: {result}")
        
        end_time = time.time()
        print(f"DAG执行完成，总耗时: {end_time - start_time:.2f}秒")
        
        return self.results
    
    def _execute_parallel(self, topological_order):
        """
        并行执行DAG中的任务
        
        Args:
            topological_order (list): 拓扑排序后的节点ID列表
        
        Returns:
            dict: 所有任务的执行结果
        """
        print("开始并行执行DAG...")
        start_time = time.time()
        
        # 创建线程池
        threads = []
        
        # 为每个节点创建一个线程
        for node_id in topological_order:
            # 等待依赖节点执行完成
            dependencies = self.dag.get_predecessors(node_id)
            for dep_id in dependencies:
                while dep_id not in self.results:
                    time.sleep(0.1)
            
            # 创建并启动线程
            thread = threading.Thread(target=self._execute_node_with_result, args=(node_id,))
            threads.append(thread)
            thread.start()
        
        # 等待所有线程完成
        for thread in threads:
            thread.join()
        
        end_time = time.time()
        print(f"DAG执行完成，总耗时: {end_time - start_time:.2f}秒")
        
        return self.results
    
    def _execute_node_with_result(self, node_id):
        """
        执行节点并保存结果
        
        Args:
            node_id (str): 节点ID
        """
        result = self._execute_node(node_id)
        with self.lock:
            self.results[node_id] = result
            print(f"节点 {node_id} 执行完成，结果: {result}")
    
    def _execute_node(self, node_id):
        """
        执行单个节点的任务
        
        Args:
            node_id (str): 节点ID
        
        Returns:
            any: 任务执行结果
        """
        node = self.dag.nodes[node_id]
        
        # 更新节点状态
        node.state = 'running'
        print(f"开始执行节点 {node_id}")
        
        try:
            # 获取任务函数和参数
            task_func = node.data.get('func')
            task_args = list(node.data.get('args', ()))
            task_kwargs = node.data.get('kwargs', {})
            
            # 收集依赖节点的结果
            dependencies = self.dag.get_predecessors(node_id)
            dep_results = {dep_id: self.results[dep_id] for dep_id in dependencies}
            
            # 如果有依赖节点，将其结果作为任务函数的参数
            if dependencies:
                # 获取依赖节点ID的列表
                dep_ids = list(dep_results.keys())
                
                # 如果任务函数有None参数，将其替换为依赖结果
                for i, arg in enumerate(task_args):
                    if arg is None:
                        # 按顺序替换None参数为依赖结果
                        if dep_ids:
                            task_args[i] = dep_results[dep_ids[0]]
                            dep_ids.pop(0)
                
                # 如果还有剩余的依赖结果，将其作为kwargs传递
                if dep_ids:
                    for dep_id in dep_ids:
                        task_kwargs[dep_id] = dep_results[dep_id]
            
            # 如果任务函数需要依赖结果字典，将其作为参数传递
            if 'dependencies' in task_kwargs:
                task_kwargs['dependencies'] = dep_results
            
            # 执行任务
            if task_func:
                result = task_func(*task_args, **task_kwargs)
                node.state = 'completed'
                return result
            else:
                # 如果没有任务函数，直接返回节点ID
                node.state = 'completed'
                return node_id
        
        except Exception as e:
            node.state = 'failed'
            print(f"节点 {node_id} 执行失败: {e}")
            raise