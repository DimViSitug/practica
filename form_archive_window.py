import sys

from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QApplication,QDialog,QLineEdit,QMainWindow,QHBoxLayout,QPushButton, QWidget, QListView, QVBoxLayout
from database import Database

class FormArchiveWindow(QDialog):
        def __init__(self, parent= None, object = None):
            super().__init__(parent)
            
            layout=QVBoxLayout()

            list_model = QStringListModel()
            list_model.setStringList(object)
            list_widget = QWidget()
            self.list_view = QListView(list_widget)
            self.list_view.setModel(list_model)
            widget = QWidget()
            widget.setLayout(layout)
            layout.addWidget(list_widget)

            self.setLayout(layout)

           

        def close(self):
            self.done(1) 

            

    