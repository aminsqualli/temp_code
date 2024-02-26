import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QTabWidget, QTableView
from PyQt5 import uic
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabs with Tables Example")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tab_widget = QTabWidget()

        # Create three tabs
        for i in range(3):
            tab = QWidget()
            tab_ui = uic.loadUi("tab_ui_file.ui")  # Load tab content from .ui file
            tab_layout = QVBoxLayout(tab)
            tab_layout.addWidget(tab_ui)

            # Fill the table with random values
            table = tab_ui.findChild(QTableView, "tableView")
            self.fill_table_random_values(table)

            self.tab_widget.addTab(tab, f"Table {i+1}")

        # Set up the "OK" button manually
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_clicked)

        # Add the tab widget and the "OK" button to the layout
        self.layout.addWidget(self.tab_widget)
        self.layout.addWidget(self.ok_button)

    def fill_table_random_values(self, table):
        # Generate random values for the table
        for row in range(table.model().rowCount()):
            for column in range(table.model().columnCount()):
                value = random.randint(1, 100)
                table.model().setData(table.model().index(row, column), value)

    def ok_clicked(self):
        print("OK button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())