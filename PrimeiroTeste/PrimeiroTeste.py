from PySide6.QtCore import Qt
from PySide6.QtGui import (QFont, QAction)
from PySide6.QtWidgets import ( QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow )
from qdarktheme import load_stylesheet

def callback():
    print("Cliquei no botão!!!")


def callback2():
    print("Callback2 acionado!!!")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        base = QWidget()
        layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(90)

        label = QLabel("PrimeiroTesteLabel")
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        botao = QPushButton("PrimeiroTestebutton")
        botao.setFont(font)
        botao.clicked.connect(callback)
        layout.addWidget(botao)

        base.setLayout(layout)

        self.setCentralWidget(base)

        menu = self.menuBar()
        arquivo_menu = menu.addMenu("Arquivo")
        action = QAction("Print!")
        action.triggered.connect(callback2)
        arquivo_menu.addAction(action)




app = QApplication()
app.setStyleSheet(load_stylesheet()) # 'light'
janela = Window()

janela.show()

app.exec()
