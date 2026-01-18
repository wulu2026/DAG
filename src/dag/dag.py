from .node import Node
from .edge import Edge

class DAG:
    """
    DAG核心类，管理节点和边，提供DAG的构建和遍历功能
    
    Attributes:
        nodes (dict): 节点字典，key为节点ID，value为Node对象
        edges (list): 边列表，包含所有Edge对象
    """
    
    def __init__(self):
        """
        初始化DAG
        """
        self.nodes = {}
        self.edges = []
    
    def add_node(self, node_id, data=None):
        """
        添加节点
        
        Args:
            node_id (str): 节点ID
            data (any, optional): 节点数据
        
        Returns:
            Node: 添加的节点对象
        """
        if node_id in self.nodes:
            raise ValueError(f"节点 {node_id} 已存在")
        
        node = Node(node_id, data)
        self.nodes[node_id] = node
        return node
    
    def remove_node(self, node_id):
        """
        移除节点及其相关边
        
        Args:
            node_id (str): 要移除的节点ID
        """
        if node_id not in self.nodes:
            raise ValueError(f"节点 {node_id} 不存在")
        
        # 移除与该节点相关的所有边
        self.edges = [edge for edge in self.edges if edge.source != node_id and edge.target != node_id]
        
        # 更新其他节点的依赖关系
        for node in self.nodes.values():
            if node_id in node.dependencies:
                node.remove_dependency(node_id)
            if node_id in node.dependents:
                node.remove_dependent(node_id)
        
        # 移除节点
        del self.nodes[node_id]
    
    def add_edge(self, source_id, target_id, data=None):
        """
        添加边（依赖关系）
        
        Args:
            source_id (str): 源节点ID
            target_id (str): 目标节点ID
            data (any, optional): 边数据
        
        Returns:
            Edge: 添加的边对象
        
        Raises:
            ValueError: 如果源节点或目标节点不存在，或者添加边会导致环
        """
        if source_id not in self.nodes:
            raise ValueError(f"源节点 {source_id} 不存在")
        if target_id not in self.nodes:
            raise ValueError(f"目标节点 {target_id} 不存在")
        
        # 检查添加边是否会导致环
        if self._would_cause_cycle(source_id, target_id):
            raise ValueError(f"添加边 {source_id} -> {target_id} 会导致环")
        
        edge = Edge(source_id, target_id, data)
        self.edges.append(edge)
        
        # 更新节点的依赖关系
        self.nodes[target_id].add_dependency(source_id)
        self.nodes[source_id].add_dependent(target_id)
        
        return edge
    
    def remove_edge(self, source_id, target_id):
        """
        移除边（依赖关系）
        
        Args:
            source_id (str): 源节点ID
            target_id (str): 目标节点ID
        """
        edge_to_remove = None
        for edge in self.edges:
            if edge.source == source_id and edge.target == target_id:
                edge_to_remove = edge
                break
        
        if edge_to_remove:
            self.edges.remove(edge_to_remove)
            
            # 更新节点的依赖关系
            self.nodes[target_id].remove_dependency(source_id)
            self.nodes[source_id].remove_dependent(target_id)
    
    def _would_cause_cycle(self, source_id, target_id):
        """
        检查添加边是否会导致环
        
        Args:
            source_id (str): 源节点ID
            target_id (str): 目标节点ID
        
        Returns:
            bool: 如果会导致环则返回True，否则返回False
        """
        # 临时添加边
        temp_edges = self.edges.copy()
        temp_edges.append(Edge(source_id, target_id))
        
        # 使用DFS检查环
        visited = set()
        recursion_stack = set()
        
        def has_cycle(node_id):
            if node_id not in visited:
                visited.add(node_id)
                recursion_stack.add(node_id)
                
                # 获取所有依赖该节点的节点（即所有以该节点为源的边的目标节点）
                neighbors = [edge.target for edge in temp_edges if edge.source == node_id]
                
                for neighbor in neighbors:
                    if neighbor not in visited:
                        if has_cycle(neighbor):
                            return True
                    elif neighbor in recursion_stack:
                        return True
            
            recursion_stack.discard(node_id)
            return False
        
        # 检查所有节点
        for node_id in self.nodes:
            if has_cycle(node_id):
                return True
        
        return False
    
    def topological_sort(self):
        """
        拓扑排序，返回节点执行顺序
        
        Returns:
            list: 节点ID列表，按拓扑顺序排列
        """
        # Kahn算法实现拓扑排序
        in_degree = {node_id: 0 for node_id in self.nodes}
        
        # 计算每个节点的入度
        for edge in self.edges:
            in_degree[edge.target] += 1
        
        # 将入度为0的节点加入队列
        queue = [node_id for node_id, degree in in_degree.items() if degree == 0]
        
        topological_order = []
        
        while queue:
            current = queue.pop(0)
            topological_order.append(current)
            
            # 获取所有依赖该节点的节点（即所有以该节点为源的边的目标节点）
            neighbors = [edge.target for edge in self.edges if edge.source == current]
            
            for neighbor in neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 检查是否存在环
        if len(topological_order) != len(self.nodes):
            raise ValueError("DAG中存在环，无法进行拓扑排序")
        
        return topological_order
    
    def get_roots(self):
        """
        获取所有根节点（没有入边的节点）
        
        Returns:
            list: 根节点ID列表
        """
        return [node_id for node_id, node in self.nodes.items() if len(node.dependencies) == 0]
    
    def get_leaves(self):
        """
        获取所有叶节点（没有出边的节点）
        
        Returns:
            list: 叶节点ID列表
        """
        return [node_id for node_id, node in self.nodes.items() if len(node.dependents) == 0]
    
    def get_predecessors(self, node_id):
        """
        获取节点的所有前置节点（直接依赖）
        
        Args:
            node_id (str): 节点ID
        
        Returns:
            list: 前置节点ID列表
        """
        if node_id not in self.nodes:
            raise ValueError(f"节点 {node_id} 不存在")
        
        return self.nodes[node_id].dependencies.copy()
    
    def get_successors(self, node_id):
        """
        获取节点的所有后置节点（直接被依赖）
        
        Args:
            node_id (str): 节点ID
        
        Returns:
            list: 后置节点ID列表
        """
        if node_id not in self.nodes:
            raise ValueError(f"节点 {node_id} 不存在")
        
        return self.nodes[node_id].dependents.copy()
    
    def __repr__(self):
        """
        返回DAG的字符串表示
        """
        return f"DAG(nodes={list(self.nodes.keys())}, edges={self.edges})"