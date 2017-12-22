"""
layouts module
---------------


"""

from qtpy import QtCore, QtWidgets

from qtlayout.custom_layouts import FlowLayout

Qt = QtCore.Qt


def __set_margin(widget, margin):
    try:
        widget.setMargin(margin)
    except AttributeError:
        widget.setContentsMargins(margin, margin, margin, margin)


def hbox(*args, margin=2, widget=None, add_spacer=False):
    """
    Automatically layouts out the widgets passed in as *args in a QHBoxLayout.  Optionally
    adds a spacer at the end.
    :param QWidget *args: the widgets to arrange in a horizontal layout
    :param int margin: the margin for the layout
    :param bool add_spacer: if True a spacer is added at the end

    Example:
        >>> qapp = QtWidgets.QApplication(['hbox layout test'])
        >>> label = QtWidgets.QLabel('A label')
        >>> btn = QtWidgets.QPushButton('Push me')
        >>> editor = QtWidgets.QLineEdit('editing')
        >>> w = hbox(label, btn, editor)
        >>> mw = QtWidgets.QMainWindow()
        >>> mw.setCentralWidget(w)
        >>> mw.setWindowTitle('hbox Example')
        >>> mw.show()
        >>> qapp.exec_()
        0
    """
    if widget is None:
        widget = QtWidgets.QWidget()

    layout = QtWidgets.QHBoxLayout(widget)
    __set_margin(layout, margin)
    widget.setLayout(layout)
    for w in args:
        try:
            w.setParent(widget)
        except AttributeError:
            pass
        try:
            layout.addWidget(w)
        except TypeError:
            layout.addItem(w)

    if add_spacer:
        spacer = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        layout.addItem(spacer)

    return widget


def vbox(*args, margin=2, widget=None, add_spacer=False):
    """
    Automatically layouts out the widgets passed in as *args in a QVBoxLayout.  Optionally
    adds a spacer at the end
    :param QWidget *args: the widgets to arrange in a vertical layout
    :param bool add_spacer: if True a spacer is added at the bottom

    Example:
        >>> qapp = QtWidgets.QApplication(['vbox layout test'])
        >>> label = QtWidgets.QLabel('A label')
        >>> btn = QtWidgets.QPushButton('Push me')
        >>> editor = QtWidgets.QLineEdit('editing')
        >>> w = vbox(label, btn, editor)
        >>> mw = QtWidgets.QMainWindow()
        >>> mw.setCentralWidget(w)
        >>> mw.setWindowTitle('vbox Example')
        >>> mw.show()
        >>> qapp.exec_()
        0
    """

    if widget is None:
        widget = QtWidgets.QWidget()

    layout = QtWidgets.QVBoxLayout(widget)
    __set_margin(layout, margin=margin)
    widget.setLayout(layout)

    for w in args:
        try:
            w.setParent(widget)
        except AttributeError:
            pass
        try:
            layout.addWidget(w)
        except TypeError:
            layout.addItem(w)

    if add_spacer:
        spacer = QtWidgets.QSpacerItem(
            20, 40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        layout.addItem(spacer)

    setattr(widget, 'items', args)

    return widget


def stack(*args):
    """
    Arranges the passed in QWidgets in a stacked layout.  This is similar to a
    tab widget, but the switching must be done using another widget which calls
    the QStackWidget's setCurrentIndex function
    :param *args: the widgets to place in a stacked layout
    :returns: a stacked widget and the slot to call to set the current displayed item

    Example:
        >>> qapp = QtWidgets.QApplication(['stack layout test'])
        >>> label = QtWidgets.QLabel('A label')
        >>> btn = QtWidgets.QPushButton('Push me')
        >>> editor = QtWidgets.QLineEdit('editing')
        >>> w = stack(label, btn, editor)

        >>> cb = QtWidgets.QComboBox()  # the combo box will control which widget is viewable
        >>> cb.addItems(['Label', 'Button', 'Line Edit'])
        >>> cb.activated.connect(w.setCurrentIndex)

        >>> w_outer = vbox(cb, w)
        >>> mw = QtWidgets.QMainWindow()
        >>> mw.setCentralWidget(w_outer)
        >>> mw.setWindowTitle('stack Example')
        >>> mw.show()
        >>> qapp.exec_()
        0
    """

    stack_widget = QtWidgets.QStackedWidget()

    for w in args:
        stack_widget.addWidget(w)

    return stack_widget


def grid(grid_items, margin=2):
    """
    Arranges the items in grid_items in a QGridLayout.  grid_items should be a
    nested list where each inner list is a row if QWidgets

    Example:
        >>> qapp = QtWidgets.QApplication(['grid layout test'])
        >>> mw = QtWidgets.QMainWindow()
        >>> #
        >>> label = QtWidgets.QLabel('A label')
        >>> btn = QtWidgets.QPushButton('Push me')
        >>> editor = QtWidgets.QLineEdit('editing')
        >>> #
        >>> label2 = QtWidgets.QLabel('A label 2')
        >>> btn2 = QtWidgets.QPushButton('Push me 2')
        >>> editor2 = QtWidgets.QLineEdit('editing 2')
        >>> #
        >>> label3 = QtWidgets.QLabel('A label 3')
        >>> btn3 = QtWidgets.QPushButton('Push me 3')
        >>> editor3 = QtWidgets.QLineEdit('editing 3')
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
    widget = QtWidgets.QWidget()
    layout = QtWidgets.QGridLayout(widget)
    # layout.setMargin(margin)
    __set_margin(layout, margin)
    widget.setLayout(layout)

    for irow, row in enumerate(grid_items):
        for icol, item in enumerate(row):
            layout.addWidget(item, irow, icol)

    return widget


def hsplit(left, right, parent=None, left_percent=0.5):
    """
    Arranges the left and right widgets in a horizontal splitter
    """

    splitter = QtWidgets.QSplitter(Qt.Horizontal)
    left.setParent(splitter)
    right.setParent(splitter)
    splitter.addWidget(left)
    splitter.addWidget(right)
    splitter.setSizes([int(left_percent*100), 100-int(left_percent*100)])
    return splitter


def vsplit(top, bottom, parent=None, splitter=None):
    """
    Arranges the top and bottom widgets in a vertical splitter
    """
    if splitter is None:
        splitter = QtWidgets.QSplitter(Qt.Vertical)
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
        >>> qapp = QtWidgets.QApplication(['flow layout test'])
        >>> label = QtWidgets.QLabel('A label')
        >>> btn = QtWidgets.QPushButton('Push me')
        >>> editor = QtWidgets.QLineEdit('editing')
        >>> w = flow(label, btn, editor)
        >>> mw = QtWidgets.QMainWindow()
        >>> mw.setCentralWidget(w)
        >>> mw.setWindowTitle('flow Example')
        >>> mw.show()
        >>> qapp.exec_()
        0
    """

    widget = QtWidgets.QWidget()
    layout = FlowLayout(widget)
    # layout.setMargin(margin)
    __set_margin(layout, margin)
    widget.setLayout(layout)

    for w in args:
        layout.addWidget(w)

    return widget


def tabs(*args):
    """
    Puts each widget into a tab page of a new QTabWidget.
    Arguments should alternate with widget and widget names

    Example:
        >>> qapp = QtWidgets.QApplication(['tabs layout test'])
        >>> t = tabs((QtWidgets.QPushButton(),'A Button Page'),(QtWidgets.QListWidget(), 'A list Page') )
        >>> mw = QtWidgets.QMainWindow()
        >>> mw.setCentralWidget(t)
        >>> mw.setWindowTitle('tabs Example')
        >>> mw.show()
        >>> qapp.exec_()
        0
    """
    widget = QtWidgets.QTabWidget()
    for child_widget, title in args:
        widget.addTab(child_widget, title)

    return widget


if __name__ == "__main__":
    import doctest
    doctest.testmod()
