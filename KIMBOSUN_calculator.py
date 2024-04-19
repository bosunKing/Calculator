import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import re

from_class = uic.loadUiType("/home/bo/amr_ws/PyQt/src/calculator_bosun.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = ""
        self.textEdit2.setText("0")
        self.setWindowTitle("Hello, Qt!")

        self.button0.clicked.connect(self.button0_clicked)
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
        self.button4.clicked.connect(self.button4_clicked)
        self.button5.clicked.connect(self.button5_clicked)
        self.button6.clicked.connect(self.button6_clicked)
        self.button7.clicked.connect(self.button7_clicked)
        self.button8.clicked.connect(self.button8_clicked)
        self.button9.clicked.connect(self.button9_clicked)
        self.buttonClr.clicked.connect(self.buttonClr_clicked)
        self.buttonDel.clicked.connect(self.buttonDel_clicked)
        self.buttonDot.clicked.connect(self.buttonDot_clicked)
        self.buttonPer.clicked.connect(self.buttonPer_clicked)
        self.buttonDiv.clicked.connect(self.buttonDiv_clicked)
        self.buttonEq.clicked.connect(self.buttonEq_clicked)
        self.buttonMinus.clicked.connect(self.buttonMinus_clicked)
        self.buttonMul.clicked.connect(self.buttonMul_clicked)
        self.buttonPlus.clicked.connect(self.buttonPlus_clicked)

    def clean_text(self, text):
        # 정규 표현식을 사용하여 0을 제거
        cleaned_text = re.sub(r'\b0+(\d*\.\d+|\d+)', r'\1', text)
        return cleaned_text



    def button0_clicked(self):
        self.text += "0"
        self.textEdit1.setText(self.text)

    def button1_clicked(self):
        self.text += "1"
        self.textEdit1.setText(self.text)

    def button2_clicked(self):
        self.text += "2"
        self.textEdit1.setText(self.text)

    def button3_clicked(self):
        self.text += "3"
        self.textEdit1.setText(self.text)

    def button4_clicked(self):
        self.text += "4"
        self.textEdit1.setText(self.text)

    def button5_clicked(self):
        self.text += "5"
        self.textEdit1.setText(self.text)

    def button6_clicked(self):
        self.text += "6"
        self.textEdit1.setText(self.text)

    def button7_clicked(self):
        self.text += "7"
        self.textEdit1.setText(self.text)

    def button8_clicked(self):
        self.text += "8"
        self.textEdit1.setText(self.text)

    def button9_clicked(self):
        self.text += "9"
        self.textEdit1.setText(self.text)

    def buttonClr_clicked(self):
        self.text = ""
        self.textEdit1.setText(self.text)
        self.textEdit2.setText("0")

    def buttonDel_clicked(self):
        self.text = self.text[:-1]
        self.textEdit1.setText(self.text)

    def buttonPer_clicked(self):
        if(self.text[-1].isdigit() or self.text[-1] == "."):
            match = re.search(r'(\d*\.?\d*)$', self.text)
            if match:
                number = match.group(1)
                percentage = str(float(number) / 100)
                self.text = self.text[:-len(number)] + percentage
                self.textEdit1.setText(self.text)

    def buttonDot_clicked(self):
        # 정규표현식을 사용하여 기호 뒤에 마침표가 있는지 확인
        if not re.search(r'\.\d*$', self.text):
            # 마침표가 없으면 추가
            self.text += "."
            self.textEdit1.setText(self.text)


    def buttonPlus_clicked(self):
        # if self.text and (self.text[-1].isdigit() or self.text[-1] == "."):
        self.text += "+"
        self.textEdit1.setText(self.text)

    def buttonMinus_clicked(self):
        self.text += "-"
        self.textEdit1.setText(self.text)
        
        

    def buttonDiv_clicked(self):
        try:
            if self.text and (self.text[-1].isdigit() or self.text[-1] == "."):
                self.text += "/"
                self.textEdit1.setText(self.text)
            elif self.text[-1] == "/" or self.text[-1] == "*":
                self.text = self.text[:-1] + "/"
                self.textEdit1.setText(self.text)
        except Exception as e:
            pass
            
        
            
            

    def buttonMul_clicked(self):
        try:
            if self.text and (self.text[-1].isdigit() or self.text[-1] == "."):
                self.text += "*"
                self.textEdit1.setText(self.text)
            elif self.text[-1] == "/" or self.text[-1] == "*":
                self.text = self.text[:-1] + "*"
                self.textEdit1.setText(self.text)
        except Exception as e:
            pass
        
            

    def buttonEq_clicked(self):
        try:
            #버튼을 누르지않고도 계산결과를 출력.
            self.text = self.textEdit1.toPlainText()
            # 앞에 나오는 0 및 연산자까지의 0을 제거
            cleaned_text = self.clean_text(self.text)
            result = eval(cleaned_text)
            rounded_result =round(result, 5)
            self.text1 = str(rounded_result)
            self.textEdit2.setText(self.text1)
            # print(cleaned_text)
            # print(result)
            # print(self.text)
            # print(self.text1)

        except Exception as e:
            self.textEdit2.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())