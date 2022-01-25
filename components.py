from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox

class Components(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Components')
        checkbox = QCheckBox('New Checkbox')
        checkbox.setTristate(True)
        checkbox.stateChanged.connect(self.show_state)
        self.setCentralWidget(checkbox)

    def show_state(self, state):
        print('Checkbox state: ', state)
        if state == Qt.Checked:
            print('Checked')
        elif state == Qt.PartiallyChecked:
            print('Partially Checked')
        elif state == Qt.Unchecked:
            print('No Checked')
        else:
            print('Invalid state of checkbox')

if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    app.exec()