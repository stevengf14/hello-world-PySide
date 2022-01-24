import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class WindowPySide(QMainWindow):
    def __init__(self):
        # Call init method from parent class
        super().__init__()
        self.setWindowTitle('OOP with PySide')
        # self.window.resize(600, 400)
        # height and width values are fixed
        self.setFixedSize(QSize(600,400))
        # Creating components
        self._add_components()

    def _add_components(self):
        # Add a menu
        menu = self.menuBar()
        menu_file = menu.addMenu('File')
        # Add many options to the menu
        action_new  = QAction('New', self)
        menu_file.addAction(action_new)
        # Add text to state bar
        action_new.setStatusTip('New File')
        # Add message in the status bar
        self.statusBar().showMessage('Status Bar information...')
        # Add a button
        button = QPushButton('New Button')
        # Public button in the window
        self.setCentralWidget(button)

if __name__ == '__main__':
    app = QApplication([])
    # Create a window object
    window = WindowPySide()
    window.show()
    # Execute window
    sys.exit(app.exec())
