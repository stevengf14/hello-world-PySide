from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit


class Components(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Components')
        text_line = QLineEdit()
        text_line.setMaxLength(15)
        text_line.setPlaceholderText('Here is the name')
        # text_line.setReadOnly(True)
        text_line.setInputMask('00-0000-0000')
        text_line.returnPressed.connect(self.press_enter)
        text_line.selectionChanged.connect(self.change_selection)
        text_line.textChanged.connect(self.change_text)
        self.setCentralWidget(text_line)

    def press_enter(self):
        print('Enter pressed')
        self.centralWidget().setText('00-0000-0000')

    def change_selection(self):
        print('Change selection')
        print(self.centralWidget().selectedText())

    def change_text(self, new_text):
        print('Text Change:s', new_text)

if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    app.exec()