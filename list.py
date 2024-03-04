import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton


class CheckableListWidget(QWidget):
    def __init__(self, items):
        super().__init__()
        self.items = items
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
        self.list_widget = QListWidget()
        self.list_widget.addItems(self.items)
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        layout.addLayout(search_layout)
        layout.addWidget(self.list_widget)

        # Button
        select_button = QPushButton("Select All")
        select_button.clicked.connect(self.select_all)
        layout.addWidget(select_button)

        self.setLayout(layout)

    def filter_list(self, text):
        self.list_widget.clear()
        for item in self.items:
            if text.lower() in item.lower():
                self.list_widget.addItem(item)

    def select_all(self):
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            item.setSelected(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    items = ["Apple", "Banana", "Orange", "Grapes", "Pineapple", "Mango"]
    widget = CheckableListWidget(items)
    widget.setWindowTitle("Checkable List Widget")
    widget.resize(300, 300)
    widget.show()
    sys.exit(app.exec())