from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow
import numpy as np
import cv2
import time
from cncStage import cncPort
import serial.tools.list_ports

class AppFunctions(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.counting = 0
        self.center()
        self.cncFlag = False
        self.__press_pos = QPoint()
        self.mainStageModeStatus = 0
        self.ui.pushButton_coarse.clicked.connect(self.selectCoarse)
        self.ui.pushButton_fine.clicked.connect(self.selectFine)
        self.ui.pushButton_step.clicked.connect(self.selectStep)
        self.ui.pushButton_exit.clicked.connect(self.APP_EXİT)
        self.ui.pushButton_Z_up.pressed.connect(self.pushButtonZ_up_mouseDown)
        self.ui.pushButton_Z_up.released.connect(self.pushButtonZ_up_mouseUp)
        self.ui.pushButton_Z_down.pressed.connect(self.pushButtonZ_down_mouseDown)
        self.ui.pushButton_Z_down.released.connect(self.pushButtonZ_down_mouseUp)
        self.ui.pushButton_X_left.pressed.connect(self.pushButtonX_down_mouseDown)
        self.ui.pushButton_X_left.released.connect(self.pushButtonX_down_mouseUp)
        self.ui.pushButton_X_right.pressed.connect(self.pushButtonX_up_mouseDown)
        self.ui.pushButton_X_right.released.connect(self.pushButtonX_up_mouseUp)
        self.ui.pushButton_Y_up.pressed.connect(self.pushButtonY_up_mouseDown)
        self.ui.pushButton_Y_up.released.connect(self.pushButtonY_up_mouseUp)
        self.ui.pushButton_Y_down.pressed.connect(self.pushButtonY_down_mouseDown)
        self.ui.pushButton_Y_down.released.connect(self.pushButtonY_down_mouseUp)
        self.ui.pushButton_goAbsulutePosition.clicked.connect(self.goAbsulutePosition)
        self.ui.pushButton_start.clicked.connect(self.connectCnc)
        self.ui.pushButton_minimize.clicked.connect(self.minimize)
        self.ui.pushButton_exit_2.clicked.connect(self.APP_EXİT)

        self.ui.stackedWidget.setCurrentIndex(0)
        comlist = serial.tools.list_ports.comports()
        connected = []
        for element in comlist:
            connected.append(element.device)
            self.ui.comboBox_comPort.addItem(str(element.device))

        print("Connected COM ports: " + str(connected))

        self.stageMod = "Coarse"
        self.stageMode_new = None
        self.stageModArray = []
        self.maxStageMode = 0
        self.highlighter_x_pos = {
            "Coarse": 25,
            "Fine": 95,
            "Step": 168,
        }

        self.selectCoarse()

        def moveWindow(event):
            if(True):
                # IF LEFT CLICK MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
        self.ui.frame_9.mouseMoveEvent=moveWindow
    def minimize(self):
        self.showMinimized()

    def connectCnc(self):
        self.cnc = cncPort()
        self.cnc.connectCnc(self.ui.comboBox_comPort.currentText())
        self.cnc.change_pixmap_signal.connect(self.update_position)
        self.cnc.start()
        self.homeFlag = False
        self.position = ""
        self.old_position = ""
        self.ui.stackedWidget.setCurrentIndex(1)
        self.cncFlag=True


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def update_position(self, position):
        if (self.homeFlag):
            if (position.find("Idle") != -1):
                self.stopHomeTimer = True
        if (position.find("MPos:") != -1):
            pFrom = position.find("MPos:") + len("MPos:")
            pTo = position.rfind("FS:") - 1
            if (pTo != -2):
                result = position[pFrom:pTo]
                x_pFrom = 0
                x_to = result.find(',')
                self.x = result[x_pFrom:x_to]
                y_pFrom = result.find(",") + len(",")
                y_to = result.rfind(",")
                self.y = result[y_pFrom:y_to]
                self.z = result[y_to + 1:]
                if (result != self.old_position):
                    self.old_position = result
                    self.updatePos()

    def selectCoarse(self):
        self.stageMode_new="Coarse"
        self.activeStepMode = False
        self.zStackFeedRate = 10
        self.xyStackFeedRate = 100
        self.xyWaitTime = 0.00001
        if self.stageMod != self.stageMode_new:
            self.animateVideoQuality()
        self.nanoStageStepSize=0.1

    def selectFine(self):
        self.activeStepMode = False
        self.zStackFeedRate = 1
        self.xyStackFeedRate = 1
        self.stageMode_new="Fine"
        if self.stageMod != self.stageMode_new:
            self.animateVideoQuality()
        self.nanoStageStepSize = 0.01

    def selectStep(self):
        self.activeStepMode = True
        self.zStackFeedRate = 1
        self.xyStackFeedRate = 1
        self.stageMode_new="Step"
        if self.stageMod != self.stageMode_new:
            self.animateVideoQuality()

        self.nanoStageStepSize = 0.005

        #### STAGE #########

    def goZp(self):
        if (self.mainStageModeStatus == 0):
            if (self.activeStepMode):
                self.cnc.goZp_stepMode()
            else:
                self.cnc.goZp(self.zStackFeedRate)
        else:
            pass

    def pushButtonZ_up_mouseDown(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.resume()
            time.sleep(0.001)
            self.goZp()
            self.ui.pushButton_Z_up.setStyleSheet(u"QPushButton{\n"
                                                  "border:none;\n"
                                                  "background-position:center;\n"
                                                  "background-repeat:no-repeat;\n"
                                                  "background-image:url(:/icons/images/İcons/upBtn_pres.png);\n"
                                                  "}\n"
                                                  )
        else:
            self.piezo.goZp(self.nanoStageStepSize)
            self.ui.pushButton_Z_up.setStyleSheet(u"QPushButton{\n"
                                                  "border:none;\n"
                                                  "background-position:center;\n"
                                                  "background-repeat:no-repeat;\n"
                                                  "background-image:url(:/icons/images/İcons/upBtn_pres.png);\n"
                                                  "}\n"
                                                  )

    def pushButtonZ_up_mouseUp(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.hold()
            self.flagZp = False
            self.ui.pushButton_Z_up.setStyleSheet(u"QPushButton{\n"
                                                  "border:none;\n"
                                                  "background-position:center;\n"
                                                  "background-repeat:no-repeat;\n"
                                                  "background-image:url(:/icons/images/İcons/upBtn.png);\n"
                                                  "}\n"
                                                  )
        else:
            self.piezo.holdZp()
            self.ui.pushButton_Z_up.setStyleSheet(u"QPushButton{\n"
                                                  "border:none;\n"
                                                  "background-position:center;\n"
                                                  "background-repeat:no-repeat;\n"
                                                  "background-image:url(:/icons/images/İcons/upBtn.png);\n"
                                                  "}\n"
                                                  )

    def goZn(self):
        if (self.mainStageModeStatus == 0):
            if (self.activeStepMode):
                self.cnc.goZn_stepMode()
            else:
                self.cnc.goZn(self.zStackFeedRate)
        else:
            pass

    def pushButtonZ_down_mouseDown(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.resume()
            time.sleep(0.001)
            self.goZn()
            self.ui.pushButton_Z_down.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "background-position:center;\n"
                                                    "background-repeat:no-repeat;\n"
                                                    "background-image:url(:/icons/images/İcons/downBtn_pres.png);\n"
                                                    "}\n"
                                                    )
        else:
            self.piezo.goZn(self.nanoStageStepSize)
            self.ui.pushButton_Z_down.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "background-position:center;\n"
                                                    "background-repeat:no-repeat;\n"
                                                    "background-image:url(:/icons/images/İcons/downBtn_pres.png);\n"
                                                    "}\n"
                                                    )

    def pushButtonZ_down_mouseUp(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.hold()
            self.ui.pushButton_Z_down.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position:center;\n"
                                                    "background-repeat:no-repeat;\n"
                                                    "background-image:url(:/icons/images/İcons/downBtn.png);\n"
                                                    "}\n"
                                                    )
        else:
            self.piezo.holdZn()
            self.ui.pushButton_Z_down.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position:center;\n"
                                                    "background-repeat:no-repeat;\n"
                                                    "background-image:url(:/icons/images/İcons/downBtn.png);\n"
                                                    "}\n"
                                                    )

    def goXp(self):
        if (self.mainStageModeStatus == 0):
            if (self.activeStepMode):
                self.cnc.goXp_stepMode()
            else:
                self.cnc.goXp(self.xyStackFeedRate)
        else:
            pass

    def pushButtonX_up_mouseDown(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.resume()
            time.sleep(0.001)
            self.goXp()
            self.ui.pushButton_X_right.setStyleSheet(u"QPushButton{\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "background-image:url(:/icons/images/İcons/rightBtn_pres.png);\n"
                                                     "}\n"
                                                     )
        else:
            self.piezo.goXp(self.nanoStageStepSize)
            self.ui.pushButton_X_right.setStyleSheet(u"QPushButton{\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "background-image:url(:/icons/images/İcons/rightBtn_pres.png);\n"
                                                     "}\n"
                                                     )

    def pushButtonX_up_mouseUp(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.hold()
            self.ui.pushButton_X_right.setStyleSheet(u"QPushButton{\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "background-image:url(:/icons/images/İcons/rightBtn.png);\n"
                                                     "}\n"
                                                     )
        else:
            self.piezo.holdXp()
            self.ui.pushButton_X_right.setStyleSheet(u"QPushButton{\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "background-image:url(:/icons/images/İcons/rightBtn.png);\n"
                                                     "}\n"
                                                     )

    def goXn(self):
        if (self.mainStageModeStatus == 0):
            if (self.activeStepMode):
                self.cnc.goXn_stepMode()
            else:
                self.cnc.goXn(self.xyStackFeedRate)
        else:
            pass

    def pushButtonX_down_mouseDown(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.resume()
            time.sleep(0.001)
            self.goXn()
            self.ui.pushButton_X_left.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position:center;\n"
                                                    "background-repeat:no-repeat;\n"
                                                    "background-image: url(:/icons/images/İcons/leftBtn_pres.png);\n"
                                                    "}\n"
                                                    )
        else:
            self.piezo.goXn(self.nanoStageStepSize)
            self.ui.pushButton_X_left.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position:center;\n"
                                                    "background-repeat:no-repeat;\n"
                                                    "background-image: url(:/icons/images/İcons/leftBtn_pres.png);\n"
                                                    "}\n"
                                                    )

    def pushButtonX_down_mouseUp(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.hold()
            self.ui.pushButton_X_left.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position:center;\n"
                                                    "background-repeat: no-repeat;\n"
                                                    "background-image: url(:/icons/images/İcons/leftBtn.png);\n"
                                                    "}\n"
                                                    )
        else:
            self.piezo.holdXn()
            self.ui.pushButton_X_left.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position:center;\n"
                                                    "background-repeat: no-repeat;\n"
                                                    "background-image: url(:/icons/images/İcons/leftBtn.png);\n"
                                                    "}\n"
                                                    )

    def goYp(self):
        if (self.mainStageModeStatus == 0):
            if (self.activeStepMode):
                self.cnc.goYp_stepMode()
            else:
                self.cnc.goYp(self.xyStackFeedRate)
        else:
            pass

    def pushButtonY_up_mouseDown(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.resume()
            time.sleep(0.001)
            self.goYp()
            self.ui.pushButton_Y_up.setStyleSheet(u"QPushButton{\n"
                                                  "border: none;\n"
                                                  "background-position:center;\n"
                                                  "background-repeat: no-repeat;\n"
                                                  "background-image: url(:/icons/images/İcons/upBtn_pres.png);\n"
                                                  "}\n"
                                                  )
        else:
            self.piezo.goYp(self.nanoStageStepSize)
            self.ui.pushButton_Y_up.setStyleSheet(u"QPushButton{\n"
                                                  "border: none;\n"
                                                  "background-position:center;\n"
                                                  "background-repeat: no-repeat;\n"
                                                  "background-image: url(:/icons/images/İcons/upBtn_pres.png);\n"
                                                  "}\n"
                                                  )

    def pushButtonY_up_mouseUp(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.hold()
            self.ui.pushButton_Y_up.setStyleSheet(u"QPushButton{\n"
                                                  "border: none;\n"
                                                  "background-position:center;\n"
                                                  "background-repeat: no-repeat;\n"
                                                  "background-image: url(:/icons/images/İcons/upBtn.png);\n"
                                                  "}\n"
                                                  )
        else:
            self.piezo.holdYp()
            self.ui.pushButton_Y_up.setStyleSheet(u"QPushButton{\n"
                                                  "border: none;\n"
                                                  "background-position:center;\n"
                                                  "background-repeat: no-repeat;\n"
                                                  "background-image: url(:/icons/images/İcons/upBtn.png);\n"
                                                  "}\n"
                                                  )

    def goYn(self):
        if (self.mainStageModeStatus == 0):
            if (self.activeStepMode):
                self.cnc.goYn_stepMode()
            else:
                self.cnc.goYn(self.xyStackFeedRate)
        else:
            pass

    def pushButtonY_down_mouseDown(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.resume()
            time.sleep(0.001)
            self.goYn()
            self.ui.pushButton_Y_down.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position: center;\n"
                                                    "background-repeat:no-repeat;\n"
                                                    "background-image: url(:/icons/images/İcons/downBtn_pres.png);\n"
                                                    "}\n"
                                                    )
        else:
            self.piezo.goYn(self.nanoStageStepSize)
            self.ui.pushButton_Y_down.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position: center;\n"
                                                    "background-repeat:no-repeat;\n"
                                                    "background-image: url(:/icons/images/İcons/downBtn_pres.png);\n"
                                                    "}\n"
                                                    )

    def pushButtonY_down_mouseUp(self):
        if (self.mainStageModeStatus == 0):
            self.cnc.hold()
            self.ui.pushButton_Y_down.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position: center;\n"
                                                    "background-repeat: no-repeat;\n"
                                                    "background-image: url(:/icons/images/İcons/downBtn.png);\n"
                                                    "}\n"
                                                    )
        else:
            self.piezo.holdYn()
            self.ui.pushButton_Y_down.setStyleSheet(u"QPushButton{\n"
                                                    "border: none;\n"
                                                    "background-position: center;\n"
                                                    "background-repeat: no-repeat;\n"
                                                    "background-image: url(:/icons/images/İcons/downBtn.png);\n"
                                                    "}\n"
                                                    )

    def goAbsulutePosition(self):
        self.cnc.resume()
        time.sleep(0.001)
        x_location = self.ui.lineEdit_X_position.text()
        y_location = self.ui.lineEdit_Y_position.text()
        z_location = self.ui.lineEdit_Z_position.text()
        self.cnc.goAbsulutePosition(x_location, y_location, z_location)


    def animateVideoQuality(self):
        """def animateVideoQuality(self): -> self
        animate the highlight QRect over the current
        selected video quality."""
        # animation
        self.animation = QPropertyAnimation(self.ui.frame_highlighter, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(QRect(int(self.highlighter_x_pos[str(self.stageMod)]), 6,65, 30))
        self.animation.setEndValue(QRect(int(self.highlighter_x_pos[str(self.stageMode_new)]), 6, 65, 30))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        self.stageMod=self.stageMode_new


    def increase(self):
        self.counting+=1
        self.ui.label_count.setText(str(self.counting))

    def center(self):
        screen = QGuiApplication.screenAt(QCursor().pos())
        fg = self.frameGeometry()
        fg.moveCenter(screen.geometry().center())
        self.move(fg.topLeft())

    def updatePos(self):
        self.total_Zpos = round(round(float(self.z), 5), 4)
        self.total_Xpos = round(round(float(self.x), 5) , 4)
        self.total_Ypos = round(round(float(self.y), 5) , 4)
        self.ui.lineEdit_X_position.setText("{:.4f}".format(round(self.total_Xpos, 4)))
        self.ui.lineEdit_Y_position.setText("{:.4f}".format(round(self.total_Ypos, 4)))
        self.ui.lineEdit_Z_position.setText("{:.4f}".format(round(self.total_Zpos, 4)))
        self.x_pos = self.x
        self.y_pos = self.y
        self.z_pos = self.z

    def APP_EXİT(self):
        if(self.cncFlag==True):
            self.cnc.terminate()
        QCoreApplication.instance().quit()
        #exit(0)