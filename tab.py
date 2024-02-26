import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QPushButton, QHBoxLayout
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tables in Tabs Example")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tab_widget = QTabWidget()

        # Create three tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # Add tables to each tab
        self.table1 = QTableWidget()
        self.table2 = QTableWidget()
        self.table3 = QTableWidget()

        self.setup_table(self.table1, 10, 5)  # 10 rows, 5 columns
        self.setup_table(self.table2, 7, 3)   # 7 rows, 3 columns
        self.setup_table(self.table3, 12, 4)  # 12 rows, 4 columns

        self.tab_widget.addTab(self.tab1, "Table 1")
        self.tab_widget.addTab(self.tab2, "Table 2")
        self.tab_widget.addTab(self.tab3, "Table 3")

        self.layout.addWidget(self.tab_widget)

        # Add OK and Cancel buttons
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        self.layout.addLayout(button_layout)

        self.ok_button.clicked.connect(self.ok_clicked)
        self.cancel_button.clicked.connect(self.close)

    def setup_table(self, table_widget, rows, columns):
        table_widget.setRowCount(rows)
        table_widget.setColumnCount(columns)
        for i in range(rows):
            for j in range(columns):
                item = QTableWidgetItem(f"Row {i}, Col {j}, Value: {random.randint(1, 100)}")
                table_widget.setItem(i, j, item)

    def ok_clicked(self):
        print("Content of Table 1:")
        self.print_table_content(self.table1)
        print("Content of Table 2:")
        self.print_table_content(self.table2)
        print("Content of Table 3:")
        self.print_table_content(self.table3)

    def print_table_content(self, table_widget):
        for row in range(table_widget.rowCount()):
            row_data = []
            for column in range(table_widget.columnCount()):
                item = table_widget.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("None")
            print("\t".join(row_data))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    