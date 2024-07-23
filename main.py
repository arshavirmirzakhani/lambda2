import sys
import PySide6.QtCore as QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from nodes.Nodes import *
from Graph import Graph


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lambda2")

        node_graph = Graph()
        node_graph.register_node(ConstantNode)
        node_graph.register_node(LabelNode)
        node_graph.register_node(AddNode)

        context_menu = node_graph.get_context_menu("graph")
        nodes_menu = context_menu.add_menu("Create Node")

        nodes_menu.add_command('Constant',lambda : node_graph.create_node("Nodes.ConstantNode"))
        nodes_menu.add_command('Label',lambda : node_graph.create_node("Nodes.LabelNode"))
        nodes_menu.add_command('Add',lambda : node_graph.create_node("Nodes.AddNode"))

        node_graph_widget = node_graph.widget
        self.setCentralWidget(node_graph_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() 

    app.exec()
