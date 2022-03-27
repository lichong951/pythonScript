# 界面支持库安装
# pip install pyqt5

# pip install PyQt5-tools

import sys,os
import time
from PyQt5.QtWidgets import (QWidget
, QProgressBar
, QSlider
,QLabel
,QMainWindow
, QFileDialog
, QTextEdit
,QLineEdit
,QAction
,QHBoxLayout
, QVBoxLayout
, QToolTip
,QMessageBox
, QPushButton
, QApplication)
from PyQt5.QtGui import QFont,QIcon 
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QMovie

import moviepy.editor as mpe

from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5.QtMultimedia import *


# fileList=[]

class Example(QMainWindow):

    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.startTimeValue=0
        self.endTimeValue=0
        self.fpsValue=1
        # 视频预览
        self.player = QMediaPlayer(self)
        self.vw=  QVideoWidget(self)                       # 定义视频显示的widget
        self.vw.setGeometry(20,20,600,600)
        self.vw.show()
        self.player.setVideoOutput(self.vw)                 # 视频播放输出的widget，就是上面定义的
        self.player.positionChanged.connect(self.changeSlide)

        # 播放按钮
        self.btn = QPushButton('play', self)
        self.btn.move(20, 620)
        self.btn.clicked.connect(self.player.play)
        # 暂停按钮
        self.btn = QPushButton('pause', self)
        self.btn.move(120, 620)
        self.btn.clicked.connect(self.player.pause)
        # 停止按钮
        self.btn = QPushButton('stop', self)
        self.btn.move(220, 620)
        self.btn.clicked.connect(self.player.stop)
        # 播放时长
        self.videoPlayDurationLabel = QLabel(self)
        self.videoPlayDurationLabel.setGeometry(320, 620, 100, 40)

        # 开始转换准备
        # 分辨率
        self.startLabel = QLabel(self)
        self.startLabel.setGeometry(640, 10, 260, 40)
        self.startLabel.setText('分辨率：默认尺寸(暂不支持变更)')
        # 开始时间
        self.startLabel = QLabel(self)
        self.startLabel.setGeometry(640, 40, 50, 40)
        self.startLabel.setText('start:')
        # 开始时间值
        startTimeValueLE = QLineEdit(self)
        startTimeValueLE.move(680, 40)
        startTimeValueLE.textChanged[str].connect(self.onChangedOfStartTime)
        startTimeValueLE.setText(str(self.startTimeValue))

        # 结束时间
        self.startLabel = QLabel(self)
        self.startLabel.setGeometry(640, 80, 50, 40)
        self.startLabel.setText('end:')
        self.endTimeValueLE = QLineEdit(self)
        self.endTimeValueLE.move(680, 80)
        self.endTimeValueLE.textChanged[str].connect(self.onChangedOfEndTime)
        self.endTimeValueLE.setText(str(self.endTimeValue))
        
        # FPS
        self.fpsLabel = QLabel(self)
        self.fpsLabel.setGeometry(640, 120, 50, 40)
        self.fpsLabel.setText('fps:')
        fpsValueLE = QLineEdit(self)
        fpsValueLE.move(680, 120)
        fpsValueLE.textChanged[str].connect(self.onChangedOfFPS)
        fpsValueLE.setText(str(self.fpsValue))

        # 转换
        self.btn = QPushButton('转换gif', self)
        self.btn.move(640, 160)
        self.btn.clicked.connect(self.transformToGif)

        # gif的文件名称
        self.gifFileNameLable=QLabel(self)
        self.gifFileNameLable.setGeometry(640, 190, 200, 60)
        # self.gifFileNameLable.setText('xxxx.gif')
        # Gif的文件大小
        self.gifSizeLable=QLabel(self)
        self.gifSizeLable.move(640,230)
        # self.gifSizeLable.setText('0KB')


        # 导出

        #预览

        # self.pbar = QProgressBar(self)
        # self.pbar.setGeometry(30, 100, 200, 25)
 
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile) 

        self.label = QLabel(self)
        self.label.setGeometry(800, 20, 400, 500)
        self.label.setScaledContents(True)
       
        self.setGeometry(0, 0, 1300, 900)
        self.setWindowTitle('视频转Gif动图')    
        self.show()
    def changeSlide(self, position):
        self.vidoeLength = self.player.duration() + 0.1
        print(self.vidoeLength)

        # self.sld_video.setValue(round((position / self.vidoeLength) * 100))
        self.videoPlayDurationLabel.setText(str(round((position / self.vidoeLength) * 100, 2)) + '%')
        if((self.endTimeValue)==0):
            self.endTimeValueLE.setText(str(int(self.player.duration()/1000)))

    def transformToGif(self):
        print('transformToGif--filepath='+fileList[0].path())
        cache = mpe.VideoFileClip(fileList[0].path()).subclip(self.startTimeValue,self.endTimeValue)
        date=time.strftime('%Y-%m-%d_%H-%M-%S')
        resultGifFilePath='./gif/'+date+'.gif'# 使用日期时间作为gif文件名称
        # TODO 转换进度条对话框 展示 
        cache.write_gif(resultGifFilePath,fps=float(self.fpsValue))
        self.gif = QMovie(resultGifFilePath)
        
        self.label.setMovie(self.gif)
        self.gif.start()

        self.gifFileNameLable.setText(date+'.gif')
        doubleSize=os.path.getsize(resultGifFilePath)/1000
        self.gifSizeLable.setText(str(int(doubleSize))+'KB')

        
    def onChangedOfFPS(self, text):
        self.fpsValue=text
        print('fps='+self.fpsValue)
        
    def onChangedOfStartTime(self, text):
        self.startTimeValue=text
        print('起点 start='+self.startTimeValue)

    def onChangedOfEndTime(self, text):
        if(''==text):
            self.endTimeValue=-1
        else :
            self.endTimeValue=int(text)
        print('end='+ str(self.endTimeValue))

    def timerEvent(self, e):
 
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
 
        self.step = self.step + 1
        self.pbar.setValue(self.step)
 
    def doAction(self):
 
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

    # def changeValue(self, value):
    #     if value == 0:
    #         self.label.setPixmap(QPixmap('./gif/2022-03-21-17.19.44.gif'))
    #     elif value > 0 and value <= 30:
    #         self.label.setPixmap(QPixmap('./img/1.jpg'))
    #     elif value > 30 and value < 80:
    #         self.label.setPixmap(QPixmap('med.ico'))
    #     else:
    #         self.label.setPixmap(QPixmap('max.ico'))
    def showDialog(self):
        # TODO 视频文件大小
        # TODO 播放时长
        # TODO 视频播放总时长显示
        
        global fileList
        fileList = QFileDialog.getOpenFileUrl()
        print(fileList[0])
        self.player.setMedia(QMediaContent(fileList[0]))  # 选取视频文件
        self.player.play() 

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
        
    # #控制窗口显示在屏幕中心的方法    
    # def center(self):
        
    #     #获得窗口
    #     qr = self.frameGeometry()
    #     #获得屏幕中心点
    #     cp = QDesktopWidget().availableGeometry().center()
    #     #显示到屏幕中心
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


