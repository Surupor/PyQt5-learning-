import sys
import MainWinVerticalLayout
import MainWinHorizontalLayout
import MainWinGridLayout
import MainWinHV
import MainWinGrid2Layout
import MainWinSpainLayout
import MainWinSizeHint
import MainWinContainerLayout
import MainWinAbsulteLayout
import MainWinFromlLayout
import MainWinButtonContract
import MainWinSignal_SlotDesigner
import MainWinMeanTool

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    # 水平布局
    # ui = MainWinHorizontalLayout.Ui_MainWindow()
    # 垂直布局
    # ui=MainWinVerticalLayout.Ui_MainWindow()
    #表格布局
    # ui=MainWinGridLayout.Ui_MainWindow()
    # 组合布局
    # ui=MainWinHV.Ui_MainWindow()
    #栅格布局
    # ui=MainWinGrid2Layout.Ui_MainWindow()
    # 表单布局
    # ui=MainWinFromlLayout.Ui_MainWindow()
    # 容器布局
    # ui=MainWinContainerLayout.Ui_MainWindow()
    # 绝对布局
    # ui=MainWinAbsulteLayout.Ui_MainWindow()

    # 分割线
    # ui=MainWinSpainLayout.Ui_MainWindow()

    # 尺寸策略
    # ui=MainWinSizeHint.Ui_MainWindow()

    # 控件之间伙伴关系
    # ui=MainWinButtonContract.Ui_MainWindow()

    #信号与槽机制
    # ui=MainWinSignal_SlotDesigner.Ui_MainWindow()

    # 添加菜单栏和工具栏
    ui=MainWinMeanTool.Ui_MainWindow()


    #向主窗口添加控件
    ui.setupUi(mainwindow)
    # 展示
    mainwindow.show()

    sys.exit(app.exec_())
