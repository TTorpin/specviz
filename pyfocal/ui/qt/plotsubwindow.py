# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './source/plotsubwindow.ui'
#
# Created by: ...third_party.qtpy UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from ...third_party.qtpy import QtCore, QtGui, QtWidgets

class Ui_SpectraSubWindow(object):
    def setupUi(self, SpectraSubWindow):
        SpectraSubWindow.setObjectName("SpectraSubWindow")
        SpectraSubWindow.resize(800, 600)
        SpectraSubWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(SpectraSubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        SpectraSubWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SpectraSubWindow)
        self.statusbar.setObjectName("statusbar")
        SpectraSubWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(SpectraSubWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        SpectraSubWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionInsert_ROI = QtWidgets.QAction(SpectraSubWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Rectangle Stroked-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsert_ROI.setIcon(icon)
        self.actionInsert_ROI.setObjectName("actionInsert_ROI")
        self.actionPlot_Settings = QtWidgets.QAction(SpectraSubWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Settings 3-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot_Settings.setIcon(icon1)
        self.actionPlot_Settings.setObjectName("actionPlot_Settings")
        self.actionGraph_Settings = QtWidgets.QAction(SpectraSubWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/Settings-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGraph_Settings.setIcon(icon2)
        self.actionGraph_Settings.setObjectName("actionGraph_Settings")
        self.toolBar.addAction(self.actionInsert_ROI)
        self.toolBar.addSeparator()

        self.retranslateUi(SpectraSubWindow)
        QtCore.QMetaObject.connectSlotsByName(SpectraSubWindow)

    def retranslateUi(self, SpectraSubWindow):
        _translate = QtCore.QCoreApplication.translate
        self.toolBar.setWindowTitle(_translate("SpectraSubWindow", "toolBar"))
        self.actionInsert_ROI.setText(_translate("SpectraSubWindow", "Rectangle ROI"))
        self.actionInsert_ROI.setToolTip(_translate("SpectraSubWindow", "Insert a rectangular ROI selection box"))
        self.actionPlot_Settings.setText(_translate("SpectraSubWindow", "Plot Settings"))
        self.actionPlot_Settings.setToolTip(_translate("SpectraSubWindow", "Edit plot settings"))
        self.actionGraph_Settings.setText(_translate("SpectraSubWindow", "Graph Settings"))
        self.actionGraph_Settings.setToolTip(_translate("SpectraSubWindow", "Edit graph settings"))

from . import icon_resource_rc
