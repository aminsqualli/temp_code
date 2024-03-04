class CheckableListModel(QAbstractListModel):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.checked_items = [False] * len(items)  # Initialize all items as unchecked

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.items[index.row()]
        elif role == Qt.CheckStateRole:
            return Qt.Checked if self.checked_items[index.row()] else Qt.Unchecked

    def setData(self, index, value, role):
        if role == Qt.CheckStateRole:
            self.checked_items[index.row()] = value == Qt.Checked
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable