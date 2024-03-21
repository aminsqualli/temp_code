from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableView, QApplication
from PyQt6.QtGui import QKeySequence


class CustomTableView(QTableView):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Backspace:
            indexes = self.selectedIndexes()
            if indexes:
                index = indexes[0]
                self.model().setData(index, "", Qt.ItemDataRole.EditRole)
        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QAbstractTableModel

    class CustomTableModel(QAbstractTableModel):
        def __init__(self, data, headers):
            super().__init__()
            self._data = data
            self._headers = headers

        def rowCount(self, parent):
            return len(self._data)

        def columnCount(self, parent):
            return len(self._headers)

        def data(self, index, role):
            if role == Qt.ItemDataRole.DisplayRole:
                return self._data[index.row()][index.column()]

        def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
            if role == Qt.ItemDataRole.EditRole:
                self._data[index.row()][index.column()] = value
                return True
            return False

        def headerData(self, section, orientation, role):
            if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
                return self._headers[section]

        def flags(self, index):
            return Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled

    app = QApplication(sys.argv)
    data = [[f"Row {i}, Col {j}" for j in range(3)] for i in range(4)]
    headers = ["Column 1", "Column 2", "Column 3"]
    model = CustomTableModel(data, headers)
    view = CustomTableView()
    view.setModel(model)
    view.show()
    sys.exit(app.exec())