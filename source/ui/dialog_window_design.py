# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_window_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogWindow(object):
    def setupUi(self, DialogWindow):
        DialogWindow.setObjectName("DialogWindow")
        DialogWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogWindow.resize(216, 62)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogWindow.sizePolicy().hasHeightForWidth())
        DialogWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(DialogWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 6, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.IconButton = QtWidgets.QPushButton(self.centralwidget)
        self.IconButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconButton.sizePolicy().hasHeightForWidth())
        self.IconButton.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icons/exclamation.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.IconButton.setIcon(icon)
        self.IconButton.setIconSize(QtCore.QSize(48, 48))
        self.IconButton.setObjectName("IconButton")
        self.horizontalLayout_2.addWidget(self.IconButton)
        spacerItem = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.InfoLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoLabel.sizePolicy().hasHeightForWidth())
        self.InfoLabel.setSizePolicy(sizePolicy)
        self.InfoLabel.setObjectName("InfoLabel")
        self.horizontalLayout_2.addWidget(self.InfoLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.AcceptButton = QtWidgets.QPushButton(self.centralwidget)
        self.AcceptButton.setObjectName("AcceptButton")
        self.horizontalLayout.addWidget(self.AcceptButton)
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        DialogWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DialogWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogWindow)

    def retranslateUi(self, DialogWindow):
        _translate = QtCore.QCoreApplication.translate
        DialogWindow.setWindowTitle(_translate("DialogWindow", "MainWindow"))
        self.InfoLabel.setText(_translate("DialogWindow", "TextLabel"))
        self.AcceptButton.setText(_translate("DialogWindow", "Yes"))
        self.CancelButton.setText(_translate("DialogWindow", "No"))
import resources.resources_rc