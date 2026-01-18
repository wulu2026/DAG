import graphviz
from .dag import DAG

class DAGVisualizer:
    """
    DAG可视化类，用于生成DAG的可视化图
    """
    
    @staticmethod
    def visualize(dag, filename="dag", format="png", show_status=False, results=None, title=None):
        """
        可视化DAG
        
        Args:
            dag (DAG): 要可视化的DAG对象
            filename (str, optional): 输出文件名，默认"dag"
            format (str, optional): 输出格式，默认"png"
            show_status (bool, optional): 是否显示节点状态，默认False
            results (dict, optional): 节点执行结果，默认None
            title (str, optional): 图的标题，默认None
        
        Returns:
            str: 生成的文件路径
        """
        # 创建graphviz图
        g = graphviz.Digraph(name=filename, format=format, strict=True)
        
        # 设置图的样式
        g.attr(rankdir='TB', size='10,12', dpi='150', bgcolor='white', fontname='Arial', fontsize='14')
        
        # 添加标题
        if title:
            g.attr(label=title, labelloc='t', fontsize='16', fontweight='bold')
        
        # 设置节点样式
        g.attr('node', shape='box', style='rounded,filled', penwidth='2', 
               fontname='Arial', fontsize='12', margin='0.3,0.2')
        
        # 设置边样式
        g.attr('edge', fontname='Arial', fontsize='10', color='#666666', penwidth='1.5', 
               arrowsize='0.8')
        
        # 定义颜色方案
        colors = {
            'completed': '#4CAF50',      # 绿色 - 已完成
            'running': '#2196F3',        # 蓝色 - 运行中
            'failed': '#F44336',         # 红色 - 失败
            'waiting': '#FFC107',        # 黄色 - 等待中
            'default': '#E0E0E0',        # 灰色 - 默认
            'edge': '#666666',           # 灰色 - 边
            'legend_bg': '#F5F5F5'       # 浅灰色 - 图例背景
        }
        
        # 添加节点
        for node_id, node in dag.nodes.items():
            # 确定节点颜色和边框颜色
            if show_status:
                state = node.state
                if state == 'completed':
                    fill_color = colors['completed']
                    font_color = '#FFFFFF'
                elif state == 'running':
                    fill_color = colors['running']
                    font_color = '#FFFFFF'
                elif state == 'failed':
                    fill_color = colors['failed']
                    font_color = '#FFFFFF'
                elif state == 'waiting':
                    fill_color = colors['waiting']
                    font_color = '#333333'
                else:
                    fill_color = colors['default']
                    font_color = '#333333'
            else:
                fill_color = colors['default']
                font_color = '#333333'
            
            # 节点标签
            label = f"<B>{node_id}</B>"
            
            # 如果有结果，添加到标签
            if results and node_id in results:
                result = results[node_id]
                if isinstance(result, dict):
                    # 只显示字典的键
                    result_keys = list(result.keys())[:3]
                    result_str = "<BR/>" + "<BR/>\n".join(result_keys) + ("<BR/>..." if len(result) > 3 else "")
                elif isinstance(result, str):
                    # 只显示前50个字符
                    result_str = "<BR/>" + result[:50] + ("..." if len(result) > 50 else "")
                else:
                    result_str = "<BR/>" + str(result)
                label += result_str
            
            # 添加节点
            g.node(node_id, label=f"<{label}>", fillcolor=fill_color, fontcolor=font_color, 
                   tooltip=f"节点: {node_id}\n状态: {node.state}")
        
        # 添加边
        for edge in dag.edges:
            g.edge(edge.source, edge.target, color=colors['edge'])
        
        try:
            # 尝试生成图
            output_path = g.render(filename, view=False)
            print(f"DAG可视化图已生成: {output_path}")
            return output_path
        except graphviz.backend.execute.ExecutableNotFound:
            # 如果Graphviz不可用，只生成DOT文件
            dot_path = f"{filename}.dot"
            g.save(dot_path)
            
            # 生成简单的文本可视化
            text_path = f"{filename}_text.txt"
            with open(text_path, 'w', encoding='utf-8') as f:
                f.write("DAG文本可视化\n")
                f.write("=" * 50 + "\n\n")
                
                # 写入节点信息
                f.write("节点信息:\n")
                for node_id, node in dag.nodes.items():
                    state = node.state
                    f.write(f"- {node_id} (状态: {state})")
                    if results and node_id in results:
                        result = results[node_id]
                        if isinstance(result, dict):
                            result_str = "\n  结果: " + ", ".join(list(result.keys())[:3]) + ("..." if len(result) > 3 else "")
                        elif isinstance(result, str):
                            result_str = "\n  结果: " + result[:50] + ("..." if len(result) > 50 else "")
                        else:
                            result_str = "\n  结果: " + str(result)
                        f.write(result_str)
                    f.write("\n")
                
                # 写入边信息
                f.write("\n依赖关系:\n")
                for edge in dag.edges:
                    f.write(f"- {edge.source} -> {edge.target}\n")
                
                # 写入拓扑排序
                try:
                    topological_order = dag.topological_sort()
                    f.write("\n执行顺序:\n")
                    for i, node_id in enumerate(topological_order, 1):
                        f.write(f"{i}. {node_id}\n")
                except ValueError as e:
                    f.write(f"\n拓扑排序失败: {e}\n")
            
            print(f"\nGraphviz不可用，已生成以下文件:")
            print(f"1. DOT文件: {dot_path}")
            print(f"   可以使用以下命令生成图片 (需要安装Graphviz):")
            print(f"   dot -T{format} {dot_path} -o {filename}.{format}")
            print(f"2. 文本可视化: {text_path}")
            print(f"   可以直接查看此文件获取DAG的基本结构信息")
            print(f"\nGraphviz安装方法:")
            print(f"- macOS: brew install graphviz")
            print(f"- Ubuntu/Debian: sudo apt-get install graphviz")
            print(f"- Windows: 从官网下载安装包 https://graphviz.org/download/")
            
            return dot_path
    
    @staticmethod
    def visualize_with_results(dag, results, filename="dag_with_results", format="png", title=None):
        """
        可视化DAG并显示执行结果
        
        Args:
            dag (DAG): 要可视化的DAG对象
            results (dict): 节点执行结果
            filename (str, optional): 输出文件名，默认"dag_with_results"
            format (str, optional): 输出格式，默认"png"
            title (str, optional): 图的标题，默认None
        
        Returns:
            str: 生成的文件路径
        """
        return DAGVisualizer.visualize(dag, filename=filename, format=format, 
                                      show_status=True, results=results, title=title)
