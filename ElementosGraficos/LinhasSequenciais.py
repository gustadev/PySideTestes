from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint
import sys


class LineDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desenhando Linhas com o Mouse")
        self.setGeometry(100, 100, 600, 400)
        self.start_point = None
        self.end_point = None
        self.lines = []  # Lista de linhas desenhadas (pares de pontos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.start_point is None:
                # Primeiro clique: define o ponto inicial
                self.start_point = event.position().toPoint()
            else:
                # Segundo clique: define o ponto final e desenha
                self.end_point = event.position().toPoint()
                self.lines.append((self.start_point, self.end_point))
                #self.start_point = None
                #self.end_point = None
                self.start_point = self.end_point
                self.end_point = None 
                self.update()  # Atualiza o widget para chamar paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("black"), 2)
        painter.setPen(pen)
        
        for line in self.lines:
            painter.drawLine(line[0], line[1])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LineDrawer()
    window.show()
    sys.exit(app.exec())