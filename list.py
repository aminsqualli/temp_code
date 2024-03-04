import sys
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListView, QLineEdit, QPushButton


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


class CheckableListWidget(QWidget):
    def __init__(self, items):
        super().__init__()
        self.model = CheckableListModel(items)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Search Box
        search_layout = QHBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search...")
        self.search_box.textChanged.connect(self.filter_list)
        search_layout.addWidget(self.search_box)

        # List Box
        self.list_view = QListView()
        self.list_view.setModel(self.model)
        self.list_view.setEditTriggers(QListView.NoEditTriggers)
        layout.addLayout(search_layout)
        layout.addWidget(self.list_view)

        # Select All Button
        self.select_button = QPushButton("Select All")
        self.select_button.clicked.connect(self.select_all)
        layout.addWidget(self.select_button)

        # Print Selected Button
        print_button = QPushButton("Print Selected")
        print_button.clicked.connect(self.print_selected)
        layout.addWidget(print_button)

        self.setLayout(layout)

    def filter_list(self, text):
        self.model.beginResetModel()
        if text:
            filtered_items = [item for item in self.model.items if text.lower() in item.lower()]
            filtered_checked = [self.model.checked_items[i] for i, item in enumerate(self.model.items) if
                                text.lower() in item.lower()]
            self.model.items = filtered_items
            self.model.checked_items = filtered_checked
        else:
            self.model.items = items
        self.model.endResetModel()

    def select_all(self):
        all_checked = all(self.model.checked_items)
        for i in range(len(self.model.checked_items)):
            self.model.checked_items[i] = not all_checked
        self.model.dataChanged.emit(self.model.index(0), self.model.index(self.model.rowCount() - 1))

    def print_selected(self):
        selected_items = [self.model.items[i] for i, checked in enumerate(self.model.checked_items) if checked]
        print("Selected items:", selected_items)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    items = ["Apple", "Banana", "Orange", "Grapes", "Pineapple", "Mango"]
    widget = CheckableListWidget(items)
    widget.setWindowTitle("Checkable List Widget")
    widget.resize(300, 300)
    widget.show()
    sys.exit(app.exec())