"""
layouts module
---------------


"""

from qt_easy_layout.qt import qti
from qt_easy_layout.custom_layouts import FlowLayout

def hbox(*args, margin=2, add_spacer=False):
    """
    Automatically layouts out the widgets passed in as *args in a QHBoxLayout.  Optionally
    adds a spacer at the end.
    :param QWidget *args: the widgets to arrange in a horizontal layout
    :param bool add_spacer: if True a spacer is added at the end

    Example:
        >>> from qt_easy_layout import qti
        >>> qapp = qti.QtGui.QApplication(['test'])
        >>> label = qti.QtGui.QLabel('A label')
        >>> btn = qti.QtGui.QPushButton('Push me')
        >>> editor = qti.QtGui.QLineEdit('editing')
        >>> w = hbox(label, btn, editor)
        >>> mw = qti.QtGui.QMainWindow()
        >>> mw.setCentralWidget(w)
        >>> mw.show()
        >>> qapp.exec_()
        0
    """
    widget = qti.QtGui.QWidget()
    layout = qti.QtGui.QHBoxLayout(widget)
    try:
        layout.setMargin(margin)
    except:
        layout.setContentsMargins(margin, margin, margin, margin)
    widget.setLayout(layout)
    for w in args:
        w.setParent(widget)
        layout.addWidget(w)

    if add_spacer:
        spacer = qti.QtGui.QSpacerItem(40, 20,
                                      qti.QtGui.QSizePolicy.Expanding,
                                      qti.QtGui.QSizePolicy.Minimum)
        layout.addItem(spacer)

    return widget


def vbox(*args, margin=2, add_spacer=False):
    """
    Automatically layouts out the widgets passed in as *args in a QVBoxLayout.  Optionally
    adds a spacer at the end
    :param QWidget *args: the widgets to arrange in a vertical layout
    :param bool add_spacer: if True a spacer is added at the bottom

    Example:
        >>> from qt_easy_layout import qti
        >>> qapp = qti.QtGui.QApplication(['test'])
        >>> label = qti.QtGui.QLabel('A label')
        >>> btn = qti.QtGui.QPushButton('Push me')
        >>> editor = qti.QtGui.QLineEdit('editing')
        >>> w = vbox(label, btn, editor)
        >>> mw = qti.QtGui.QMainWindow()
        >>> mw.setCentralWidget(w)
        >>> mw.show()
        >>> qapp.exec_()
        0
    """

    widget = qti.QtGui.QWidget()
    layout = qti.QtGui.QVBoxLayout(widget)
    try:
        layout.setMargin(margin)
    except:
        layout.setContentsMargins(margin, margin, margin, margin)
    widget.setLayout(layout)

    for w in args:
        layout.addWidget(w)

    if add_spacer:
        spacer = qti.QtGui.QSpacerItem(20, 40,
                                      qti.QtGui.QSizePolicy.Minimum,
                                      qti.QtGui.QSizePolicy.Maximum)
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
        >>> from qt_easy_layout import QtGui
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

    stack_widget = qti.QtGui.QStackedWidget()

    for w in args:
        stack_widget.addWidget(w)

    return stack_widget

def grid(grid_items, margin=2):
    """
    Arranges the items in grid_items in a QGridLayout.  grid_items should be a
    nested list where each inner list is a row if QWidgets

    Example:
        >>> from qt_easy_layout import qti
        >>> qapp = qti.QtGui.QApplication(['test'])
        >>> mw = qti.QtGui.QMainWindow()
        >>> #
        >>> label = qti.QtGui.QLabel('A label')
        >>> btn = qti.QtGui.QPushButton('Push me')
        >>> editor = qti.QtGui.QLineEdit('editing')
        >>> #
        >>> label2 = qti.QtGui.QLabel('A label 2')
        >>> btn2 = qti.QtGui.QPushButton('Push me 2')
        >>> editor2 = qti.QtGui.QLineEdit('editing 2')
        >>> #
        >>> label3 = qti.QtGui.QLabel('A label 3')
        >>> btn3 = qti.QtGui.QPushButton('Push me 3')
        >>> editor3 = qti.QtGui.QLineEdit('editing 3')
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
    widget = qti.QtGui.QWidget()
    layout = qti.QtGui.QGridLayout(widget)
    try:
        layout.setMargin(margin)
    except:
        layout.setContentsMargins(margin, margin, margin, margin)
    widget.setLayout(layout)

    for irow, row in enumerate(grid_items):
        for icol, item in enumerate(row):
            layout.addWidget(item, irow, icol)

    return widget


def hsplit(left, right, parent=None):
    """
    Arranges the left and right widgets in a horizontal splitter
    """

    splitter = qti.QtGui.QSplitter(qti.Qt.Horizontal)
    left.setParent(splitter)
    right.setParent(splitter)
    splitter.addWidget(left)
    splitter.addWidget(right)

    return splitter

def vsplit(top, bottom, parent=None, splitter=None):
    """
    Arranges the top and bottom widgets in a vertical splitter
    """
    if splitter is None:
        splitter = qti.QtGui.QSplitter(qti.Qt.Vertical)
    top.setParent(splitter)
    bottom.setParent(splitter)
    splitter.addWidget(top)
    splitter.addWidget(bottom)

    return splitter


def flow(*args, margin=2):
    """
    Automatically layouts out the widgets passed in as *args in a QVBoxLayout.  Optionally
    adds a spacer at the end
    :param QWidget *args: the widgets to arrange in a vertical layout
    :param bool add_spacer: if True a spacer is added at the bottom

    Example:
        >>> qapp = qti.QtGui.QApplication(['test'])
        >>> label = qti.QtGui.QLabel('A label')
        >>> btn = qti.QtGui.QPushButton('Push me')
        >>> editor = qti.QtGui.QLineEdit('editing')
        >>> w = vbox(label, btn, editor)
        >>> mw = qti.QtGui.QMainWindow()
        >>> mw.setCentralWidget(w)
        >>> mw.show()
        >>> qapp.exec_()
        0
    """

    widget = qti.QtGui.QWidget()
    layout = FlowLayout(widget)
    try:
        layout.setMargin(margin)
    except:
        layout.setContentsMargins(margin, margin, margin, margin)
    widget.setLayout(layout)

    for w in args:
        layout.addWidget(w)

    return widget


if __name__ == "__main__":
    import doctest
    doctest.testmod()