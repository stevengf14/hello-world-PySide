from PySide6.QtWidgets import QMainWindow, QApplication, QListWidget


class Components(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Components')
        list = QListWidget()
        list.addItem('First')
        list.addItems(['Second', 'Third'])
        list.currentItemChanged.connect(self.change_element)
        list.currentTextChanged.connect(self.change_text)
        self.setCentralWidget(list)

    def change_element(self, new_element):
        print(f'New Element: {new_element.text()}')

    def change_text(self, new_text):
        print(f'New text: {new_text}')

if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    app.exec()