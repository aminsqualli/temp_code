import sys
from PySide6.QtWidgets import QApplication, QDialog, QTableView, QVBoxLayout, QPushButton, QStandardItemModel, QStandardItem

class TableViewDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        self.add_row_button = QPushButton("Add Row")
        self.add_row_button.clicked.connect(self.add_row)

        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.add_row_button)
        self.setLayout(layout)

        self.populate_initial_data()

    def populate_initial_data(self):
        # Populate initial data
        self.model.setColumnCount(2)
        self.model.setHorizontalHeaderLabels(["Column 1", "Column 2"])
        self.add_row()

    def add_row(self):
        row = [QStandardItem("Data 1"), QStandardItem("Data 2")]
        self.model.appendRow(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = TableViewDialog()
    dialog.exec()