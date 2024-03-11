from PyQt5 import QtCore, QtGui, QtWidgets

class CustomTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers, parent=None):
        super().__init__(parent)
        self._data = data
        self._headers = headers

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QtCore.QModelIndex()):
        if self._data:
            return len(self._data[0])
        return 0

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            if section < len(self._headers):
                return self._headers[section]
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

class MyTableView(QtWidgets.QTableView):
    def paste(self):
        clipboard = QtWidgets.QApplication.clipboard()
        mime_data = clipboard.mimeData()

        if mime_data.hasText():
            text = mime_data.text()
            rows = text.split('\n')
            selected_indexes = self.selectedIndexes()

            if selected_indexes:
                top_left_index = selected_indexes[0]

                for i, row_text in enumerate(rows):
                    columns = row_text.split('\t')
                    for j, column_text in enumerate(columns):
                        if i < len(selected_indexes) and j < len(columns):
                            index = self.model().index(top_left_index.row() + i, top_left_index.column() + j)
                            self.model().setData(index, column_text)

def main():
    app = QtWidgets.QApplication([])
    data = [[''] * 5 for _ in range(5)]  # Example data
    headers = ['Column {}'.format(i) for i in range(5)]  # Example headers
    model = CustomTableModel(data, headers)
    table_view = MyTableView()
    table_view.setModel(model)

    # Create main window and set the table view as central widget
    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(table_view)

    # Add paste action to main window
    paste_action = QtWidgets.QAction("Paste", main_window)
    paste_action.setShortcut(QtGui.QKeySequence.Paste)
    paste_action.triggered.connect(table_view.paste)
    main_window.addAction(paste_action)

    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()