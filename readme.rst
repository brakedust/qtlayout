qt_easy_laoyt module
-----------------------

This module makes it easier to programatically layout widgets for PyQt and PySide
applications in Python.  There are several helper functions which wrap commonly used
layouts (by me anyway).

The following layouts are currently handled:

    * hbox - QHBoxLayout
    * vbox - QVBoxLayout
    * stack - QStackWidget
    * grid - QGridLayout
    * hsplit - QSplitter (with horizontal orientation)
    * vsplit - QSplitter (with vetical orientation)
For example, to layout a few widgets in a QHBoxLayout:

.. code-block::python

from qt_easy_layout import QtGui

        # the necessary imports
        from qt_easy_layout import QtGui, hbox

        # must create a QApplication first
        qapp = QtGui.QApplication(['test'])

        # define our controls
        label = QtGui.QLabel('A label')
        btn = QtGui.QPushButton('Push me')
        editor = QtGui.QLineEdit('editing')

        # lay them out in an hbox layout.  This takes care
        # of creating a parent widget, creating a layout,
        # setting the layout of the parent widget, and (finally)
        # adding all of the controls to the layout.
        # widgets
        # The parent widget is returned.
        w = hbox(label, btn, editor)

        # create the main window and go
        mw = QtGui.QMainWindow()
        mw.setCentralWidget(w)
        mw.show()
        qapp.exec_()

