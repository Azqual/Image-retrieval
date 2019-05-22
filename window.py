from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtGui import QPixmap
import os

from Form import Ui_Form

class MyWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.picnums = 10
        self.picpath="D:\\Study\\now_First\\Multimedia_Technology\\Practice\\CBIR-images"

    def openimage(self):
        path = QFileDialog.getOpenFileName(self, "选取文件", self.picpath, "All Files (*);;*.jpg;;*.png;;*.bmp;")[0]
        print(path)
        image = QPixmap()
        image.load(path)
        item = QGraphicsPixmapItem(image)  # 创建一个变量用于承载加载后的图片
        self.graphicsView.scene = QGraphicsScene() # 创建一个图片元素的对象
        self.graphicsView.scene.addItem(item)  # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)

    def picnum(self):
        try:
            self.picnums = int(self.lineEdit.text()) # 获取文本框内容
        except:
            pass
        print(self.picnums)

    def loadpicpath(self):
        self.picpath=QFileDialog.getExistingDirectory()
        dirs = os.listdir( self.picpath )
        print(dirs)
        QMessageBox.information(self, "提示信息",
                                      self.tr("您已成功导入图片库"),
                                      QMessageBox.Ok,
                                      QMessageBox.Ok)
    def startsearch(self):
        self.listWidget.clear()
        print('searching...')
        file = ['D:\\Study\\now_First\\Multimedia_Technology\\Practice\\CBIR-images\\001.ak47\\001_000' + str(j + 1) + '.jpg' for j in range(9)]
        file2 = ['D:\\Study\\now_First\\Multimedia_Technology\\Practice\\CBIR-images\\001.ak47\\001_00' + str(j) + '.jpg' for j in range(10,21)]
        file=file+file2
        print(file)
        for i in range(self.picnums):
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap((file[i])), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            self.listWidget.addItem(item)
            print(item.icon())
            print('lskdjf')


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())
