# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainQOFVOd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(250, 600)
        MainWindow.setMinimumSize(QSize(250, 600))
        MainWindow.setMaximumSize(QSize(250, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(250, 0))
        self.centralwidget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 75))
        self.frame_7.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(200, 30))
        self.label_22.setMaximumSize(QSize(16777215, 30))
        self.label_22.setStyleSheet(u"font: 63 18pt \"Segoe UI Semibold\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:none;\n"
"\n"
"")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_22)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_8)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(250, 200))
        self.frame_4.setMaximumSize(QSize(250, 200))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 30))
        self.label_2.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox_comPort = QComboBox(self.frame_6)
        self.comboBox_comPort.setObjectName(u"comboBox_comPort")
        self.comboBox_comPort.setMinimumSize(QSize(0, 25))
        self.comboBox_comPort.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setPointSize(11)
        self.comboBox_comPort.setFont(font1)
        self.comboBox_comPort.setStyleSheet(u"QComboBox{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"}\n"
"QComboBox QAbstractItemView{border: 0px;color:white}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.comboBox_comPort)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.pushButton_start = QPushButton(self.frame_4)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(100, 30))
        self.pushButton_start.setMaximumSize(QSize(100, 30))
        self.pushButton_start.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_start, 0, Qt.AlignHCenter)

        self.pushButton_exit_2 = QPushButton(self.frame_4)
        self.pushButton_exit_2.setObjectName(u"pushButton_exit_2")
        self.pushButton_exit_2.setMinimumSize(QSize(100, 30))
        self.pushButton_exit_2.setMaximumSize(QSize(100, 30))
        self.pushButton_exit_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_exit_2, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setStyleSheet(u"background-color:rgb(30, 30, 30);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 30))
        self.label_23.setMaximumSize(QSize(130, 30))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(7)
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:none;\n"
"\n"
"")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_23)


        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_window = QFrame(self.frame_9)
        self.frame_window.setObjectName(u"frame_window")
        self.frame_window.setMaximumSize(QSize(110, 16777215))
        self.frame_window.setFrameShape(QFrame.NoFrame)
        self.frame_window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_window)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_minimize = QPushButton(self.frame_window)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setMinimumSize(QSize(30, 30))
        self.pushButton_minimize.setMaximumSize(QSize(30, 30))
        self.pushButton_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minimize.setAutoFillBackground(False)
        self.pushButton_minimize.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/images/\u0130cons/icon_minimize.png);\n"
"border:none;\n"
"border-radius:5px;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_minimize.setAutoRepeat(False)
        self.pushButton_minimize.setAutoExclusive(False)
        self.pushButton_minimize.setAutoDefault(False)
        self.pushButton_minimize.setFlat(False)

        self.horizontalLayout_6.addWidget(self.pushButton_minimize)

        self.pushButton_maximize = QPushButton(self.frame_window)
        self.pushButton_maximize.setObjectName(u"pushButton_maximize")
        self.pushButton_maximize.setMinimumSize(QSize(30, 30))
        self.pushButton_maximize.setMaximumSize(QSize(30, 30))
        self.pushButton_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_maximize.setAutoFillBackground(False)
        self.pushButton_maximize.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/images/\u0130cons/icon_maximize.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(200, 200, 200);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_maximize.setAutoRepeat(False)
        self.pushButton_maximize.setAutoExclusive(False)
        self.pushButton_maximize.setAutoDefault(False)
        self.pushButton_maximize.setFlat(False)

        self.horizontalLayout_6.addWidget(self.pushButton_maximize)

        self.pushButton_exit = QPushButton(self.frame_window)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setMinimumSize(QSize(30, 30))
        self.pushButton_exit.setMaximumSize(QSize(30, 30))
        self.pushButton_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_exit.setAutoFillBackground(False)
        self.pushButton_exit.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/images/\u0130cons/cil-x.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(170, 0, 0);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_exit.setAutoRepeat(False)
        self.pushButton_exit.setAutoExclusive(False)
        self.pushButton_exit.setAutoDefault(False)
        self.pushButton_exit.setFlat(False)

        self.horizontalLayout_6.addWidget(self.pushButton_exit)


        self.horizontalLayout_2.addWidget(self.frame_window)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.frame_20 = QFrame(self.page_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 50))
        self.frame_20.setMaximumSize(QSize(16777215, 100))
        self.frame_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.pushButton_home = QPushButton(self.frame_20)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setMinimumSize(QSize(150, 30))
        self.pushButton_home.setMaximumSize(QSize(30, 16777215))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_home.setFont(font3)
        self.pushButton_home.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/images/\u0130cons/home_btn.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-image: url(:/icons/images/\u0130cons/home_Btn_pres.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_53.addWidget(self.pushButton_home)


        self.verticalLayout_9.addWidget(self.frame_20)

        self.frame_14 = QFrame(self.page_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 50))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_highlighter = QFrame(self.frame_14)
        self.frame_highlighter.setObjectName(u"frame_highlighter")
        self.frame_highlighter.setGeometry(QRect(25, 6, 65, 30))
        self.frame_highlighter.setMaximumSize(QSize(16777215, 16777215))
        self.frame_highlighter.setStyleSheet(u"background-color: rgba(0, 122, 204,120);\n"
"border-radius:10px;")
        self.frame_highlighter.setFrameShape(QFrame.NoFrame)
        self.frame_highlighter.setFrameShadow(QFrame.Raised)
        self.pushButton_coarse = QPushButton(self.frame_14)
        self.pushButton_coarse.setObjectName(u"pushButton_coarse")
        self.pushButton_coarse.setGeometry(QRect(20, 5, 75, 30))
        self.pushButton_coarse.setMinimumSize(QSize(60, 30))
        self.pushButton_coarse.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_coarse.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.pushButton_fine = QPushButton(self.frame_14)
        self.pushButton_fine.setObjectName(u"pushButton_fine")
        self.pushButton_fine.setGeometry(QRect(92, 5, 75, 30))
        self.pushButton_fine.setMinimumSize(QSize(60, 30))
        self.pushButton_fine.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_fine.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.pushButton_step = QPushButton(self.frame_14)
        self.pushButton_step.setObjectName(u"pushButton_step")
        self.pushButton_step.setGeometry(QRect(165, 5, 75, 30))
        self.pushButton_step.setMinimumSize(QSize(60, 30))
        self.pushButton_step.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_step.setStyleSheet(u"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.pushButton_coarse.raise_()
        self.pushButton_fine.raise_()
        self.pushButton_step.raise_()
        self.frame_highlighter.raise_()

        self.verticalLayout_9.addWidget(self.frame_14)

        self.frame_38 = QFrame(self.page_2)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 180))
        self.frame_38.setMaximumSize(QSize(16777215, 180))
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_38)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(4, -1, 4, -1)
        self.frame_18 = QFrame(self.frame_38)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_18)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_66 = QFrame(self.frame_18)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 45))
        self.frame_66.setMaximumSize(QSize(16777215, 45))
        self.frame_66.setFrameShape(QFrame.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_132 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_132.setSpacing(0)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.frame_145 = QFrame(self.frame_66)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setMinimumSize(QSize(50, 0))
        self.frame_145.setMaximumSize(QSize(50, 16777215))
        self.frame_145.setFrameShape(QFrame.NoFrame)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.frame_212 = QFrame(self.frame_145)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setGeometry(QRect(70, 10, 120, 80))
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_132.addWidget(self.frame_145)

        self.frame_138 = QFrame(self.frame_66)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_133 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_133.setSpacing(0)
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.horizontalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Y_up = QPushButton(self.frame_138)
        self.pushButton_Y_up.setObjectName(u"pushButton_Y_up")
        self.pushButton_Y_up.setMinimumSize(QSize(43, 42))
        self.pushButton_Y_up.setMaximumSize(QSize(45, 45))
        self.pushButton_Y_up.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Y_up.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/images/\u0130cons/upBtn.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-image: url(:/icons/images/\u0130cons/upBtn_pres.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_133.addWidget(self.pushButton_Y_up)


        self.horizontalLayout_132.addWidget(self.frame_138)

        self.frame_213 = QFrame(self.frame_66)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setMinimumSize(QSize(42, 0))
        self.frame_213.setMaximumSize(QSize(42, 16777215))
        self.frame_213.setFrameShape(QFrame.NoFrame)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.frame_214 = QFrame(self.frame_213)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setGeometry(QRect(70, 10, 120, 80))
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_132.addWidget(self.frame_213)

        self.frame_113 = QFrame(self.frame_66)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.NoFrame)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_134 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_134.setSpacing(0)
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.horizontalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Z_up = QPushButton(self.frame_113)
        self.pushButton_Z_up.setObjectName(u"pushButton_Z_up")
        self.pushButton_Z_up.setMinimumSize(QSize(45, 45))
        self.pushButton_Z_up.setMaximumSize(QSize(45, 45))
        self.pushButton_Z_up.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Z_up.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/images/\u0130cons/upBtn.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-image: url(:/icons/images/\u0130cons/upBtn_pres.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_134.addWidget(self.pushButton_Z_up)


        self.horizontalLayout_132.addWidget(self.frame_113)


        self.verticalLayout_70.addWidget(self.frame_66)

        self.frame_86 = QFrame(self.frame_18)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(0, 50))
        self.frame_86.setMaximumSize(QSize(16777215, 50))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_138 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_138.setSpacing(0)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.horizontalLayout_138.setContentsMargins(0, 0, 0, 0)
        self.frame_224 = QFrame(self.frame_86)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_224.setFrameShape(QFrame.NoFrame)
        self.frame_224.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_139 = QHBoxLayout(self.frame_224)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.pushButton_X_left = QPushButton(self.frame_224)
        self.pushButton_X_left.setObjectName(u"pushButton_X_left")
        self.pushButton_X_left.setMinimumSize(QSize(45, 45))
        self.pushButton_X_left.setMaximumSize(QSize(45, 41))
        self.pushButton_X_left.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/images/\u0130cons/leftBtn.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-image: url(:/icons/images/\u0130cons/leftBtn_pres.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"")

        self.horizontalLayout_139.addWidget(self.pushButton_X_left)


        self.horizontalLayout_138.addWidget(self.frame_224)

        self.frame_223 = QFrame(self.frame_86)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setMinimumSize(QSize(60, 0))
        self.frame_223.setMaximumSize(QSize(40, 16777215))
        self.frame_223.setFrameShape(QFrame.NoFrame)
        self.frame_223.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_138.addWidget(self.frame_223)

        self.frame_222 = QFrame(self.frame_86)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setFrameShape(QFrame.NoFrame)
        self.frame_222.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_140 = QHBoxLayout(self.frame_222)
        self.horizontalLayout_140.setSpacing(0)
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_140.setContentsMargins(0, 0, 0, 0)
        self.pushButton_X_right = QPushButton(self.frame_222)
        self.pushButton_X_right.setObjectName(u"pushButton_X_right")
        self.pushButton_X_right.setMinimumSize(QSize(45, 45))
        self.pushButton_X_right.setMaximumSize(QSize(45, 45))
        self.pushButton_X_right.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_X_right.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/images/\u0130cons/rightBtn.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-image: url(:/icons/images/\u0130cons/rightBtn_pres.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_140.addWidget(self.pushButton_X_right)


        self.horizontalLayout_138.addWidget(self.frame_222)

        self.frame_215 = QFrame(self.frame_86)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_138.addWidget(self.frame_215)


        self.verticalLayout_70.addWidget(self.frame_86)

        self.frame_106 = QFrame(self.frame_18)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(0, 45))
        self.frame_106.setMaximumSize(QSize(16777215, 45))
        self.frame_106.setFrameShape(QFrame.NoFrame)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_141 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_141.setSpacing(0)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.frame_228 = QFrame(self.frame_106)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setMinimumSize(QSize(50, 0))
        self.frame_228.setMaximumSize(QSize(50, 16777215))
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_141.addWidget(self.frame_228)

        self.frame_227 = QFrame(self.frame_106)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_142 = QHBoxLayout(self.frame_227)
        self.horizontalLayout_142.setSpacing(0)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Y_down = QPushButton(self.frame_227)
        self.pushButton_Y_down.setObjectName(u"pushButton_Y_down")
        self.pushButton_Y_down.setMinimumSize(QSize(45, 45))
        self.pushButton_Y_down.setMaximumSize(QSize(45, 45))
        self.pushButton_Y_down.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Y_down.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/images/\u0130cons/downBtn.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-image: url(:/icons/images/\u0130cons/downBtn_pres.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_Y_down.setCheckable(True)
        self.pushButton_Y_down.setChecked(False)

        self.horizontalLayout_142.addWidget(self.pushButton_Y_down)


        self.horizontalLayout_141.addWidget(self.frame_227)

        self.frame_226 = QFrame(self.frame_106)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setMinimumSize(QSize(42, 0))
        self.frame_226.setMaximumSize(QSize(42, 16777215))
        self.frame_226.setFrameShape(QFrame.NoFrame)
        self.frame_226.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_141.addWidget(self.frame_226)

        self.frame_225 = QFrame(self.frame_106)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setFrameShape(QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_143 = QHBoxLayout(self.frame_225)
        self.horizontalLayout_143.setSpacing(0)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Z_down = QPushButton(self.frame_225)
        self.pushButton_Z_down.setObjectName(u"pushButton_Z_down")
        self.pushButton_Z_down.setMinimumSize(QSize(45, 45))
        self.pushButton_Z_down.setMaximumSize(QSize(45, 41))
        self.pushButton_Z_down.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Z_down.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/images/\u0130cons/downBtn.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-image: url(:/icons/images/\u0130cons/downBtn_pres.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_143.addWidget(self.pushButton_Z_down)


        self.horizontalLayout_141.addWidget(self.frame_225)


        self.verticalLayout_70.addWidget(self.frame_106)


        self.verticalLayout_10.addWidget(self.frame_18)


        self.verticalLayout_9.addWidget(self.frame_38)

        self.frame_33 = QFrame(self.page_2)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 120))
        self.frame_33.setMaximumSize(QSize(16777215, 180))
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_33)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_9 = QLabel(self.frame_34)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(30, 30))
        self.label_9.setMaximumSize(QSize(30, 30))
        self.label_9.setStyleSheet(u"background-image: url(:/icons/images/\u0130cons/x_axis.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;")

        self.horizontalLayout_20.addWidget(self.label_9)

        self.lineEdit_X_position = QLineEdit(self.frame_34)
        self.lineEdit_X_position.setObjectName(u"lineEdit_X_position")
        self.lineEdit_X_position.setMinimumSize(QSize(0, 25))
        self.lineEdit_X_position.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_X_position.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_X_position.setStyleSheet(u"QLineEdit{\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(49, 51, 50);\n"
"border-radius:5px;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;\n"
"selection-background-color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QLineEdit:hover { \n"
"	border-color:rgb(0, 0, 127);\n"
"	border-width : 2px;\n"
"	\n"
"}\n"
"")
        self.lineEdit_X_position.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lineEdit_X_position)


        self.verticalLayout_8.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_7 = QLabel(self.frame_35)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(30, 30))
        self.label_7.setMaximumSize(QSize(30, 30))
        self.label_7.setStyleSheet(u"background-image: url(:/icons/images/\u0130cons/y_axis.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;")

        self.horizontalLayout_21.addWidget(self.label_7)

        self.lineEdit_Y_position = QLineEdit(self.frame_35)
        self.lineEdit_Y_position.setObjectName(u"lineEdit_Y_position")
        self.lineEdit_Y_position.setMinimumSize(QSize(0, 25))
        self.lineEdit_Y_position.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_Y_position.setStyleSheet(u"QLineEdit{\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(49, 51, 50);\n"
"border-radius:5px;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;\n"
"selection-background-color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QLineEdit:hover { \n"
"	border-color:rgb(0, 0, 127);\n"
"	border-width : 2px;\n"
"	\n"
"}\n"
"")
        self.lineEdit_Y_position.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_Y_position)


        self.verticalLayout_8.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_8 = QLabel(self.frame_36)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(30, 30))
        self.label_8.setMaximumSize(QSize(30, 30))
        self.label_8.setStyleSheet(u"background-image: url(:/icons/images/\u0130cons/z_axis.png);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;")

        self.horizontalLayout_22.addWidget(self.label_8)

        self.lineEdit_Z_position = QLineEdit(self.frame_36)
        self.lineEdit_Z_position.setObjectName(u"lineEdit_Z_position")
        self.lineEdit_Z_position.setMinimumSize(QSize(0, 25))
        self.lineEdit_Z_position.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_Z_position.setStyleSheet(u"QLineEdit{\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(49, 51, 50);\n"
"border-radius:5px;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;\n"
"selection-background-color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QLineEdit:hover { \n"
"	border-color:rgb(0, 0, 127);\n"
"	border-width : 2px;\n"
"	\n"
"}\n"
"")
        self.lineEdit_Z_position.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.lineEdit_Z_position)


        self.verticalLayout_8.addWidget(self.frame_36)


        self.verticalLayout_9.addWidget(self.frame_33)

        self.frame_32 = QFrame(self.page_2)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 45))
        self.frame_32.setMaximumSize(QSize(16777215, 60))
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_goAbsulutePosition = QPushButton(self.frame_32)
        self.pushButton_goAbsulutePosition.setObjectName(u"pushButton_goAbsulutePosition")
        self.pushButton_goAbsulutePosition.setMinimumSize(QSize(100, 30))
        self.pushButton_goAbsulutePosition.setMaximumSize(QSize(100, 30))
        self.pushButton_goAbsulutePosition.setFont(font3)
        self.pushButton_goAbsulutePosition.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goAbsulutePosition.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/images/\u0130cons/goButton.png);\n"
"background-color: rgb(0,110,0);\n"
"border-radius:5px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border-radius:5px;\n"
"background-color: rgb(0,140,0);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.pushButton_goAbsulutePosition)


        self.verticalLayout_9.addWidget(self.frame_32)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_minimize.setDefault(False)
        self.pushButton_maximize.setDefault(False)
        self.pushButton_exit.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"STAGE CONTROL", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"COM PORT:", None))
        self.comboBox_comPort.setCurrentText("")
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_exit_2.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"STAGE CONTROL", None))
#if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_exit.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_exit.setText("")
        self.pushButton_home.setText("")
        self.pushButton_coarse.setText(QCoreApplication.translate("MainWindow", u"Coarse", None))
        self.pushButton_fine.setText(QCoreApplication.translate("MainWindow", u"Fine", None))
        self.pushButton_step.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.pushButton_Y_up.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_Y_up.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Z_up.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_Z_up.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_X_left.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_X_left.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_X_right.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_X_right.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Y_down.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_Y_down.setShortcut(QCoreApplication.translate("MainWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_Z_down.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_Z_down.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.label_9.setText("")
        self.lineEdit_X_position.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_7.setText("")
        self.lineEdit_Y_position.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_8.setText("")
        self.lineEdit_Z_position.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_goAbsulutePosition.setText("")
    # retranslateUi

