# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


# class ListWidget(QtWidgets.QListWidget):
#     def findSel(self, current):
#         print('slkdfjl')
#         currentItem = self.itemWidget(current)
#         pixmap = currentItem.pixmap()
#         print (pixmap)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("ECNU图片匹配 V1.0")
        Form.resize(928, 568)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setIconSize(QtCore.QSize(500,300 ))  # Icon 大小
        self.listWidget.setMovement(QtWidgets.QListView.Static)  # Listview显示状态
        # self.listWidget.setMaximumWidth(800)  #
        self.listWidget.setSpacing(12)  # 间距大小

        self.horizontalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(Form.openimage)
        self.lineEdit.editingFinished.connect(Form.picnum)
        self.pushButton.clicked.connect(Form.loadpicpath)
        self.pushButton_5.clicked.connect(Form.startsearch)
        # self.listWidget.itemClicked.connect(ListWidget.findSel)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "导入图片库"))
        self.pushButton_4.setText(_translate("Form", "选择图片"))
        self.label.setText(_translate("Form", "  请输入匹配张数:"))
        self.lineEdit.setText(_translate("Form", "10"))
        self.pushButton_5.setText(_translate("Form", "搜索"))

