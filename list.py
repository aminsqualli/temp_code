import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QCheckBox, QListWidgetItem


class CheckableListWidget(QWidget):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.checked_items = set()  # Store checked items separately
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
        self.list_widget.setSelectionMode(QListWidget.MultiSelection)
        self.populate_list()
        layout.addLayout(search_layout)
        layout.addWidget(self.list_widget)

        # Select All Button
        select_button = QPushButton("Select All")
        select_button.clicked.connect(self.select_all)
        layout.addWidget(select_button)

        # Print Selected Button
        print_button = QPushButton("Print Selected")
        print_button.clicked.connect(self.print_selected)
        layout.addWidget(print_button)

        self.setLayout(layout)

    def populate_list(self):
        for item in self.items:
            list_item = QListWidgetItem()
            checkbox = QCheckBox(item)
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, checkbox)

    def filter_list(self, text):
        self.list_widget.clear()
        for item in self.items:
            if text.lower() in item.lower():
                list_item = QListWidgetItem()
                checkbox = QCheckBox(item)
                self.list_widget.addItem(list_item)
                self.list_widget.setItemWidget(list_item, checkbox)
                if item in self.checked_items:  # Set checkbox state based on stored checked items
                    checkbox.setChecked(True)

    def select_all(self):
        self.checked_items.clear()  # Clear stored checked items
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            widget = self.list_widget.itemWidget(item)
            widget.setChecked(True)
            self.checked_items.add(widget.text())  # Add checked item to stored checked items

    def print_selected(self):
        selected_items = []
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            widget = self.list_widget.itemWidget(item)
            if widget.isChecked():
                selected_items.append(widget.text())
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