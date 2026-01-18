class Edge:
    """
    DAG边类，代表节点之间的依赖关系
    
    Attributes:
        source (str): 源节点ID
        target (str): 目标节点ID
        data (any): 边存储的数据，通常用于描述依赖关系的属性
    """
    
    def __init__(self, source, target, data=None):
        """
        初始化边
        
        Args:
            source (str): 源节点ID
            target (str): 目标节点ID
            data (any, optional): 边存储的数据
        """
        self.source = source
        self.target = target
        self.data = data
    
    def __repr__(self):
        """
        返回边的字符串表示
        """
        return f"Edge(source={self.source}, target={self.target})"