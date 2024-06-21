from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
import sys
from nodes.Nodes import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lambda2")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() 

    node_graph = NodeGraph()
    node_graph.register_node(AddNode)
    node_graph.register_node(ConstantNode)
    node_graph.widget.show()

    node = node_graph.create_node("Lambda2.AddNode")
    node = node_graph.create_node("Lambda2.ConstantNode")

    app.exec()
