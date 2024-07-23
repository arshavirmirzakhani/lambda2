import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from nodes.Nodes import *
from Graph import Graph


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lambda2")

        self.node_graph = Graph()
        self.node_graph.register_node(AddNode)
        self.node_graph.register_node(ConstantNode)

        self.context_menu = self.node_graph.get_context_menu("graph")
        self.nodes_menu = self.context_menu.add_menu("Nodes")
        self.nodes_menu.add_command('Add',lambda : self.node_graph.create_node("Nodes.AddNode"))

        self.NodeGraphWidget = self.node_graph.widget
        self.setCentralWidget(self.NodeGraphWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() 

    app.exec()
