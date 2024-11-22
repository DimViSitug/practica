import sys

from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QMainWindow,QTextEdit,QMessageBox,QApplication, QHBoxLayout,QDialog,QPushButton, QWidget, QListView, QVBoxLayout
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
        self.button.clicked.connect(self.show_napravlenies)


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

    def show_napravlenies(self):
        # Получение данных из базы данных и отображение их в текстовом поле
        db = Database()
        result_raw = db.get_napravlenies()
        output = []
        for row in result_raw:
          try:

            if len(row) >= 3:  # Check if enough elements exist in the tuple  # Extract the first 3 elements.
                output.append(f"Пациент: {row["id_patients"]}\nНаправление: {row["id_wards"]}\nКто направил: {row["doctor"]}\n\n")
            else:
             print(f"Warning: Insufficient data for row: {row}")  # Add a warning

          except (KeyError, IndexError, TypeError, ValueError) as e:
              print(f"Error processing row: {row}, Error: {e}")

        form = FormArchiveWindow(self, output)
        form.show()

        

    def update_list_view_patients(self):
        self.patients_list.clear()
        try:
            db = Database() 
            patients = db.get_napravlenies()
            for patient in patients:
                self.patient_list.addItem(patient[0]) 
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка получения списка пациентов: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
        