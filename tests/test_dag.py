import unittest
from src.dag.dag import DAG
from src.dag.node import Node
from src.dag.edge import Edge

class TestDAG(unittest.TestCase):
    """
    DAG测试用例
    """
    
    def setUp(self):
        """
        测试前的准备工作
        """
        self.dag = DAG()
    
    def test_add_node(self):
        """
        测试添加节点
        """
        node = self.dag.add_node("node1", data="test data")
        self.assertIsInstance(node, Node)
        self.assertEqual(node.id, "node1")
        self.assertEqual(node.data, "test data")
        self.assertIn("node1", self.dag.nodes)
    
    def test_add_duplicate_node(self):
        """
        测试添加重复节点
        """
        self.dag.add_node("node1")
        with self.assertRaises(ValueError):
            self.dag.add_node("node1")
    
    def test_add_edge(self):
        """
        测试添加边
        """
        self.dag.add_node("node1")
        self.dag.add_node("node2")
        edge = self.dag.add_edge("node1", "node2", data="test edge")
        
        self.assertIsInstance(edge, Edge)
        self.assertEqual(edge.source, "node1")
        self.assertEqual(edge.target, "node2")
        self.assertEqual(edge.data, "test edge")
        self.assertEqual(len(self.dag.edges), 1)
        
        # 检查节点的依赖关系
        self.assertIn("node1", self.dag.nodes["node2"].dependencies)
        self.assertIn("node2", self.dag.nodes["node1"].dependents)
    
    def test_add_edge_to_nonexistent_node(self):
        """
        测试添加边到不存在的节点
        """
        self.dag.add_node("node1")
        with self.assertRaises(ValueError):
            self.dag.add_edge("node1", "node2")  # node2不存在
    
    def test_add_cyclic_edge(self):
        """
        测试添加会导致环的边
        """
        self.dag.add_node("node1")
        self.dag.add_node("node2")
        self.dag.add_edge("node1", "node2")
        
        with self.assertRaises(ValueError):
            self.dag.add_edge("node2", "node1")  # 会导致环
    
    def test_remove_node(self):
        """
        测试移除节点
        """
        self.dag.add_node("node1")
        self.dag.add_node("node2")
        self.dag.add_edge("node1", "node2")
        
        self.dag.remove_node("node1")
        
        self.assertNotIn("node1", self.dag.nodes)
        self.assertEqual(len(self.dag.edges), 0)
        self.assertEqual(len(self.dag.nodes["node2"].dependencies), 0)
    
    def test_remove_edge(self):
        """
        测试移除边
        """
        self.dag.add_node("node1")
        self.dag.add_node("node2")
        self.dag.add_edge("node1", "node2")
        
        self.dag.remove_edge("node1", "node2")
        
        self.assertEqual(len(self.dag.edges), 0)
        self.assertEqual(len(self.dag.nodes["node2"].dependencies), 0)
        self.assertEqual(len(self.dag.nodes["node1"].dependents), 0)
    
    def test_topological_sort(self):
        """
        测试拓扑排序
        """
        # 创建一个简单的DAG: 1 -> 2 -> 3
        self.dag.add_node("1")
        self.dag.add_node("2")
        self.dag.add_node("3")
        self.dag.add_edge("1", "2")
        self.dag.add_edge("2", "3")
        
        topological_order = self.dag.topological_sort()
        
        # 检查拓扑排序的正确性
        self.assertEqual(topological_order[0], "1")
        self.assertEqual(topological_order[-1], "3")
        self.assertLess(topological_order.index("2"), topological_order.index("3"))
    
    def test_get_roots(self):
        """
        测试获取根节点
        """
        self.dag.add_node("1")
        self.dag.add_node("2")
        self.dag.add_node("3")
        self.dag.add_edge("1", "3")
        self.dag.add_edge("2", "3")
        
        roots = self.dag.get_roots()
        
        self.assertEqual(len(roots), 2)
        self.assertIn("1", roots)
        self.assertIn("2", roots)
    
    def test_get_leaves(self):
        """
        测试获取叶节点
        """
        self.dag.add_node("1")
        self.dag.add_node("2")
        self.dag.add_node("3")
        self.dag.add_edge("1", "2")
        self.dag.add_edge("1", "3")
        
        leaves = self.dag.get_leaves()
        
        self.assertEqual(len(leaves), 2)
        self.assertIn("2", leaves)
        self.assertIn("3", leaves)

if __name__ == "__main__":
    unittest.main()