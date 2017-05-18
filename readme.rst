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
    from qtlayout import QtGui, hbox

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
    # The parent widget is returned.
    w = hbox(label, btn, editor)

    # create the main window and go
    mw = QtGui.QMainWindow()
    mw.setCentralWidget(w)
    mw.show()
    qapp.exec_()


Links to External Documentation
--------------------------------

Documentation for Qt can be found here: http://qt-project.org/doc/

Documentation for Pyside can be found here: http://qt-project.org/wiki/PySideDocumentation

Documentation for PyQt can be found here: http://pyqt.sourceforge.net/Docs/PyQt4/
