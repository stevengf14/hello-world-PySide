from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox


class Components(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Components')
        combobox = QComboBox()
        combobox.addItem('First')
        combobox.addItems(['Second', 'Third'])
        combobox.currentIndexChanged.connect(self.change_index)
        combobox.currentTextChanged.connect(self.change_text)
        combobox.setEditable(True)
        # combobox.setInsertPolicy(QComboBox.NoInsert)
        # combobox.setInsertPolicy(QComboBox.InsertAtTop)
        # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        combobox.setMaxCount(6)
        self.setCentralWidget(combobox)

    def change_index(self, new_index):
        print(f'New Index: {new_index}')

    def change_text(self, new_text):
        print(f'New text: {new_text}')

if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    app.exec()