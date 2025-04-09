from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPen, QBrush
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsItem

application = QApplication()

mainWindow = QMainWindow()
mainWindow.setWindowTitle("Quadrados Moviveis")
mainWindow.setMinimumSize(800,600)
#mainWindow.setFixedSize(800,800)

cena = QGraphicsScene(mainWindow)
visualizacao = QGraphicsView(cena)

linha_azul = QPen(Qt.GlobalColor.blue,6)
linha_vermelha = QPen(Qt.GlobalColor.red,6)
linha_verde = QPen(Qt.GlobalColor.green,6)

fundo_azul = QBrush(Qt.GlobalColor.blue)
fundo_vermelha = QBrush(Qt.GlobalColor.red)
fundo_verde = QBrush(Qt.GlobalColor.green)

rect1 = cena.addRect (50, 50, 100, 100, linha_azul, fundo_vermelha)
rect2 = cena.addRect (100, 100, 100, 100, linha_vermelha, fundo_azul)
rect3 = cena.addRect (150, 150, 100, 100, linha_verde, fundo_verde)
rect1.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
rect2.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
rect3.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

mainWindow.setCentralWidget(visualizacao)

mainWindow.show()

application.exec()
