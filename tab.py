import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QTabWidget, QTableView
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
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
            tab_layout = QVBoxLayout(tab)
            tab_ui = uic.loadUi("tab_ui_file.ui")
            tab_layout.addWidget(self.create_tab_content(tab_ui))

            self.tab_widget.addTab(tab, f"Table {i+1}")

        # Set up the "OK" button manually
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_clicked)

        # Add the tab widget and the "OK" button to the layout
        self.layout.addWidget(self.tab_widget)
        self.layout.addWidget(self.ok_button)

    def create_tab_content(self, tab_ui):
        # Create a new instance of the UI loaded from the .ui file
        tab_content = QWidget()
        tab_layout = QVBoxLayout(tab_content)
        tab_layout.addWidget(tab_ui)

        # Find the table view
        table = tab_content.findChild(QTableView)

        if table is not None:
            # Fill the table with random values
            self.fill_table_random_values(table)

        return tab_content

    def fill_table_random_values(self, table):
        # Create a new model
        model = QStandardItemModel()

        # Set the model for the table
        table.setModel(model)

        # Add columns to the model
        model.setColumnCount(5)
        for col in range(5):
            model.setHeaderData(col, table.horizontalHeader().orientation(), f"Column {col+1}")

        # Add random values to the model
        for row in range(10):
            row_items = [QStandardItem(str(random.randint(1, 100))) for _ in range(5)]
            model.appendRow(row_items)

    def ok_clicked(self):
        print("OK button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())