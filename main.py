import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = True
        self.circles = 0
        self.setWindowTitle('Git и жёлтые окружности')

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.circles += 1
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(self.circles):
            qp.setPen(QColor((255, 255, 0)))
            size = randint(0, 200)
            x1, y1 = randint(0, 709 - size), randint(0, 521 - size)
            qp.drawEllipse(x1, y1, size, size)
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
