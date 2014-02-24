"""
layouts module
---------------


"""

from qteasylayout.qt import QtGui, Qt

def hbox(*args, add_spacer=False):
    """
    Automatically layouts out the widgets passed in as *args in a QHBoxLayout.  Optionally
    adds a spacer at the end.
    :param QWidget *args: the widgets to arrange in a horizontal layout
    :param bool add_spacer: if True a spacer is added at the end

    Example:
        >>> from qteasylayout import QtGui
        >>> qapp = QtGui.QApplication(['test'])
        >>> label = QtGui.QLabel('A label')
        >>> btn = QtGui.QPushButton('Push me')
        >>> editor = QtGui.QLineEdit('editing')
        >>> w = hbox(label, btn, editor)
        >>> mw = QtGui.QMainWindow()
        >>> mw.setCentralWidget(w)
        >>> mw.show()
        >>> qapp.exec_()
        0
    """
    widget = QtGui.QWidget()
    layout = QtGui.QHBoxLayout(widget)
    widget.setLayout(layout)
    for w in args:
        w.setParent(widget)
        layout.addWidget(w)

    if add_spacer:
        spacer = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        layout.addItem(spacer)

    return widget


def vbox(*args, add_spacer=False):
    """
    Automatically layouts out the widgets passed in as *args in a QVBoxLayout.  Optionally
    adds a spacer at the end
    :param QWidget *args: the widgets to arrange in a vertical layout
    :param bool add_spacer: if True a spacer is added at the bottom

    Example:
        >>> qapp = QtGui.QApplication(['test'])
        >>> label = QtGui.QLabel('A label')
        >>> btn = QtGui.QPushButton('Push me')
        >>> editor = QtGui.QLineEdit('editing')
        >>> w = vbox(label, btn, editor)
        >>> mw = QtGui.QMainWindow()
        >>> mw.setCentralWidget(w)
        >>> mw.show()
        >>> from qteasylayout import QtGui
        >>> qapp.exec_()
        0
    """

    widget = QtGui.QWidget()
    layout = QtGui.QVBoxLayout(widget)
    widget.setLayout(layout)
    for w in args:
        layout.addWidget(w)

    if add_spacer:
        spacer = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        layout.addItem(spacer)

    return widget

def stack(*args):
    """
    Arranges the passed in QWidgets in a stacked layout.  This is similar to a
    tab widget, but the switching must be done using another widget which calls
    the QStackWidget's setCurrentIndex function
    :param *args: the widgets to place in a stacked layout
    :returns: a stacked widget and the slot to call to set the current displayed item

    Example:
        >>> from qteasylayout import QtGui
        >>> qapp = QtGui.QApplication(['test'])
        >>> label = QtGui.QLabel('A label')
        >>> btn = QtGui.QPushButton('Push me')
        >>> editor = QtGui.QLineEdit('editing')
        >>> w = stack(label, btn, editor)

        >>> cb = QtGui.QComboBox()  # the combo box will control which widget is viewable
        >>> cb.addItems(['Label', 'Button', 'Line Edit'])
        >>> cb.activated.connect(w.setCurrentIndex)

        >>> w_outer = vbox(cb, w)
        >>> mw = QtGui.QMainWindow()
        >>> mw.setCentralWidget(w_outer)
        >>> mw.show()
        >>> qapp.exec_()
        0
    """

    stack_widget = QtGui.QStackedWidget()

    for w in args:
        stack_widget.addWidget(w)

    return stack_widget

def grid(grid_items):
    """
    Arranges the items in grid_items in a QGridLayout.  grid_items should be a
    nested list where each inner list is a row if QWidgets

    Example:
        >>> from qteasylayout import QtGui
        >>> qapp = QtGui.QApplication(['test'])
        >>> mw = QtGui.QMainWindow()
        >>> #
        >>> label = QtGui.QLabel('A label')
        >>> btn = QtGui.QPushButton('Push me')
        >>> editor = QtGui.QLineEdit('editing')
        >>> #
        >>> label2 = QtGui.QLabel('A label 2')
        >>> btn2 = QtGui.QPushButton('Push me 2')
        >>> editor2 = QtGui.QLineEdit('editing 2')
        >>> #
        >>> label3 = QtGui.QLabel('A label 3')
        >>> btn3 = QtGui.QPushButton('Push me 3')
        >>> editor3 = QtGui.QLineEdit('editing 3')
        >>> #
        >>> w3 = grid([[label, btn, editor],
        ...          [label2, btn2, editor2],
        ...          [label3, btn3, editor3]])
        >>> #
        >>> mw.setCentralWidget(w3)
        >>> mw.setWindowTitle('Grid Example')
        >>> mw.show()
        >>> qapp.exec_()
        0

    """
    widget = QtGui.QWidget()
    layout = QtGui.QGridLayout(widget)
    widget.setLayout(layout)

    for irow, row in enumerate(grid_items):
        for icol, item in enumerate(row):
            layout.addWidget(item, irow, icol)

    return widget


def hsplit(left, right, parent=None):
    """
    Arranges the left and right widgets in a horizontal splitter
    """

    splitter = QtGui.QSplitter(Qt.Horizontal)
    left.setParent(splitter)
    right.setParent(splitter)
    splitter.addWidget(left)
    splitter.addWidget(right)

    return splitter

def vsplit(top, bottom, parent=None):
    """
    Arranges the top and bottom widgets in a vertical splitter
    """
    splitter = QtGui.QSplitter(Qt.Vertical)
    top.setParent(splitter)
    bottom.setParent(splitter)
    splitter.addWidget(top)
    splitter.addWidget(bottom)

    return splitter


if __name__ == "__main__":
    import doctest
    doctest.testmod()