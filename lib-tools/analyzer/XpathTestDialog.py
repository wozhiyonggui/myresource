# -*- coding: UTF-8 -*-
"""

"""
__author__ = 'howtoesc@gmail.com'

import sys
import PyQt4
from Ui_XpathTestDialog import Ui_XpathTestDialog
from PyQt4 import QtGui, QtCore
from lxml import etree
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..\\")))
from lib.common import *
from LCS import diff
import MainWindow


class XpathTestDialog(QtGui.QDialog, Ui_XpathTestDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        # self.tableWidget_project.horizontalHeader().setDefaultSectionSize(180)

    def et2tw(self, n, t):
        if isinstance(t, QtGui.QTreeWidget):
            ti = QtGui.QTreeWidgetItem(t)
        else:
            ti = QtGui.QTreeWidgetItem()
            t.addChild(ti)

        ti.setText(0, n.tag)
        ti.setText(1, '/'.join([k + ':' + v for k, v in list(n.attrib.iteritems())[:-1]]))

        for c in n:
            self.et2tw(c, ti)

        return ti

    @PyQt4.QtCore.pyqtSlot()
    def on_test_xpath_pressed(self):
        self.treeWidget.clear()
        try:
            r, i = get_node_by_path(get_engine(),MainWindow.MainWindow.qstos(self.xpath.text()))
            for rr in r:
                self.et2tw(rr, self.treeWidget)
            self.treeWidget.expandAll()
        except etree.XPathEvalError as e:
            ti = QtGui.QTreeWidgetItem(self.treeWidget)
            ti.setText(0, unicode(e))
