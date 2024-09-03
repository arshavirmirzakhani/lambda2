import sys
import PySide6.QtCore as QtCore
from PySide6.QtWidgets import *
from nodes.Nodes import *
from Graph import Graph


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Lambda2')

        node_graph = Graph()
        node_graph.register_node(ConstantNode)
        node_graph.register_node(LabelNode)
        node_graph.register_node(AddNode)

        graph_context_menu = node_graph.get_context_menu('graph')
        graph_nodes_menu = graph_context_menu.add_menu('Create Node')

        graph_nodes_menu.add_command('Constant',lambda : node_graph.create_node('Nodes.ConstantNode'))
        graph_nodes_menu.add_command('Label',lambda : node_graph.create_node('Nodes.LabelNode'))
        graph_nodes_menu.add_command('Add',lambda : node_graph.create_node('Nodes.AddNode'))

        
        node_context_menu = node_graph.get_context_menu('nodes')

        node_context_menu.add_command('Delete node',lambda graph,node : graph.remove_node(node),'Del',node_class=BaseNode)


        self.setCentralWidget(node_graph.widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() 

    app.exec()
