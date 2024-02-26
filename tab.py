import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QPushButton, QHBoxLayout
import random
import pandas as pd


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

        # Add tables to tabs
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(self.table1)
        self.tab1.setLayout(tab1_layout)

        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(self.table2)
        self.tab2.setLayout(tab2_layout)

        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(self.table3)
        self.tab3.setLayout(tab3_layout)

        # Add tabs to tab widget
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

        # Set headers
        for col in range(columns):
            table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(f"Column {col + 1}"))

        for i in range(rows):
            for j in range(columns):
                item = QTableWidgetItem(f"Row {i + 1}, Col {j + 1}, Value: {random.randint(1, 100)}")
                table_widget.setItem(i, j, item)

    def ok_clicked(self):
        dataframes = []
        for table_widget in [self.table1, self.table2, self.table3]:
            data = []
            headers = []
            for column in range(table_widget.columnCount()):
                headers.append(table_widget.horizontalHeaderItem(column).text())
            for row in range(table_widget.rowCount()):
                row_data = []
                for column in range(table_widget.columnCount()):
                    item = table_widget.item(row, column)
                    row_data.append(item.text() if item is not None else "")
                data.append(row_data)
            df = pd.DataFrame(data, columns=headers)
            dataframes.append(df)

        # Print dataframes
        for idx, df in enumerate(dataframes, start=1):
            print(f"DataFrame {idx}:")
            print(df)
            print("\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())