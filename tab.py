import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QTabWidget, QTableView
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
import pandas as pd

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

        return tab_content

    def tables_to_dataframes(self):
        dataframes = []
        for i in range(self.tab_widget.count()):
            tab = self.tab_widget.widget(i)
            table = tab.findChild(QTableView)
            model = table.model()
            if model is not None:
                dataframe = pd.DataFrame([[model.index(row, col).data() for col in range(model.columnCount())]
                                          for row in range(model.rowCount())],
                                         columns=[model.headerData(col, Qt.Horizontal) for col in range(model.columnCount())])
                dataframes.append(dataframe)
        return dataframes

    def ok_clicked(self):
        dataframes = self.tables_to_dataframes()
        for i, df in enumerate(dataframes, 1):
            print(f"Table {i} DataFrame:")
            print(df)
            print()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())