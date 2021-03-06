import  sys
from PyQt5.QtWidgets import QMainWindow,QApplication

#图标
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        #设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")
        #设置窗口的尺寸
        self.resize(400,300)

        #获得状态栏
        self.status=self.statusBar()
        #显示消息
        self.status.showMessage("只存在5秒的消息",-1)


if __name__=="__main__":

    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon("frog.jpg"))
    main=FirstMainWin()
    main.show()
    sys.exit(app.exec_())

