# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_XpathTestDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_XpathTestDialog(object):
    def setupUi(self, XpathTestDialog):
        XpathTestDialog.setObjectName(_fromUtf8("XpathTestDialog"))
        XpathTestDialog.resize(802, 531)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("res/test_xpath.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        XpathTestDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(XpathTestDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.test_xpath = QtGui.QPushButton(XpathTestDialog)
        self.test_xpath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.test_xpath.setObjectName(_fromUtf8("test_xpath"))
        self.gridLayout.addWidget(self.test_xpath, 0, 1, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(XpathTestDialog)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("tag"))
        self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 2)
        self.xpath = QtGui.QLineEdit(XpathTestDialog)
        self.xpath.setObjectName(_fromUtf8("xpath"))
        self.gridLayout.addWidget(self.xpath, 0, 0, 1, 1)

        self.retranslateUi(XpathTestDialog)
        QtCore.QMetaObject.connectSlotsByName(XpathTestDialog)

    def retranslateUi(self, XpathTestDialog):
        XpathTestDialog.setWindowTitle(_translate("XpathTestDialog", "Dialog", None))
        self.test_xpath.setText(_translate("XpathTestDialog", "Test", None))
        self.treeWidget.headerItem().setText(1, _translate("XpathTestDialog", "attrib", None))

