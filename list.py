import sys
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListView, QLineEdit, QPushButton, QStyledItemDelegate, QCheckBox


class CheckableListModel(QAbstractListModel):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.checked_items = [False] * len(items)  # Initialize all items as unchecked
        self.filtered_indices = list(range(len(items)))  # Indices of items after filtering

    def rowCount(self, parent=QModelIndex()):
        return len(self.filtered_indices)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.items[self.filtered_indices[index.row()]]
        elif role == Qt.CheckStateRole:
            return Qt.Checked if self.checked_items[self.filtered_indices[index.row()]] else Qt.Unchecked

    def setData(self, index, value, role):
        if role == Qt.CheckStateRole:
            self.checked_items[self.filtered_indices[index.row()]] = value == Qt.Checked
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable


class CheckableItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        checked = index.data(Qt.CheckStateRole) == Qt.Checked
        checkbox_rect = option.rect.adjusted(5, 0, -5, 0)
        super().paint(painter, option, index)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white if option.state & QStyle.State_Selected else option.palette.base())
        painter.drawRect(checkbox_rect)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black if checked else Qt.lightGray)
        painter.drawRoundedRect(checkbox_rect.adjusted(2, 2, -2, -2), 3, 3)

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            if option.rect.adjusted(5, 0, -5, 0).contains(event.pos()):
                model.setData(index, Qt.Checked if model.data(index, Qt.CheckStateRole) == Qt.Unchecked else Qt.Unchecked, Qt.CheckStateRole)
                return True
        return super().editorEvent(event, model, option, index)


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
        self.list_view.setItemDelegate(CheckableItemDelegate())
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
        filtered_indices = []
        for i, item in enumerate(self.model.items):
            if text.lower() in item.lower():
                filtered_indices.append(i)
        self.model.filtered_indices = filtered_indices
        self.model.layoutChanged.emit()

    def select_all(self):
        all_checked = all(self.model.checked_items)
        for i in self.model.filtered_indices:
            self.model.checked_items[i] = not all_checked
        self.model.dataChanged.emit(self.model.index(0), self.model.index(len(self.model.filtered_indices) - 1))

    def print_selected(self):
        selected_items = [self.model.items[i] for i in self.model.filtered_indices if self.model.checked_items[i]]
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