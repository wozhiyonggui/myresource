# -*- coding: UTF-8 -*-
"""

"""
__author__ = 'howtoesc@gmail.com'

import sys
import PyQt4
from Ui_MainWindow import Ui_MainWindow
from PyQt4 import QtGui, QtCore
from lxml import etree
from LCS import diff
import time, os

import XpathTestDialog
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..\\")))
from lib.common import *



def save_wt_dump(f):
    f.write(etree.tostring(etree.fromstring(get_wt_dump(get_engine())), method='xml', pretty_print=True))


def load_wt_dump(f):
    r, n = treetraverse(etree.parse(f).getroot())
    return n


def get_node_by_path(engine,x, t=1):
    for i in range(0, t):
        r = treetraverse(etree.fromstring(get_wt_dump(engine)))[1].xpath(x)
        if r is not None:
            return (r, i)
        else:
            time.sleep(1)
    return (None, t)

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.tableWidget_project.horizontalHeader().setDefaultSectionSize(180)

        self.et = etree.Element('ztgt-scene-analyse')
        self.et.append(etree.Element('project', name='', path='', full_path=''))

        self.left, self.right = ('', '')
        self.ln, self.rn = (None, None)

        self.WindowTitle = ['project', '', '[', '', '] ztgt-scene-analyse']

        self.setWindowTitle(' '.join(self.WindowTitle))

        self.treeWidget_left.verticalScrollBar().valueChanged.connect(
            self.treeWidget_right.verticalScrollBar().setValue)
        self.treeWidget_right.verticalScrollBar().valueChanged.connect(
            self.treeWidget_left.verticalScrollBar().setValue)

    @staticmethod
    def qstos(s):
        return unicode(s.toUtf8(), encoding="UTF-8")

    def _update_windows_title(self):
        if len(self.et.find('project').attrib['full_path']) < 60:
            p = self.et.find('project').attrib['full_path']
        else:
            p = u'{0} ... {1}'.format(self.et.find('project').attrib['full_path'][0:30],
                                      self.et.find('project').attrib['full_path'][-30:])

        self.setWindowTitle(
            u'{0} - [{1}] -  ztgt-scene-analyse'.format(self.et.find('project').attrib['name'], p))

    def _get_ready(self):
        self.action_new.setEnabled(False)
        self.action_open.setEnabled(False)

        self.action_del_scene.setEnabled(True)
        self.action_dump_scene.setEnabled(True)

        self.action_left.setEnabled(True)
        self.action_right.setEnabled(True)

        self.action_test_xpath.setEnabled(True)

    def _get_select(self):
        if -1 == self.tableWidget_project.currentRow():
            QtGui.QMessageBox.information(self, u'info', u'请选择场景')
            return None

        return self.tableWidget_project.item(self.tableWidget_project.currentRow(), 0)

    @PyQt4.QtCore.pyqtSlot()
    def on_action_new_triggered(self):
        s, t = QtGui.QInputDialog.getText(self, u'请输入项目名', u'项目名')

        if not t or s == '':
            return

        self.et.clear()
        self.et.append(etree.Element('project', isSaved='False', name=self.qstos(s), path='', full_path=''))

        self._save()
        self._get_ready()

    @PyQt4.QtCore.pyqtSlot()
    def on_action_open_triggered(self):
        f = QtGui.QFileDialog.getOpenFileName(self, u'请选择项目文件', './', 'XML (*.xml)')

        if not f:
            return

        self.et = etree.parse(open(self.qstos(f), 'r')).getroot()

        self._update_windows_title()

        s = self.et.find('scenes')

        if s is None:
            return

        self.tableWidget_project.clearContents()
        self.tableWidget_project.setRowCount(len(s))

        for i in range(0, len(s)):
            self.tableWidget_project.setItem(i, 0, QtGui.QTableWidgetItem(s[i].tag))

        self._get_ready()

    def _save(self):
        # New Project
        if not self.et.find('project').get('path'):
            d = QtGui.QFileDialog.getExistingDirectory(self, u'请选择项目需要保存的目录')

            if d:
                self.et.find('project').attrib['path'] = self.qstos(d)
                self.et.find('project').attrib['full_path'] = self.qstos(d) + '/' + self.et.find('project').attrib[
                    'name'] + u'-project.xml'
            else:
                return

        if self.et.find('scenes') is None:
            self.et.append(etree.Element('scenes'))
        else:
            self.et.find('scenes').clear()

        for i in range(0, self.tableWidget_project.rowCount()):
            self.et.find('scenes').append(etree.Element(self.qstos(self.tableWidget_project.item(i, 0).text())))

        try:
            etree.ElementTree(self.et).write(
                open(self.et.find('project').attrib['full_path'], 'w'), pretty_print=True, encoding='UTF-8')
        except IOError as e:
            # TODO:add error box
            QtGui.QMessageBox.information(self, u'info', u'保存失败:{}{}'.format(e.errno, e.strerror))

        self._update_windows_title()

    @PyQt4.QtCore.pyqtSlot()
    def on_action_dump_scene_triggered(self):
        tf = u'{0}/{1}'.format(self.et.find('project').attrib['path'], time.time())
        save_wt_dump(open(tf, 'w'))

        if not os.path.exists(tf) or not os.path.getsize(tf):
            QtGui.QMessageBox.information(self, u'info', u'Dump失败')
            return

        s, t = ('', None)
        while 1:
            s, t = QtGui.QInputDialog.getText(self, u'请输入场景名', u'场景名', QtGui.QLineEdit.Normal, s)

            if not t or s == '':
                return

            if 0 < len(self.tableWidget_project.findItems(s, QtCore.Qt.MatchExactly)):
                QtGui.QMessageBox.information(self, u'info', u'禁止场景名重名')
                continue
            else:
                break

        n = self.tableWidget_project.currentRow()

        if -1 == n:
            n = self.tableWidget_project.rowCount()
        else:
            n += 1

        self.tableWidget_project.insertRow(n)

        self.tableWidget_project.setItem(n, 0, QtGui.QTableWidgetItem(s))

        self._save()

        os.rename(tf, u'{0}/{1}-dump.xml'.format(self.et.find('project').attrib['path'], self.qstos(s)))

    @PyQt4.QtCore.pyqtSlot()
    def on_action_del_scene_triggered(self):
        a = self._get_select()

        if not a:
            return

        reply = QtGui.QMessageBox.question(self, 'info', u'确认删除{}?'.format(a.text()),
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.tableWidget_project.removeRow(self.tableWidget_project.currentRow())
            self._save()
        else:
            return

    @staticmethod
    def clone_ghost_tree(n):
        g = etree.Element('_')
        g.attrib['__diff__'] = 'T-'
        for c in n:
            g.append(MainWindow.clone_ghost_tree(c))
        return g

    @staticmethod
    def cmp_attrib(ln, rn):
        if ln.attrib != rn.attrib:
            ln.attrib['__diff__'] = 'A'
            rn.attrib['__diff__'] = 'A'
        else:
            ln.attrib['__diff__'] = 'O'
            rn.attrib['__diff__'] = 'O'

    @staticmethod
    def set_tree_tplus(n):
        n.attrib['__diff__'] = 'T+'
        for c in n:
            MainWindow.set_tree_tplus(c)

    @staticmethod
    def diff_tree(ln, rn):
        w = diff([e.tag for e in ln], [e.tag for e in rn])

        # for i in w:
        for i in range(0, len(w)):
            if '=' == w[i]:
                MainWindow.cmp_attrib(ln[i], rn[i])
                MainWindow.diff_tree(ln[i], rn[i])

            elif '-' == w[i]:
                rn.insert(i, MainWindow.clone_ghost_tree(ln[i]))
                MainWindow.set_tree_tplus(ln[i])
            elif '+' == w[i]:
                ln.insert(i, MainWindow.clone_ghost_tree(rn[i]))
                MainWindow.set_tree_tplus(rn[i])
            else:
                pass

    cls = {'T+': QtCore.Qt.green,
           'T-': QtCore.Qt.darkGreen,
           'A': QtCore.Qt.yellow}

    @staticmethod
    def et2tw(n, t):
        if isinstance(t, QtGui.QTreeWidget):
            ti = QtGui.QTreeWidgetItem(t)
        else:
            ti = QtGui.QTreeWidgetItem()
            t.addChild(ti)

        if n.attrib['__diff__'] != 'T-':
            ti.setText(0, n.tag)

        ti.setText(1, '/'.join([k + ':' + v for k, v in list(n.attrib.iteritems())[:-1]]))

        if n.attrib['__diff__'] != 'O':
            cl = MainWindow.cls[n.attrib['__diff__']]
            ti.setBackground(0, cl)
            ti.setBackground(1, cl)

        for c in n:
            MainWindow.et2tw(c, ti)

        return ti

    def _diff_display(self):

        if self.left == '' or self.rn == '':
            return

        self.rn = load_wt_dump(
            open(self.et.find('project').attrib['path'] + u'/' + self.right + u'-dump.xml', 'r'))
        self.ln = load_wt_dump(
            open(self.et.find('project').attrib['path'] + u'/' + self.left + u'-dump.xml', 'r'))

        self.diff_tree(self.ln, self.rn)
        self.ln.attrib['__diff__'] = 'O'
        self.rn.attrib['__diff__'] = 'O'

        self.treeWidget_left.clear()
        self.treeWidget_right.clear()

        self.et2tw(self.ln, self.treeWidget_left)
        self.treeWidget_left.expandAll()
        self.et2tw(self.rn, self.treeWidget_right)
        self.treeWidget_right.expandAll()

    @PyQt4.QtCore.pyqtSlot()
    def on_action_left_triggered(self):
        a = self._get_select()

        if not a:
            return

        self.left = self.qstos(a.text())
        self.treeWidget_left.setHeaderLabel(a.text())

        if not self.right:
            self.on_action_right_triggered()
            return

        self._diff_display()

    @PyQt4.QtCore.pyqtSlot()
    def on_action_right_triggered(self):
        a = self._get_select()

        if not a:
            return

        self.right = self.qstos(a.text())
        self.treeWidget_right.setHeaderLabel(a.text())

        if not self.left:
            self.on_action_left_triggered()
            return

        self._diff_display()

    def _get_fathers(self, i):
        if not i.parent():
            return ''
        return self._get_fathers(i.parent()) + '/' + i.parent().text(0)

    @PyQt4.QtCore.pyqtSlot()
    def on_treeWidget_right_itemSelectionChanged(self):
        i = self.treeWidget_right.currentItem()
        self.lineEdit_r.setText(self._get_fathers(i) + '/' + i.text(0) + ':' + i.text(1))
        self.lineEdit_r.home(False)

    @PyQt4.QtCore.pyqtSlot()
    def on_treeWidget_left_itemSelectionChanged(self):
        i = self.treeWidget_left.currentItem()
        self.lineEdit_l.setText(self._get_fathers(i) + '/' + i.text(0) + ':' + i.text(1))
        self.lineEdit_l.home(False)

    @PyQt4.QtCore.pyqtSlot()
    def on_action_test_xpath_triggered(self):
        d = XpathTestDialog.XpathTestDialog()
        d.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
