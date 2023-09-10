from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QHBoxLayout, QMessageBox, QWidget, QPushButton, QLabel, QVBoxLayout


app = QApplication([])#сворюємо додаток

main_win = QWidget()#створюємо вікно
main_win.setWindowTitle("Конкурс від Crazy People")#назва вікна
main_win.resize(400, 200)#розмір

question = QLabel("Коли пукнув Христофор Колумб?")
btn1 = QRadioButton("1991")
btn2 = QRadioButton("1266")
btn3 = QRadioButton("3000")
btn4 = QRadioButton("0001")

vline = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()

vline.addWidget(question, alignment=Qt.AlignCenter)
row1.addWidget(btn1, alignment=Qt.AlignCenter)
row1.addWidget(btn2, alignment=Qt.AlignCenter)
row2.addWidget(btn3, alignment=Qt.AlignCenter)
row2.addWidget(btn4, alignment=Qt.AlignCenter)

vline.addLayout(row1)
vline.addLayout(row2)

main_win.setLayout(vline)

def show_win():
    message = QMessageBox()
    message.setText("Ви відповіли правильно!")
    message.exec_()

btn3.clicked.connect(show_win)

main_win.show()#показуємо вікно
app.exec_()