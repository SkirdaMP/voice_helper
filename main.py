from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread
from GUI import Ui_MainWindow
import sys
import speech_recognition as sr


class TreadVoice(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        pass    


class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_listen.clicked.connect(self.voiceListen)

    def voiceListen(self):
        print('Произошёл запуск')
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # self.ui.label.setText("Говорите")
            r.pause_threshold = 0.5
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            task = r.recognize_google(audio, language="ru-RU").lower()
            if "закрыть" in task:
                sys.exit(0)
            else:
                self.ui.listWidget.addItem("Вы сказали " + task)
                # self.ui.label.setText("Вы сказали " + task)
                # self.ui.label.adjustSize()
        except (sr.UnknownValueError, sr.RequestError):
            self.ui.listWidget.addItem('Не понятно, повторите')
            # self.ui.label.setText('Не понятно, повторите')
            task = self.voiceListen()
        return task

    # def sayText(task):
    #     if "стоп" in task:
    #         sys.exit(0)
    #     else:
    #         self.ui.label.setText("Вы сказали " + task)
    #         self.ui.label.adjustSize()

    def main(self):
        self.voiceListen()

app = QtWidgets.QApplication([])
application = mainwindow()
application.show()

sys.exit(app.exec())
