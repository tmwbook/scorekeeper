'''
@author: Thomas
'''
import sys
import os
import atexit
username = os.environ.get("USERNAME")
DIRECTORY_FOR_FILES = os.getcwd() + "\\SCORE_FILES\\"
APP_DATA_DIR = 'C:/users/' + username + '/appdata/local/Score Keeper/'

nameOne = ''
nameTwo = ''
scoreOne = 0
scoreTwo = 0

#UI AUTOMATED CODE

from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(379, 152)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(379, 152))
        Form.setMaximumSize(QtCore.QSize(379, 152))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 381, 161))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.playerOne_txt = QtGui.QLineEdit(self.tab)
        self.playerOne_txt.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.playerOne_txt.setObjectName(_fromUtf8("playerOne_txt"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 131, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.playerTwo_txt = QtGui.QLineEdit(self.tab)
        self.playerTwo_txt.setGeometry(QtCore.QRect(10, 80, 131, 31))
        self.playerTwo_txt.setObjectName(_fromUtf8("playerTwo_txt"))
        self.playerTwoScore_inc = QtGui.QSpinBox(self.tab)
        self.playerTwoScore_inc.setGeometry(QtCore.QRect(180, 80, 42, 31))
        self.playerTwoScore_inc.setObjectName(_fromUtf8("playerTwoScore_inc"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(260, 82, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.playerOneScore_inc = QtGui.QSpinBox(self.tab)
        self.playerOneScore_inc.setGeometry(QtCore.QRect(180, 30, 42, 31))
        self.playerOneScore_inc.setObjectName(_fromUtf8("playerOneScore_inc"))
        self.scores = QtGui.QLabel(self.tab)
        self.scores.setGeometry(QtCore.QRect(180, 10, 46, 13))
        self.scores.setObjectName(_fromUtf8("scores"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.directoryChange_txt = QtGui.QLineEdit(self.tab_2)
        self.directoryChange_txt.setGeometry(QtCore.QRect(10, 50, 331, 31))
        self.directoryChange_txt.setObjectName(_fromUtf8("directoryChange_txt"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 331, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.submitChanges)
        QtCore.QObject.connect\
            (self.playerOneScore_inc, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Form.changeScoreOne)
        QtCore.QObject.connect\
            (self.playerTwoScore_inc, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Form.changeScoreTwo)
        QtCore.QObject.connect(self.playerOne_txt, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Form.changeNameOne)
        QtCore.QObject.connect(self.playerTwo_txt, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Form.changeNameTwo)
        QtCore.QObject.connect\
            (self.directoryChange_txt, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), Form.changeDirectory)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Score Keeper", None))
        self.playerOne_txt.setPlaceholderText(_translate("Form", "Enter Name(s)...", None))
        self.label.setText(_translate("Form", "Player/ Team 1", None))
        self.playerTwo_txt.setPlaceholderText(_translate("Form", "Enter Names(s)...", None))
        self.label_2.setText(_translate("Form", "Player/Team 2", None))
        self.pushButton.setToolTip(_translate("Form",\
                                              "<html><head/><body><p>Press to apply all changes made in the fields\
                                              </p></body></html>", None))
        self.pushButton.setText(_translate("Form", "Submit Changes", None))
        self.scores.setText(_translate("Form", "Scores", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Match", None))
        self.directoryChange_txt.setText(_translate("Form", "C:/foulder/sub-foulder/sub-foulder/", None))
        self.label_3.setText(_translate("Form", \
                                        "Enter the directory you want your txt files to go following the format\n"
"in the box.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Settings", None))

    #these functions pass the information from the widgets to functions outside of the class
    def submitChanges(self):
        commitChanges()

    def changeScoreOne(self):
        changeScore(1, self.playerOneScore_inc.value())

    def changeScoreTwo(self):
        changeScore(2, self.playerTwoScore_inc.value())

    def changeNameOne(self):
        changeName(1, self.playerOne_txt.text())

    def changeNameTwo(self):
        changeName(2, self.playerTwo_txt.text())

    def changeDirectory(self):
        changeFileDirectory(self.directoryChange_txt.text())

#Functions that change globals


def changeScore(playerNumber, score):
    global scoreOne, scoreTwo
    if playerNumber == 1:
        scoreOne = score
        #print scoreOne
        return scoreOne
    else:
        scoreTwo = score
        #print scoreTwo
        return scoreTwo


def changeName(playerNumber, name):
    global nameOne, nameTwo
    if playerNumber == 1:
        nameOne = name
        #print nameOne
        return name
    else:
        nameTwo = name
        #print nameTwo
        return name


def changeFileDirectory(directory):
    global DIRECTORY_FOR_FILES
    DIRECTORY_FOR_FILES = directory
    #print DIRECTORY_FOR_FILES
    return DIRECTORY_FOR_FILES


def commitChanges():
    global DIRECTORY_FOR_FILES, nameOne, scoreOne, nameTwo, scoreTwo
    files = ['player_one_name.txt', 'player_one_score.txt', 'player_two_name.txt', 'player_two_score.txt']
    data = [nameOne, scoreOne, nameTwo, scoreTwo]
    i = 0
    if not foulderExists(DIRECTORY_FOR_FILES):
        os.makedirs(DIRECTORY_FOR_FILES)
    for end in files:
        with open(DIRECTORY_FOR_FILES + end, 'w') as x:
            x.write(str(data[i]))
        i += 1


def foulderExists(foulder):
    check = os.path.exists(foulder)
    return check


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
