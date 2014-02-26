
from qt_easy_layout.qt import use_pyside, use_pyqt

from qt_easy_layout.layouts import hbox, vbox, hsplit, vsplit, grid
from qt_easy_layout import qti

print(qti.QtGui)

def test_1():
    use_pyqt()
    mw = qti.QtGui.QMainWindow()
    print(type(mw))
    label = qti.QtGui.QLabel('A label')
    btn = qti.QtGui.QPushButton('Push me')
    btn.setMinimumHeight(100)
    editor = qti.QtGui.QLineEdit('editing')

    label2 = qti.QtGui.QLabel('A label 2')
    btn2 = qti.QtGui.QPushButton('Push me 2')
    editor2 = qti.QtGui.QLineEdit('editing 2')

    w3 = vbox(hbox(label, btn, editor),
              hbox(label2, btn2, editor2)
              )


    mw.setCentralWidget(w3)
    mw.setWindowTitle('test_1 - vbox - ' + str(type(mw)))
    return mw

def test_2():
    use_pyqt()
    mw = qti.QtGui.QMainWindow()

    lw = qti.QtGui.QListWidget(mw)

    label = qti.QtGui.QLabel('A label')
    btn = qti.QtGui.QPushButton('Push me')
    editor = qti.QtGui.QLineEdit('editing')

    w = vsplit(lw,
               hbox(label, btn, editor)
               )

    mw.setCentralWidget(w)
    mw.setWindowTitle('test_2 - vsplit - ' + str(type(mw)))
    return mw



def test_3():
    use_pyside()
    mw = qti.QtGui.QMainWindow()

    label = qti.QtGui.QLabel('A label')
    btn = qti.QtGui.QPushButton('Push me')
    editor = qti.QtGui.QLineEdit('editing')

    label2 = qti.QtGui.QLabel('A label 2')
    btn2 = qti.QtGui.QPushButton('Push me 2')
    editor2 = qti.QtGui.QLineEdit('editing 2')

    w = hsplit(
           vsplit(
              vbox(
                  hbox(label, btn, editor),
                  hbox(label2, btn2, editor2)
                ),
              qti.QtGui.QListWidget()
             ),
           qti.QtGui.QTextEdit()
           )

    mw.setCentralWidget(w)
    mw.setWindowTitle('test_3 - complex - ' + str(type(mw)))
    return mw

def test_4():
    """
    testing a grid layout
    """
    use_pyside()
    mw = qti.QtGui.QMainWindow()

    label = qti.QtGui.QLabel('A label')
    btn = qti.QtGui.QPushButton('Push me')
    editor = qti.QtGui.QLineEdit('editing')

    label2 = qti.QtGui.QLabel('A label 2')
    btn2 = qti.QtGui.QPushButton('Push me 2')
    editor2 = qti.QtGui.QLineEdit('editing 2')

    label3 = qti.QtGui.QLabel('A label 3')
    btn3 = qti.QtGui.QPushButton('Push me 3')
    editor3 = qti.QtGui.QLineEdit('editing 3')

    w3 = grid([[label, btn, editor],
               [label2, btn2, editor2],
               [label3, btn3, editor3]],
              margin=10)

    mw.setCentralWidget(w3)
    mw.setWindowTitle('test_4 - grid - ' + str(type(mw)))
    return mw


if __name__ == "__main__":
    qapp = qti.QtGui.QApplication(['test'])
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

