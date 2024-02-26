import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the tab layout from the .ui file
        self.tab_widget = uic.loadUi("your_tab_ui_file.ui")

        # Set up the "OK" button manually
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_clicked)

        # Add the "OK" button to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        layout.addWidget(self.ok_button)

        # Set the layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def ok_clicked(self):
        print("OK button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())