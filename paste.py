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

        value = self._data[index.row()][index.column()]
        
        if role == QtCore.Qt.DisplayRole:
            # Display numeric values as floats
            if isinstance(value, (int, float)):
                return "{:.2f}".format(value)
            return str(value)
        elif role == QtCore.Qt.EditRole:
            # Make numeric values editable as floats
            if isinstance(value, (int, float)):
                return "{:.2f}".format(value)
            return str(value)
        
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
            try:
                # Try to convert the value to float
                value = float(value)
            except ValueError:
                pass  # If conversion fails, keep the value as string
            
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def paste(self, text, top_left_index):
        rows = text.split('\n')
        num_rows = len(rows)
        num_columns = 0
        
        # Determine the number of columns in the pasted data
        for row_text in rows:
            columns = row_text.split('\t')
            num_columns = max(num_columns, len(columns))
        
        # Ensure the model has enough rows and columns to accommodate the pasted data
        self.insertRows(top_left_index.row(), num_rows)
        self.insertColumns(top_left_index.column(), num_columns)
        
        # Paste the data
        for i, row_text in enumerate(rows):
            columns = row_text.split('\t')
            for j, column_text in enumerate(columns):
                if i < len(rows) and j < len(columns):
                    index = self.index(top_left_index.row() + i, top_left_index.column() + j)
                    try:
                        # Try to convert the text to a float
                        value = float(column_text)
                    except ValueError:
                        # If conversion fails, keep the value as string
                        value = column_text
                    self.setData(index, value)