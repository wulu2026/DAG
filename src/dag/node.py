class Node:
    """
    DAG节点类，代表一个任务
    
    Attributes:
        id (str): 节点唯一标识符
        data (any): 节点存储的数据，通常是任务函数和参数
        dependencies (list[str]): 依赖的节点ID列表
        dependents (list[str]): 依赖该节点的节点ID列表
        state (str): 节点状态 (pending, running, completed, failed)
        result (any): 节点执行结果
    """
    
    def __init__(self, id, data=None):
        """
        初始化节点
        
        Args:
            id (str): 节点唯一标识符
            data (any, optional): 节点存储的数据
        """
        self.id = id
        self.data = data
        self.dependencies = []  # 依赖的节点ID列表
        self.dependents = []    # 依赖该节点的节点ID列表
        self.state = 'pending'  # 初始状态为待处理
        self.result = None      # 初始结果为None
    
    def add_dependency(self, node_id):
        """
        添加依赖节点ID
        
        Args:
            node_id (str): 依赖的节点ID
        """
        if node_id not in self.dependencies:
            self.dependencies.append(node_id)
    
    def add_dependent(self, node_id):
        """
        添加依赖该节点的节点ID
        
        Args:
            node_id (str): 依赖该节点的节点ID
        """
        if node_id not in self.dependents:
            self.dependents.append(node_id)
    
    def remove_dependency(self, node_id):
        """
        移除依赖节点ID
        
        Args:
            node_id (str): 要移除的依赖节点ID
        """
        if node_id in self.dependencies:
            self.dependencies.remove(node_id)
    
    def remove_dependent(self, node_id):
        """
        移除依赖该节点的节点ID
        
        Args:
            node_id (str): 要移除的依赖该节点的节点ID
        """
        if node_id in self.dependents:
            self.dependents.remove(node_id)
    
    def __repr__(self):
        """
        返回节点的字符串表示
        """
        return f"Node(id={self.id}, state={self.state}, dependencies={self.dependencies})"