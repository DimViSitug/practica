import sys

from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QMainWindow,QTextEdit,QApplication, QHBoxLayout,QDialog,QPushButton, QWidget, QListView, QVBoxLayout
from database import Database
from form_archive_window import FormArchiveWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главная")
        self.resize(800,600)

        list_model = QStringListModel()

        list_widget = QWidget()
        self.list_view = QListView(list_widget)
        self.list_view.setModel(list_model)
        self.list_view.resize(800,600)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.button = QPushButton("Архив")
        self.button.clicked.connect(self.show_patients)


        buttons = QHBoxLayout()
        buttons.addWidget(self.button)
        buttons_widget = QWidget()
        buttons_widget.setLayout(buttons)

        layout = QVBoxLayout()
        layout.addWidget(buttons_widget)
        layout.addWidget(list_widget)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def show_patients(self):
        # Получение данных из базы данных и отображение их в текстовом поле
        patients = Database.fetch_patients(self)
        output = "Список пациентов:\n\n"
        for name, department, registrar in patients:
            output += f"Пациент: {name}\nНаправление: {department}\nКто направил: {registrar}\n\n"
        self.text_edit.setPlainText(output)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
        