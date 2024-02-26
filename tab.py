import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QWidget
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        uic.loadUi("your_ui_file.ui", self)

        # Connect button click signals to methods
        self.ok_button.clicked.connect(self.ok_clicked)
        self.cancel_button.clicked.connect(self.close)

    def ok_clicked(self):
        # Implement your OK button functionality here
        pass

    def setup_tables(self):
        # Add tables to the tabs
        for i in range(self.tab_widget.count()):
            tab = self.tab_widget.widget(i)
            table = QTableWidget()
            self.setup_table(table, 10, 5)  # Example: 10 rows, 5 columns
            layout = QVBoxLayout(tab)
            layout.addWidget(table)

    def setup_table(self, table_widget, rows, columns):
        table_widget.setRowCount(rows)
        table_widget.setColumnCount(columns)
        for i in range(rows):
            for j in range(columns):
                item = QTableWidgetItem(f"Row {i + 1}, Col {j + 1}, Value")
                table_widget.setItem(i, j, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # Call the method to set up tables
    window.setup_tables()

    window.show()
    sys.exit(app.exec_())