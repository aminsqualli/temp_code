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

    def paste(self, text, top_left_index):
        rows = text.split('\n')
        for i, row_text in enumerate(rows):
            columns = row_text.split('\t')
            for j, column_text in enumerate(columns):
                if i < len(rows) and j < len(columns):
                    index = self.index(top_left_index.row() + i, top_left_index.column() + j)
                    self.setData(index, column_text)

def main():
    app = QtWidgets.QApplication([])
    data = [[''] * 5 for _ in range(5)]  # Example data
    headers = ['Column {}'.format(i) for i in range(5)]  # Example headers
    model = CustomTableModel(data, headers)
    table_view = QtWidgets.QTableView()
    table_view.setModel(model)

    # Create main window and set the table view as central widget
    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(table_view)

    # Add paste action to main window
    def handle_paste():
        clipboard = QtWidgets.QApplication.clipboard()
        mime_data = clipboard.mimeData()
        if mime_data.hasText():
            top_left_index = table_view.currentIndex()
            model.paste(mime_data.text(), top_left_index)

    paste_action = QtWidgets.QAction("Paste", main_window)
    paste_action.setShortcut(QtGui.QKeySequence.Paste)
    paste_action.triggered.connect(handle_paste)
    main_window.addAction(paste_action)

    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
    
def paste(self, text, top_left_index):
    rows = text.split('\n')
    for i, row_text in enumerate(rows):
        columns = row_text.split('\t')
        for j, column_text in enumerate(columns):
            if i < len(rows) and j < len(columns):
                index = self.index(top_left_index.row() + i, top_left_index.column() + j)
                try:
                    # Try to convert the text to a float
                    value = float(column_text)
                    self.setData(index, value)
                except ValueError:
                    # If conversion fails, set the data as text
                    self.setData(index, column_text)
