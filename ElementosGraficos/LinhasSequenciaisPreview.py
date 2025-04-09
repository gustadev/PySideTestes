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
        self.drawing = False
        self.lines = []  # Lista de linhas desenhadas (pares de pontos)
        self.lastLine = None
        

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.start_point is None:
                # Primeiro clique: define o ponto inicial
                self.start_point = event.position().toPoint()
                self.drawing = True
        else :
            if event.button() == Qt.MouseButton.RightButton:
                self.lines.clear()
                self.lastLine = None
                self.start_point = None
                self.end_point = None
                self.update()

           
    def mouseMoveEvent(self, event):
        if self.drawing:
            current_point = event.position().toPoint()
            self.lastLine = (self.start_point, current_point)
            self.update()

    def mouseReleaseEvent(self, event):
        self.drawing = False
        self.lines.append(self.lastLine)
        self.lastLine = None
        self.start_point = self.end_point
        self.end_point = None 
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("black"), 2)
        painter.setPen(pen)    
        if self.lastLine != None :
            painter.drawLine(self.lastLine[0],self.lastLine[1])
        # if self.lines.count() > 0 :
        for line in self.lines:
            if line != None :
                painter.drawLine(line[0], line[1])
                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LineDrawer()
    window.show()
    sys.exit(app.exec())