from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os, sys
import numpy as np
import csv
from pathlib import Path
from QTbegin import Ui_MainWindow
import time
import numpy as np
import pandas as pd
class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.stop=0
        self.ui.setupUi(self)
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('Multiple Browse') 
        self.ui.pushButton_5.clicked.connect(self.SingleBrowse)
        self.timer=QtCore.QTimer(self)
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.plotthis)
        self.whatever=0



        # self.ui.pushButton_2.clicked.connect(self.Play)
        # self.ui.pushButton_4.clicked.connect(self.Pause)
        # self.PauseGraph = 0
        self.ui.pushButton_4.clicked.connect(self.pause)
        self.ui.pushButton_2.clicked.connect(self.play)

        self.show()
        self.x=[] 
        self.y=[]
        self.xcsv=[]
        self.ycsv=[]
        # self.xlsx=[]
        # self.ylsx=[]

    
    def play(self):
        self.stop = 0
        self.timer.start()




    def pause(self):
        self.stop = 1
        self.timer.stop()

    def update_plot_data(self):
        if self.stop ==0:
            self.play()
        if self.stop==1:
            print ("s")
            self.pause()


    def plotthis(self):
        if self.ext == ".txt":
            if  self.stop==0:
                    self.play()
                    self.ui.graphicsView.plot(self.x,self.y, label='loadedfile')
                    QtCore.QCoreApplication.processEvents()
            else:
                self.pause()
                

        elif self.ext == ".csv":
              if  self.stop==0:
                  self.play()
                  self.ui.graphicsView_2.plot(self.xcsv,self.ycsv, label='loadedfile',pen='r')
                  QtCore.QCoreApplication.processEvents()

              else:
                    self.pause()
        # elif self.ext==".xlsx" :



            #  self.ui.graphicsView_3.plot(self.xlsx,self.ylsx,label = 'ya mosahel',pen ='r')



    def SingleBrowse(self):
        filePaths = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File',"~/Desktop/sigViews",'*.txt && *.csv && *.xlsx')
        for filePath in filePaths:
            for f in filePath:
                print('filePath',f, '\n')
                if f == '*':
                    break
                self.ext = os.path.splitext(f)[-1].lower()
                if self.ext == ".txt":
                    print( "is an txt!")
                # fileHandle = open(f, 'r')
                    with open(f,'r')as csvfile:
                        self.plots=np.genfromtxt(csvfile, delimiter=' ')

                        for row in self.plots:
                            # self.ui.graphicsView.clear()
                            self.x.append(float (row[0]))
                            self.y.append(float (row[1]))
                            self.arraylength=len(self.x)
                            self.plotthis()

                                

                elif self.ext == ".csv":
                     print ("this is .csv")
                     with open(f,'r')as csvfile:
                         plots=csv.reader(csvfile, delimiter=',')
                         for row in plots:
                                self.ui.graphicsView.clear()
                                self.xcsv.append(float (row[0]))
                                self.ycsv.append(float (row[1]))
                                self.plotthis()
                # elif self.ext==".xlsx":
                #         self.df =pd.read_excel('emg_healthy.xlsx', sheet_name='emg_healthy')
                #         self.ui.graphicsView_3.plot(self.df['Column1'], self.df['Column2'], pen='r')
                #         QtCore.QCoreApplication.processEvents()



                    # self.plotthis()
                        # self.ui.graphicsView.clear()




def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == '__main__':
    main()
