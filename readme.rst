-----------------------
qtlayout module
-----------------------

Intro
------

This module makes it easier to programatically layout widgets for PyQt and PySide
applications in Python.  There are several helper functions which wrap commonly used
layouts.

*qtlayout* uses the *qtpy* module to support PyQt4, PyQt5, and PySide.

The following layouts are currently handled:

    * hbox - QHBoxLayout
    * vbox - QVBoxLayout
    * stack - QStackWidget
    * grid - QGridLayout
    * hsplit - QSplitter (with horizontal orientation)
    * vsplit - QSplitter (with vetical orientation)
    * flow - custom flow layout container


Example
--------

To layout a few widgets in a QHBoxLayout:

.. code-block:: python

    # the necessary imports
    from qtlayout import QtWidgets, hbox

    # must create a QApplication first
    qapp = QtWidgets.QApplication(['test'])

    # define our controls
    label = QtWidgets.QLabel('A label')
    btn = QtWidgets.QPushButton('Push me')
    editor = QtWidgets.QLineEdit('editing')

    # lay them out in an hbox layout.  This takes care
    # of creating a parent widget, creating a layout,
    # setting the layout of the parent widget, and (finally)
    # adding all of the controls to the layout.
    # The parent widget is returned.
    w = hbox(label, btn, editor)

    # create the main window and go
    mw = QtWidgets.QMainWindow()
    mw.setCentralWidget(w)
    mw.show()
    qapp.exec_()


Links to External Documentation
--------------------------------

    * Qt: http://doc.qt.io/
    * PySide: http://wiki.qt.io/PySide
    * PySide2: https://wiki.qt.io/PySide2
    * PyQt4, PyQt5: https://riverbankcomputing.com/software/pyqt/intro
    * qtpy: https://github.com/spyder-ide/qtpy


