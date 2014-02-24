
from qt_easy_layout.qt import use_pyside
use_pyside()
from qt_easy_layout.layouts import hbox, vbox, hsplit, vsplit, grid
from qt_easy_layout.qt import QtGui

print(QtGui)

def test_1():
    mw = QtGui.QMainWindow()

    label = QtGui.QLabel('A label')
    btn = QtGui.QPushButton('Push me')
    editor = QtGui.QLineEdit('editing')

    label2 = QtGui.QLabel('A label 2')
    btn2 = QtGui.QPushButton('Push me 2')
    editor2 = QtGui.QLineEdit('editing 2')

    w3 = vbox(hbox(label, btn, editor),
              hbox(label2, btn2, editor2)
              )


    mw.setCentralWidget(w3)

    return mw

def test_2():

    mw = QtGui.QMainWindow()

    lw = QtGui.QListWidget(mw)

    label = QtGui.QLabel('A label')
    btn = QtGui.QPushButton('Push me')
    editor = QtGui.QLineEdit('editing')

    w = vsplit(lw,
               hbox(label, btn, editor)
               )

    mw.setCentralWidget(w)

    return mw

def test_3():

    mw = QtGui.QMainWindow()

    label = QtGui.QLabel('A label')
    btn = QtGui.QPushButton('Push me')
    editor = QtGui.QLineEdit('editing')

    label2 = QtGui.QLabel('A label 2')
    btn2 = QtGui.QPushButton('Push me 2')
    editor2 = QtGui.QLineEdit('editing 2')

    w = hsplit(
           vsplit(
              vbox(
                  hbox(label, btn, editor),
                  hbox(label2, btn2, editor2)
                ),
              QtGui.QListWidget()
             ),
           QtGui.QTextEdit()
           )

    mw.setCentralWidget(w)
    return mw

def test_4():
    """
    testing a grid layout
    """
    mw = QtGui.QMainWindow()

    label = QtGui.QLabel('A label')
    btn = QtGui.QPushButton('Push me')
    editor = QtGui.QLineEdit('editing')

    label2 = QtGui.QLabel('A label 2')
    btn2 = QtGui.QPushButton('Push me 2')
    editor2 = QtGui.QLineEdit('editing 2')

    label3 = QtGui.QLabel('A label 3')
    btn3 = QtGui.QPushButton('Push me 3')
    editor3 = QtGui.QLineEdit('editing 3')

    w3 = grid([[label, btn, editor],
             [label2, btn2, editor2],
             [label3, btn3, editor3]],
            parent=None
            )

    mw.setCentralWidget(w3)

    return mw


if __name__ == "__main__":
    qapp = QtGui.QApplication(['test'])
    qapp.setStyle('cleanlooks')
    mw1 = test_1()
    mw1.show()

    mw2 = test_2()
    mw2.show()

    mw3 = test_3()
    mw3.show()

    mw4 = test_4()
    mw4.show()
    qapp.exec_()

