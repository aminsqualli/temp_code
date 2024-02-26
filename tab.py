import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QPushButton


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

        self.setup_table(self.table1, [[f"Table 1 Row {i}, Col {j}" for j in range(5)] for i in range(10)])
        self.setup_table(self.table2, [[f"Table 2 Row {i}, Col {j}" for j in range(3)] for i in range(7)])
        self.setup_table(self.table3, [[f"Table 3 Row {i}, Col {j}" for j in range(4)] for i in range(12)])

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
        self.cancel_button.clicked.connect(self.cancel_clicked)

    def setup_table(self, table_widget, data):
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data[0]))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                table_widget.setItem(i, j, QTableWidgetItem(item))

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