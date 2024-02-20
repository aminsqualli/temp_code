import sys
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import QApplication, QDialog, QTableView, QVBoxLayout, QPushButton

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or [[]]

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self._data[index.row()][index.column()]
        return None

    def setData(self, index: QModelIndex, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index: QModelIndex):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        if self._data:
            return len(self._data[0])
        return 0

class TableViewDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.model = CustomTableModel()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.setEditTriggers(QTableView.DoubleClicked | QTableView.EditKeyPressed)

        self.add_row_button = QPushButton("Add Row")
        self.add_row_button.clicked.connect(self.add_row)

        self.save_button = QPushButton("Save Data")
        self.save_button.clicked.connect(self.save_data)

        layout = QVBoxLayout(self)
        layout.addWidget(self.table_view)
        layout.addWidget(self.add_row_button)
        layout.addWidget(self.save_button)

        self.populate_initial_data()

    def populate_initial_data(self):
        # Populate initial data
        self.model._data = [["Data 1", "Data 2"]]
        self.model.layoutChanged.emit()

    def add_row(self):
        self.model._data.append(["", ""])
        self.model.layoutChanged.emit()

    def save_data(self):
        table_data = self.get_table_data()
        print("Updated Table Data:", table_data)
        # Here you can do whatever you need with the updated table data

    def get_table_data(self):
        data = []
        for row in range(self.model.rowCount()):
            row_data = []
            for column in range(self.model.columnCount()):
                value = self.model.data(self.model.index(row, column), Qt.EditRole)
                row_data.append(value)
            data.append(row_data)
        return data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = TableViewDialog()
    dialog.show()
    sys.exit(app.exec())