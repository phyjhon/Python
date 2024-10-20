# -*- coding: utf-8 -*-

from PySide6 import QtWidgets
import xlrd
import pandas as pd
import numpy as np
import openpyxl
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QToolBar, QWidget, QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1263, 824)
        self.actionInstructions = QAction(MainWindow)
        self.actionInstructions.setObjectName(u"actionInstructions")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        self.actionHelp_Contact = QAction(MainWindow)
        self.actionHelp_Contact.setObjectName(u"actionHelp_Contact")
        self.actionprint = QAction(MainWindow)
        self.actionprint.setObjectName(u"actionprint")
        icon = QIcon()
        icon.addFile(u"print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionprint.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -119, 1121, 807))
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 10, 381, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 40, 541, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_11.setFont(font1)
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 80, 344, 232))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 5, 1, 1, 1)

        self.comboBox_dose_rate = QComboBox(self.gridLayoutWidget)
        self.comboBox_dose_rate.addItem("")
        self.comboBox_dose_rate.setObjectName(u"comboBox_dose_rate")

        self.gridLayout_2.addWidget(self.comboBox_dose_rate, 3, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 8, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 7, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)

        self.comboBox_phantom_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_phantom_2.addItem("")
        self.comboBox_phantom_2.addItem("")
        self.comboBox_phantom_2.setObjectName(u"comboBox_phantom_2")

        self.gridLayout_2.addWidget(self.comboBox_phantom_2, 4, 1, 1, 1)

        self.comboBox_linac = QComboBox(self.gridLayoutWidget)
        self.comboBox_linac.addItem("")
        self.comboBox_linac.setObjectName(u"comboBox_linac")

        self.gridLayout_2.addWidget(self.comboBox_linac, 1, 1, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 7, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 8, 1, 1, 1)

        self.comboBox_energy = QComboBox(self.gridLayoutWidget)
        self.comboBox_energy.addItem("")
        self.comboBox_energy.setObjectName(u"comboBox_energy")

        self.gridLayout_2.addWidget(self.comboBox_energy, 2, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 6, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 6, 0, 1, 1)

        self.label_44 = QLabel(self.gridLayoutWidget)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_2.addWidget(self.label_44, 0, 0, 1, 1)

        self.comboBox__user = QComboBox(self.gridLayoutWidget)
        self.comboBox__user.addItem("")
        self.comboBox__user.setObjectName(u"comboBox__user")

        self.gridLayout_2.addWidget(self.comboBox__user, 0, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 310, 131, 20))
        self.formLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 340, 351, 138))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_tpr_20 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_tpr_20.setObjectName(u"lineEdit_tpr_20")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_tpr_20)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_tpr_10 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_tpr_10.setObjectName(u"lineEdit_tpr_10")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_tpr_10)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.label_tpr_2010 = QLabel(self.formLayoutWidget)
        self.label_tpr_2010.setObjectName(u"label_tpr_2010")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_tpr_2010)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.label_tpr_var = QLabel(self.formLayoutWidget)
        self.label_tpr_var.setObjectName(u"label_tpr_var")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_tpr_var)

        self.pushButton_tpr2010 = QPushButton(self.formLayoutWidget)
        self.pushButton_tpr2010.setObjectName(u"pushButton_tpr2010")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.pushButton_tpr2010)

        self.label_tpr_decision = QLabel(self.formLayoutWidget)
        self.label_tpr_decision.setObjectName(u"label_tpr_decision")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_tpr_decision)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 500, 291, 16))
        self.label_20.setFont(font1)
        self.gridLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 540, 160, 80))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_detector = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_detector.addItem("")
        self.comboBox_detector.setObjectName(u"comboBox_detector")

        self.gridLayout_3.addWidget(self.comboBox_detector, 0, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)

        self.comboBox_electrometer = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_electrometer.addItem("")
        self.comboBox_electrometer.setObjectName(u"comboBox_electrometer")

        self.gridLayout_3.addWidget(self.comboBox_electrometer, 1, 1, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 640, 441, 21))
        self.label_22.setFont(font1)
        self.gridLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(30, 680, 271, 117))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.gridLayoutWidget_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 2, 1, 1, 1)

        self.lineEdit_temp = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_temp.setObjectName(u"lineEdit_temp")

        self.gridLayout_4.addWidget(self.lineEdit_temp, 0, 1, 1, 1)

        self.lineEdit_pressure = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_pressure.setObjectName(u"lineEdit_pressure")

        self.gridLayout_4.addWidget(self.lineEdit_pressure, 1, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_3)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_4.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_3)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_4.addWidget(self.label_34, 3, 0, 1, 1)

        self.lineEdit_elec_calib = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_elec_calib.setObjectName(u"lineEdit_elec_calib")

        self.gridLayout_4.addWidget(self.lineEdit_elec_calib, 3, 1, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(560, 0, 20, 851))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget_4 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(590, 30, 508, 210))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_v1 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_v1.setObjectName(u"lineEdit_v1")

        self.gridLayout_5.addWidget(self.lineEdit_v1, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_5.addWidget(self.comboBox_2, 2, 1, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 2, 0, 1, 1)

        self.lineEdit_m2 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_m2.setObjectName(u"lineEdit_m2")

        self.gridLayout_5.addWidget(self.lineEdit_m2, 5, 1, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_4)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 3, 0, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_4)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 5, 0, 1, 1)

        self.lineEdit_mminus = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_mminus.setObjectName(u"lineEdit_mminus")

        self.gridLayout_5.addWidget(self.lineEdit_mminus, 4, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_m1 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_m1.setObjectName(u"lineEdit_m1")

        self.gridLayout_5.addWidget(self.lineEdit_m1, 3, 1, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_4)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 1, 0, 1, 1)

        self.lineEdit_v2 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_v2.setObjectName(u"lineEdit_v2")

        self.gridLayout_5.addWidget(self.lineEdit_v2, 1, 1, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_4)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 4, 0, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_4)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_5.addWidget(self.label_38, 6, 0, 1, 1)

        self.lineEdit_mu = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_mu.setObjectName(u"lineEdit_mu")

        self.gridLayout_5.addWidget(self.lineEdit_mu, 6, 1, 1, 1)

        self.pushButton_calculate = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        self.pushButton_calculate.setGeometry(QRect(800, 260, 93, 28))
        self.gridLayoutWidget_5 = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(590, 320, 471, 461))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_kelec = QLabel(self.gridLayoutWidget_5)
        self.label_kelec.setObjectName(u"label_kelec")

        self.gridLayout_6.addWidget(self.label_kelec, 1, 1, 1, 1)

        self.label_ks = QLabel(self.gridLayoutWidget_5)
        self.label_ks.setObjectName(u"label_ks")

        self.gridLayout_6.addWidget(self.label_ks, 3, 1, 1, 1)

        self.label_abs_ref = QLabel(self.gridLayoutWidget_5)
        self.label_abs_ref.setObjectName(u"label_abs_ref")

        self.gridLayout_6.addWidget(self.label_abs_ref, 7, 1, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget_5)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_6.addWidget(self.label_43, 10, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_5)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 7, 0, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_5)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 6, 0, 1, 1)

        self.label_percent_variation = QLabel(self.gridLayoutWidget_5)
        self.label_percent_variation.setObjectName(u"label_percent_variation")

        self.gridLayout_6.addWidget(self.label_percent_variation, 10, 1, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_5)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 2, 0, 1, 1)

        self.label_ktp = QLabel(self.gridLayoutWidget_5)
        self.label_ktp.setObjectName(u"label_ktp")

        self.gridLayout_6.addWidget(self.label_ktp, 0, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_5)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 1, 0, 1, 1)

        self.label_kpol = QLabel(self.gridLayoutWidget_5)
        self.label_kpol.setObjectName(u"label_kpol")

        self.gridLayout_6.addWidget(self.label_kpol, 2, 1, 1, 1)

        self.label_37 = QLabel(self.gridLayoutWidget_5)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 3, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_5)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 0, 0, 1, 1)

        self.label_45 = QLabel(self.gridLayoutWidget_5)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_6.addWidget(self.label_45, 4, 0, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_5)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 8, 0, 1, 1)

        self.label_ndwq = QLabel(self.gridLayoutWidget_5)
        self.label_ndwq.setObjectName(u"label_ndwq")

        self.gridLayout_6.addWidget(self.label_ndwq, 4, 1, 1, 1)

        self.label_abs_dmax = QLabel(self.gridLayoutWidget_5)
        self.label_abs_dmax.setObjectName(u"label_abs_dmax")

        self.gridLayout_6.addWidget(self.label_abs_dmax, 9, 1, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget_5)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_6.addWidget(self.label_42, 9, 0, 1, 1)

        self.label_mcrt = QLabel(self.gridLayoutWidget_5)
        self.label_mcrt.setObjectName(u"label_mcrt")

        self.gridLayout_6.addWidget(self.label_mcrt, 6, 1, 1, 1)

        self.label_dmax = QLabel(self.gridLayoutWidget_5)
        self.label_dmax.setObjectName(u"label_dmax")

        self.gridLayout_6.addWidget(self.label_dmax, 8, 1, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget_5)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_6.addWidget(self.label_46, 5, 0, 1, 1)

        self.label_kqq0 = QLabel(self.gridLayoutWidget_5)
        self.label_kqq0.setObjectName(u"label_kqq0")

        self.gridLayout_6.addWidget(self.label_kqq0, 5, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1263, 26))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionInstructions)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionLicense)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionHelp_Contact)
        self.toolBar.addAction(self.actionprint)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

        df = pd.ExcelFile("linac_library.xlsx")
        total_item = list(df.sheet_names)
        for i in total_item:
            self.comboBox_linac.addItem(i)

        detectors = pd.read_excel("detector_library.xlsx", 'detectors', engine= "openpyxl")
        detector_list = list(detectors.loc[:, 'serial_no'])
        for num in detector_list:
            self.comboBox_detector.addItem(str(num))

        electrometer = pd.read_excel("detector_library.xlsx", "electrometer", engine="openpyxl")
        electrometer_list = list(electrometer.loc[:, 'name'])
        for electrometer in electrometer_list:
            self.comboBox_electrometer.addItem(electrometer)

        self.comboBox_linac.currentTextChanged.connect(self.select_energy)
        self.comboBox_phantom_2.currentTextChanged.connect(self.water_phantom)
        self.pushButton_tpr2010.clicked.connect(self.beam_quality)
        self.pushButton_calculate.clicked.connect(self.calculation)
        self.actionprint.triggered.connect(self.printing)
        self.actionLicense.triggered.connect(self.license)
        self.actionHelp_Contact.triggered.connect(self.Contact)

        user_file_name = pd.read_excel("user_library.xlsx", "user")
        user_name_list = list(user_file_name.loc[:, "user"])
        for user in user_name_list:
            self.comboBox__user.addItem(user)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TRS398 High Energy Photons", None))
        MainWindow.setWindowIcon(QIcon("icon_abs.png"))
        self.actionInstructions.setText(QCoreApplication.translate("MainWindow", u"Instructions", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.actionHelp_Contact.setText(QCoreApplication.translate("MainWindow", u"Help/Contact", None))
        self.actionprint.setText(QCoreApplication.translate("MainWindow", u"print", None))
#if QT_CONFIG(shortcut)
        self.actionprint.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Determination of Absorbed Dose to Water", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Radiation treatment unit and reference conditions for Dwq measurement", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"10x10 cm^2", None))
        self.comboBox_dose_rate.setItemText(0, QCoreApplication.translate("MainWindow", u"select", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Energy", None))
        #self.label_18.setText(QCoreApplication.translate("MainWindow", u"Reference distance in case of vw", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"100 cm", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Reference field size", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nominal Dose Rate (MU/min)", None))
        self.comboBox_phantom_2.setItemText(0, QCoreApplication.translate("MainWindow", u"water phantom", None))
        # self.comboBox_phantom_2.setItemText(1, QCoreApplication.translate("MainWindow", u"virtual water", None))

        self.comboBox_linac.setItemText(0, QCoreApplication.translate("MainWindow", u"select", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"SSD", None))
        #self.label_19.setText(QCoreApplication.translate("MainWindow", u"updates only if vw is used", None))
        self.comboBox_energy.setItemText(0, QCoreApplication.translate("MainWindow", u"select", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Linac", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"10 g/cm^2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Reference Phantom", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Reference Depth", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.comboBox__user.setItemText(0, QCoreApplication.translate("MainWindow", u"select", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Beam Quality", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TPR (meter reading at 20 cm)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TPR (meter reading at 10 cm)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TPR 20,10", None))
        self.label_tpr_2010.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TPR 2010 variation from baseline ", None))
        self.label_tpr_var.setText("")
        self.pushButton_tpr2010.setText(QCoreApplication.translate("MainWindow", u"click_for_TPR_2010 ", None))
        self.label_tpr_decision.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ionization Chamber and Electrometer", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Detector", None))
        self.comboBox_detector.setItemText(0, QCoreApplication.translate("MainWindow", u"select", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Electrometer", None))
        self.comboBox_electrometer.setItemText(0, QCoreApplication.translate("MainWindow", u"select", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Dosimeter reading and correction for influencing quanitites", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"User Polarity", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Pressure in mBar", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"positive", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Negative", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Temperature in degree celsius ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Electrometer calibration factor", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"pulsed radiation", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"pulsed scanned radiation", None))

        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Pulsed/pulsed scanned radiation ", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Uncorrected dosimeter reading at V1 ", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Uncorrected dosimeter reading for reduced voltage V2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Polarizing voltage V1 ", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Reduced Voltage V2", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Uncorrected dosimeter reading with negative polarity -V1", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Corresponding accelerator Monitor Units", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_kelec.setText("")
        self.label_ks.setText("")
        self.label_abs_ref.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"percent variation from baseline value", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Absorbed dose to water at reference depth", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Corrected dosimeter reading at voltage V1", None))
        self.label_percent_variation.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Polarity correction factor", None))
        self.label_ktp.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"electrometer calibration factor", None))
        self.label_kpol.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Recombination correction factor", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Temperature pressure correction factor Ktp ", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Ndwq0", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Dose maximum depth", None))
        self.label_ndwq.setText("")
        self.label_abs_dmax.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Absorbed dose to water at depth of Dmax", None))
        self.label_mcrt.setText("")
        self.label_dmax.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Kqqo", None))
        self.label_kqq0.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))

        self.lineEdit_elec_calib.setText("1")
    # retranslateUi

    def Contact(self):
        msgBox = QMessageBox()
        #msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Thirumurugan Elango \nMedical Physics Resident \nCancer Institute(WIA) Adyar \nemail id: thiru20@pm.me")
        msgBox.setWindowTitle("Contact")
        #msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBox.exec()

    def license(self):
        msgBox = QMessageBox()
        #msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Determination of the absorbed dose to water in a high-energy photon beam."
                           "\nCopyright (C) <2021>  <Thirumurugan Elango>"
                           "\nThis program is free software: you can redistribute it and/or modify"
                           "\n it under the terms of the GNU General Public License as published by"
                           "\nthe Free Software Foundation, either version 3 of the License"
                           "\nThis program is distributed in the hope that it will be useful,"
                           "\nbut WITHOUT ANY WARRANTY; without even the implied warranty of"
                           "\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
                           "\nGNU General Public License for more details."
                           "\nYou should have received a copy of the GNU General Public License"
                           "\nalong with this program.  If not, see <https://www.gnu.org/licenses/>.")
        msgBox.setWindowTitle("License")
        #msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBox.exec()


    def select_energy(self):
        '''selecting linac energy'''
        file_name = self.comboBox_linac.currentText()
        self.comboBox_energy.clear()
        df = pd.read_excel('linac_library.xlsx',file_name)
        total_item = (df.loc[:, "energy"])
        total_item_1 = total_item.count()
        self.comboBox_energy.addItem("select")
        for i in range(0, total_item_1):
            self.comboBox_energy.addItem(total_item[i])
        self.comboBox_energy.currentTextChanged.connect(self.dose_rate)
    def dose_rate(self):
        file_name = self.comboBox_linac.currentText()
        df = pd.read_excel('linac_library.xlsx', file_name)
        energy_selected = self.comboBox_energy.currentText()
        dose_rate = df.loc[lambda  df: df["energy"]== energy_selected]
        dose_rate = dose_rate.loc[:,'dose_rate']
        dose_rate =dose_rate.values.tolist()
        dose_rate = dose_rate[0]
        #dose_rate = dose_rate.values[1]
        print(dose_rate)
        self.comboBox_dose_rate.clear()
        self.comboBox_dose_rate.addItem(str(dose_rate))

    def water_phantom(self):
        if self.comboBox_phantom_2.currentText() == "water phantom":
            self.label_19.setText("water phantom")
        elif self.comboBox_phantom_2.currentText() == "virtual water":
            df = pd.read_excel("detector_library.xlsx",'detectors',engine="openpyxl")
            depth = df.loc[0,"virtual_water_depth"]
            self.label_19.setText(str(depth))
            global depth_to_print
            depth_to_print = str(depth)


    def beam_quality(self):
        global tpr_2010
        tpr_20 = float(self.lineEdit_tpr_20.text())
        tpr_10 = float(self.lineEdit_tpr_10.text())
        tpr_2010 =tpr_20/tpr_10
        self.label_tpr_2010.setText(str(tpr_2010))
        file_name = self.comboBox_linac.currentText()
        df = pd.read_excel('linac_library.xlsx', file_name)
        energy_selected = self.comboBox_energy.currentText()
        tpr_value = df.loc[lambda  df: df["energy"]== energy_selected]
        print(tpr_value)
        tpr_value = tpr_value.loc[:, 'tpr2010']
        tpr_value = tpr_value.values.tolist()
        print(len(tpr_value))
        tpr_value = tpr_value[0]
        diff_tpr = tpr_2010 - tpr_value
        self.label_tpr_var.setText(str(diff_tpr))
        if abs(diff_tpr) >= 0.009:
            self.label_tpr_decision.setText('action needed')
        elif abs(diff_tpr) < 0.009:
            self.label_tpr_decision.setText("Beam Quality is within tolerance")


    def list_beam_quality_correction(self):
        global beam_quality_values , PTW_30001_30010_farmer , PTW_30002_30011_farmer,PTW_30004_30012_farmer,PTW_30006_30013_farmer
        global PTW_31002_flexible, PTW_31003_flexible, PTW_31006_PinPoint, PTW_31014_PinPoint, SNC_100700_0_Farmer,SNC_100700_1_Farmer
        global Victoreen_Radocon_III_550,Victoreen_Radocon_II_555,Victoreen_30_348,Victoreen_30_351,Victoreen_30_349
        global Victoreen_30_361, Scdx_Wellhofer_CC01, Scdx_Wellhofer_CC04_IC04, Scdx_Wellhofer_CC08_IC05_IC06
        global Scdx_Wellhofer_CC13_IC10_IC15, Scdx_Wellhofer_CC25_IC25, Scdx_Wellhofer_FC23_C_IC28_Farmer_shortened
        global Scdx_Wellhofer_FC65_P_IC69_Farmer,Scdx_Wellhofer_FC65_G_IC70_Farmer,Capintec_PR_05P_mini,Capintec_PR_05_mini
        global Capintec_PR_06_C_G_Farmer,Exradin_A2_Spokas,Exradin_T2_Spokas,Exradin_A1_mini_Shonka,Exradin_T1_mini_Shonka
        global Exradin_A12_Farmer,Far_West_Tech_IC_18,FZH_TK_01,Nuclear_Assoc_30_750,Nuclear_Assoc_30_749,Nuclear_Assoc_30_744
        global Nuclear_Assoc_30_716,Nuclear_Assoc_30_753_Farmer_shortened,Nuclear_Assoc_30_751_Farmer,Nuclear_Assoc_30_752_Farmer
        global NE_2515,NE_2515_3,NE_2577,NE_2505_Farmer,NE_2505_A_Farmer,NE_2505_3_3A_Farmer,NE_2505_3_3B_Farmer,NE_2571_Farmer
        global NE_2581_Farmer,NE_2561_2611_Sec_Std,PTW_23323_micro,PTW_23331_rigid,PTW_23332_rigid,PTW_23333

        beam_quality_values = [0.50,0.53,0.56,0.59,0.62,0.65,0.68,0.70,0.72,0.74,0.76,0.78,0.80,0.82,0.84]
        PTW_30001_30010_farmer = [1.004,1.003,1.001,0.999,0.997,0.994,0.990,0.988,0.985,0.981,0.976,0.969,0.962,0.955,0.943]
        PTW_30002_30011_farmer = [1.006,1.004,1.001,0.999,0.997,0.994,0.992,0.990,0.987,0.984,0.980,0.973,0.967,0.959,0.948]
        PTW_30004_30012_farmer = [1.006,1.005,1.002,1.000,0.999,0.996,0.994,0.992,0.989,0.986,0.982,0.976,0.969,0.962,0.950]
        PTW_30006_30013_farmer = [1.002,1.002,1.000,0.999,0.997,0.994,0.990,0.988,0.984,0.980,0.975,0.968,0.960,0.952,0.940]
        PTW_31002_flexible = [1.003,1.002,1.000,0.999,0.997,0.994,0.990,0.988,0.984,0.980,0.975,0.968,0.960,0.952,0.940]
        PTW_31003_flexible = [1.003,1.002,1.000,0.999,0.997,0.994,0.990,0.988,0.984,0.980,0.975,0.968,0.960,0.952,0.940]
        PTW_31006_PinPoint = [1.004,1.003,1.001,0.999,0.998,0.995,0.992,0.989,0.985,0.980,0.974,0.966,0.959,0.951,0.940]
        PTW_31014_PinPoint = [1.004,1.003,1.001,0.999,0.998,0.995,0.992,0.989,0.985,0.980,0.975,0.967,0.959,0.952,0.941]
        SNC_100700_0_Farmer = [1.005,1.004,1.001,0.999,0.998,0.995,0.992,0.989,0.986,0.981,0.976,0.969,0.962,0.954,0.943]
        SNC_100700_1_Farmer = [1.007,1.006,1.003,1.001,0.999,0.997,0.995,0.993,0.990,0.986,0.983,0.976,0.969,0.961,0.951]
        Victoreen_Radocon_III_550 = [1.005,1.004,1.001,0.998,0.996,0.993,0.989,0.986,0.983,0.979,0.975,0.968,0.961,0.954,0.943]
        Victoreen_Radocon_II_555 = [1.005,1.003,1.000,0.997,0.995,0.990,0.986,0.983,0.979,0.975,0.970,0.963,0.956,0.949,0.938]
        Victoreen_30_348 = [1.004,1.003,1.000,0.998,0.996,0.992,0.989,0.986,0.982,0.978,0.973,0.966,0.959,0.951,0.940]
        Victoreen_30_351 = [1.004,1.002,1.000,0.998,0.996,0.992,0.989,0.986,0.983,0.979,0.974,0.967,0.960,0.952,0.941]
        Victoreen_30_349 = [1.003,1.002,1.000,0.998,0.996,0.992,0.989,0.986,0.983,0.980,0.976,0.969,0.962,0.954,0.942]
        Victoreen_30_361 = [1.004,1.003,1.000,0.998,0.996,0.992,0.989,0.986,0.983,0.979,0.974,0.967,0.960,0.953,0.942]
        Scdx_Wellhofer_CC01 = [1.002,1.002,1.002,1.001,1.000,0.999,0.996,0.994,0.991,0.986,0.981,0.972,0.964,0.956,0.944]
        Scdx_Wellhofer_CC04_IC04 = [1.001,1.001,1.001,1.000,0.999,0.997,0.995,0.992,0.989,0.984,0.979,0.970,0.962,0.953,0.941]
        Scdx_Wellhofer_CC08_IC05_IC06 = [1.001,1.001,1.001,1.000,0.999,0.997,0.995,0.993,0.989,0.985,0.980,0.972,0.964,0.955,0.943]
        Scdx_Wellhofer_CC13_IC10_IC15 = [1.001,1.001,1.001,1.000,0.999,0.997,0.995,0.993,0.989,0.985,0.980,0.972,0.964,0.955,0.943]
        Scdx_Wellhofer_CC25_IC25 = [1.001,1.001,1.001,1.000,0.999,0.997,0.995,0.993,0.989,0.985,0.980,0.972,0.964,0.955,0.943]
        Scdx_Wellhofer_FC23_C_IC28_Farmer_shortened = [1.001,1.001,1.001,1.000,0.999,0.997,
                                                       0.995,0.993,0.990,0.985,0.980,0.972,0.964,0.955,0.943]
        Scdx_Wellhofer_FC65_P_IC69_Farmer = [1.003,1.002,1.001,0.999,0.998,0.995,0.993,
                                             0.990,0.986,0.981,0.976,0.968,0.960,0.952,0.940]
        Scdx_Wellhofer_FC65_G_IC70_Farmer = [1.005,1.004,1.002,1.000,0.998,0.997,0.995,
                                             0.992,0.989,0.985,0.981,0.973,0.966,0.958,0.947]
        Capintec_PR_05P_mini = [1.004,1.003,1.002,1.001,1.000,0.998,0.996,0.994,0.991,0.987,0.983,0.975,0.968,0.960,0.949]
        Capintec_PR_05_mini = [1.004,1.003,1.002,1.001,1.000,0.998,0.996,0.994,0.991,0.987,0.983,0.975,0.968,0.960,0.949]
        Capintec_PR_06_C_G_Farmer = [1.001,1.001,1.000,0.998,0.998,0.995,0.992,0.990,0.988,0.984,0.980,0.972,0.965,0.956,0.944]
        Exradin_A2_Spokas = [1.001,1.001,1.001,1.000,0.999,0.997,0.996,0.994,0.992,0.989,0.986,0.979,0.971,0.962,0.949]
        Exradin_T2_Spokas = [1.002,1.001,0.999,0.996,0.993,0.988,0.984,0.980,0.977,0.973,0.969,0.962,0.954,0.946,0.934]
        Exradin_A1_mini_Shonka = [1.002,1.002,1.001,1.000,1.000,0.998,0.996,0.994,0.991,0.986,0.982,0.974,0.966,0.957,0.945]
        Exradin_T1_mini_Shonka = [1.003,1.001,0.999,0.996,0.993,0.988,0.984,0.980,0.975,0.970,0.965,0.957,0.949,0.942,0.930]
        Exradin_A12_Farmer = [1.001,1.001,1.000,1.000,0.999,0.997,0.994,0.992,0.990,0.986,0.981,0.974,0.966,0.957,0.944]
        Far_West_Tech_IC_18 = [1.005,1.003,1.000,0.997,0.993,0.988,0.983,0.979,0.976,0.971,0.966,0.959,0.953,0.945,0.934]
        FZH_TK_01 = [1.002,1.001,1.000,0.998,0.996,0.993,0.990,0.987,0.984,0.980,0.975,0.968,0.960,0.952,0.939]
        Nuclear_Assoc_30_750 = [1.001,1.001,1.000,0.999,0.998,0.996,0.994,0.991,0.988,0.984,0.979,0.971,0.963,0.954,0.941]
        Nuclear_Assoc_30_749 = [1.001,1.000,1.000,0.999,0.998,0.996,0.994,0.992,0.989,0.984,0.980,0.972,0.964,0.956,0.942]
        Nuclear_Assoc_30_744 = [1.001,1.000,1.000,0.999,0.998,0.996,0.994,0.992,0.989,0.984,0.980,0.972,0.964,0.956,0.942]
        Nuclear_Assoc_30_716 = [1.001,1.000,1.000,0.999,0.998,0.996,0.994,0.992,0.989,0.984,0.980,0.972,0.964,0.956,0.942]
        Nuclear_Assoc_30_753_Farmer_shortened = [1.001,1.000,1.000,0.999,0.998,0.996,0.994,
                                                 0.992,0.989,0.985,0.980,0.973,0.965,0.956,0.943]
        Nuclear_Assoc_30_751_Farmer = [1.002,1.002,1.000,0.999,0.997,0.994,0.991,0.989,
                                       0.985,0.981,0.977,0.969,0.961,0.953,0.940]
        Nuclear_Assoc_30_752_Farmer = [1.004,1.003,1.001,1.000,0.998,0.996,0.993,0.991,
                                       0.989,0.985,0.981,0.974,0.967,0.959,0.947]
        NE_2515 = [1.001,1.001,1.000,0.999,0.997,0.994,0.991,0.988,0.984,0.980,0.975,0.967,0.959,0.950,0.937]
        NE_2515_3 = [1.005,1.004,1.002,1.000,0.998,0.995,0.993,0.991,0.989,0.986,0.982,0.975,0.969,0.961,0.949]
        NE_2577 = [1.005,1.004,1.002,1.000,0.998,0.995,0.993,0.991,0.989,0.986,0.982,0.975,0.969,0.961,0.949]
        NE_2505_Farmer = [1.001,1.001,1.000,0.999,0.997,0.994,0.991,0.988,0.984,0.980,0.975,0.967,0.959,0.950,0.937]
        NE_2505_A_Farmer = [1.005,1.003,1.001,0.997,0.995,0.990,0.985,0.982,0.978,0.974,0.969,0.962,0.955,0.947,0.936]
        NE_2505_3_3A_Farmer = [1.005,1.004,1.002,1.000,0.998,0.995,0.993,0.991,0.989,0.986,0.982,0.975,0.969,0.961,0.949]
        NE_2505_3_3B_Farmer = [1.006,1.004,1.001,0.999,0.996,0.991,0.987,0.984,0.980,0.976,0.971,0.964,0.957,0.950,0.938]
        NE_2571_Farmer = [1.005,1.004,1.002,1.000,0.998,0.995,0.993,0.991,0.989,0.986,0.982,0.975,0.969,0.961,0.949]
        NE_2581_Farmer = [1.005,1.003,1.001,0.998,0.995,0.991,0.986,0.983,0.980,0.975,0.970,0.963,0.956,0.949,0.937]
        NE_2561_2611_Sec_Std = [1.006,1.004,1.001,0.999,0.998,0.994,0.992,0.990,0.988,0.985,0.982,0.975,0.969,0.961,0.949]
        PTW_23323_micro = [1.003,1.003,1.000,0.999,0.997,0.993,0.990,0.987,0.984,0.980,0.975,0.967,0.960,0.953,0.941]
        PTW_23331_rigid = [1.004,1.003,1.000,0.999,0.997,0.993,0.990,0.988,0.985,0.982,0.978,0.971,0.964,0.956,0.945]
        PTW_23332_rigid = [1.004,1.003,1.001,0.999,0.997,0.994,0.990,0.988,0.984,0.980,0.976,0.968,0.961,0.954,0.943]
        PTW_23333 = [1.004,1.003,1.001,0.999,0.997,0.994,0.990,0.988,0.985,0.981,0.976,0.969,0.963,0.955,0.943]



    def calculation(self):
        df = pd.read_excel("detector_library.xlsx",'detectors',engine="openpyxl")
        detector_no = self.comboBox_detector.currentText()
        ref_detector = df.loc[lambda  df: df["serial_no"]== int(detector_no)]
        global ref_temp_celsius, ref_pressure_mbar, kpol ,voltage_ratio,a0,a1,a2,kq,abs_ref_depth,abs_dmax,ktp,dmax_result
        ref_temp_list = []
        ref_temp = ref_detector.loc[:,"temperature_from_calib_certificate_celsius"]
        ref_temp_list = ref_temp.values.tolist()
        print(len(ref_temp_list))
        ref_temp_celsius = ref_temp_list[0]
        print(ref_temp_celsius)
        ref_pressure_list = []
        ref_pressure = ref_detector.loc[:,"pressure_from_calibration_certificate_mBar"]
        ref_pressure_list = ref_pressure.values.tolist()
        ref_pressure_mbar = ref_pressure_list[0]
        print(ref_pressure_mbar)
        ktp = ((273.2 + float(self.lineEdit_temp.text()))/(273.2 + ref_temp_celsius)) * (ref_pressure_mbar/float(self.lineEdit_pressure.text()))
        self.label_ktp.setText(str(round(ktp,4)))
        kelec = float(self.lineEdit_elec_calib.text())
        self.label_kelec.setText(str(kelec))
        voltage_ratio = float(self.lineEdit_v1.text())/float(self.lineEdit_v2.text())
        if self.comboBox_2.currentText() == "pulsed radiation":
            if voltage_ratio == 2.0:
                a0 = 2.337
                a1 = -3.636
                a2 = 2.299
            elif voltage_ratio == 2.5:
                a0 = 1.474
                a1 = -1.587
                a2 = 1.114
            elif voltage_ratio == 3.0:
                a0 = 1.198
                a1 = -0.875
                a2 = 0.677
            elif voltage_ratio == 3.5:
                a0 = 1.080
                a1 = -0.542
                a2 = 0.463
            elif voltage_ratio == 4.0:
                a0 = 1.022
                a1 = -0.363
                a2 = 0.341
            elif voltage_ratio == 5.0:
                a0 = 0.975
                a1 = -0.188
                a2 = 0.214
        elif self.comboBox_2.currentText() == "pulsed scanned radiation":
            if voltage_ratio == 2.0:
                a0 = 4.711
                a1 = -8.242
                a2 = 4.533
            elif voltage_ratio == 2.5:
                a0 = 2.719
                a1 = -3.977
                a2 = 2.261
            elif voltage_ratio == 3.0:
                a0 = 2.001
                a1 = -2.402
                a2 = 1.404
            elif voltage_ratio == 3.5:
                a0 = 1.665
                a1 = -1.647
                a2 = 0.984
            elif voltage_ratio == 4.0:
                a0 = 1.468
                a1 = -1.200
                a2 = 0.734
            elif voltage_ratio == 5.0:
                a0 = 1.279
                a1 = -0.750
                a2 = 0.474
        if self.comboBox.currentText() == "positive":
            kpol = (abs(float(self.lineEdit_m1.text())) + abs(float(self.lineEdit_mminus.text()))) / (2 * abs(float(self.lineEdit_m1.text())))
        elif self.comboBox.currentText() == "Negative":
            kpol = (abs(float(self.lineEdit_m1.text())) + abs(float(self.lineEdit_mminus.text()))) / (2* abs(
                float(self.lineEdit_mminus.text())))
        self.label_kpol.setText(str(round(kpol,4)))
        global ks
        if self.comboBox.currentText() == "positive":
            ks = a0 + (a1 * (float(self.lineEdit_m1.text()) / float(self.lineEdit_m2.text()))) + \
                 ((a2) * (float(self.lineEdit_m1.text()) / float(self.lineEdit_m2.text())) ** 2)
        elif self.comboBox.currentText() == "Negative":
            ks = a0 + (a1 * (float(self.lineEdit_mminus.text()) / float(self.lineEdit_m2.text()))) + \
                 ((a2) * (float(self.lineEdit_mminus.text()) / float(self.lineEdit_m2.text())) ** 2)
        self.label_ks.setText(str(round(ks, 4)))

        global mu
        if self.comboBox.currentText() == "positive":
            mu = float(self.lineEdit_m1.text())/ float(self.lineEdit_mu.text())
        elif self.comboBox.currentText() == "Negative":
            mu = abs(float(self.lineEdit_mminus.text()))/float(self.lineEdit_mu.text())

        print(mu)
        self.list_beam_quality_correction()
        global ref_detector_type
        ref_detector_type = ref_detector.loc[:, "Chamber_type"]
        ref_detector_type = ref_detector_type.values.tolist()
        ref_detector_type = ref_detector_type[0]

        beam_quality_lists_import = beam_quality_values
        print(beam_quality_lists_import)
        print(tpr_2010)
        print(ref_detector_type)
        if ref_detector_type == 'PTW_30006_30013_farmer':
            ref_detector_name = PTW_30006_30013_farmer
        elif ref_detector_type == "PTW_30004_30012_farmer":
            ref_detector_name = PTW_30004_30012_farmer
        elif ref_detector_type == "PTW_23323_micro":
            ref_detector_name = PTW_23323_micro
        elif ref_detector_type == "PTW_23331_rigid":
            ref_detector_name = PTW_23331_rigid
        elif ref_detector_type == "PTW_23332_rigid":
            ref_detector_name = PTW_23332_rigid
        elif ref_detector_type == "PTW_23333_3mm_cap":
            ref_detector_name = PTW_23333
        elif ref_detector_type == "PTW_23333_4.6_mm_cap":
            ref_detector_name = PTW_23333
        elif ref_detector_type == "PTW_30010_farmer":
            ref_detector_name = PTW_30001_30010_farmer
        elif ref_detector_type == "PTW_30001_farmer":
            ref_detector_name = PTW_30001_30010_farmer
        elif ref_detector_type == "PTW_31002_flexible":
            ref_detector_name = PTW_31002_flexible
        elif ref_detector_type == "PTW_31003_flexible":
            ref_detector_name = PTW_31003_flexible
        elif ref_detector_type == "PTW_31006_PinPoint":
            ref_detector_name = PTW_31006_PinPoint
        elif ref_detector_type == "PTW_31014_PinPoint":
            ref_detector_name = PTW_31014_PinPoint
        elif ref_detector_type == "SNC_100700_0_Farmer":
            ref_detector_name = SNC_100700_0_Farmer
        elif ref_detector_type == "SNC_100700_1_Farmer":
            ref_detector_name = SNC_100700_1_Farmer
        elif ref_detector_type == "Victoreen_Radocon_III_550":
            ref_detector_name = Victoreen_Radocon_III_550
        elif ref_detector_type == "Victoreen_Radocon_II_555":
            ref_detector_name = Victoreen_Radocon_II_555
        elif ref_detector_type == "Victoreen_30_348":
            ref_detector_name = Victoreen_30_348
        elif ref_detector_type == "Victoreen_30_351":
            ref_detector_name = Victoreen_30_351
        elif ref_detector_type == "Victoreen_30_349":
            ref_detector_name = Victoreen_30_349
        elif ref_detector_type == "Victoreen_30_361":
            ref_detector_name = Victoreen_30_361
        elif ref_detector_type == "Scdx_Wellhofer_CC01":
            ref_detector_name = Scdx_Wellhofer_CC01
        elif ref_detector_type == "Scdx_Wellhofer_CC04_IC04":
            ref_detector_name = Scdx_Wellhofer_CC04_IC04
        elif ref_detector_type == "Scdx_Wellhofer_CC13_IC10_IC15":
            ref_detector_name = Scdx_Wellhofer_CC13_IC10_IC15
        elif ref_detector_type == "Scdx_Wellhofer_CC08_IC05_IC06":
            ref_detector_name = Scdx_Wellhofer_CC08_IC05_IC06
        elif ref_detector_type == "Scdx_Wellhofer_CC25_IC25":
            ref_detector_name = Scdx_Wellhofer_CC25_IC25
        elif ref_detector_type == "Scdx_Wellhofer_FC23_C_IC28_Farmer_shortened":
            ref_detector_name = Scdx_Wellhofer_FC23_C_IC28_Farmer_shortened
        elif ref_detector_type == "Scdx_Wellhofer_FC65_P_IC69_Farmer":
            ref_detector_name = Scdx_Wellhofer_FC65_P_IC69_Farmer
        elif ref_detector_type == "Scdx_Wellhofer_FC65_G_IC70_Farmer":
            ref_detector_name = Scdx_Wellhofer_FC65_G_IC70_Farmer
        elif ref_detector_type == "Capintec_PR_05P_mini":
            ref_detector_name = Capintec_PR_05P_mini
        elif ref_detector_type == "Capintec_PR_05_mini":
            ref_detector_name = Capintec_PR_05_mini
        elif ref_detector_type == "Capintec_PR_06_C_G_Farmer":
            ref_detector_name = Capintec_PR_06_C_G_Farmer
        elif ref_detector_type == "Exradin_A2_Spokas":
            ref_detector_name = Exradin_A2_Spokas
        elif ref_detector_type == "Exradin_T2_Spokas":
            ref_detector_name = Exradin_T2_Spokas
        elif ref_detector_type == "Exradin_A1_mini_Shonka":
            ref_detector_name = Exradin_A1_mini_Shonka
        elif ref_detector_type == "Exradin_T1_mini_Shonka":
            ref_detector_name =  Exradin_T1_mini_Shonka
        elif ref_detector_type == "Exradin_A12_Farmer":
            ref_detector_name =  Exradin_A12_Farmer
        elif ref_detector_type == "Far_West_Tech_IC_18":
            ref_detector_name =  Far_West_Tech_IC_18
        elif ref_detector_type == "FZH_TK_01":
            ref_detector_name =  FZH_TK_01
        elif ref_detector_type == "Nuclear_Assoc_30_750":
            ref_detector_name =  Nuclear_Assoc_30_750
        elif ref_detector_type == "Nuclear_Assoc_30_749":
            ref_detector_name =  Nuclear_Assoc_30_749
        elif ref_detector_type == "Nuclear_Assoc_30_744":
            ref_detector_name =  Nuclear_Assoc_30_744
        elif ref_detector_type == "Nuclear_Assoc_30_716":
            ref_detector_name =  Nuclear_Assoc_30_716
        elif ref_detector_type == "Nuclear_Assoc_30_753_Farmer_shortened":
            ref_detector_name =  Nuclear_Assoc_30_753_Farmer_shortened
        elif ref_detector_type == "Nuclear_Assoc_30_752_Farmer":
            ref_detector_name =  Nuclear_Assoc_30_752_Farmer
        elif ref_detector_type == "Nuclear_Assoc_30_751_Farmer":
            ref_detector_name =  Nuclear_Assoc_30_751_Farmer
        elif ref_detector_type == "NE_2515":
            ref_detector_name =  NE_2515
        elif ref_detector_type == "NE_2515_3":
            ref_detector_name =  NE_2515_3
        elif ref_detector_type == "NE_2577":
            ref_detector_name =  NE_2577
        elif ref_detector_type == "NE_2505_Farmer":
            ref_detector_name =  NE_2505_Farmer
        elif ref_detector_type == "NE_2505_A_Farmer":
            ref_detector_name =  NE_2505_A_Farmer
        elif ref_detector_type == "NE_2505_3_3A_Farmer":
            ref_detector_name =  NE_2505_3_3A_Farmer
        elif ref_detector_type == "NE_2505_3_3B_Farmer":
            ref_detector_name =  NE_2505_3_3B_Farmer
        elif ref_detector_type == "NE_2571_Farmer":
            ref_detector_name =  NE_2571_Farmer
        elif ref_detector_type == "NE_2581_Farmer_PMMA_cap":
            ref_detector_name =  NE_2581_Farmer
        elif ref_detector_type == "NE_2581_Farmer_Polystyrene_cap":
            ref_detector_name =  NE_2581_Farmer
        elif ref_detector_type == "NE_2561_2611_Sec_Std":
            ref_detector_name =  NE_2561_2611_Sec_Std

        kq = np.interp(tpr_2010, beam_quality_values, ref_detector_name)
        print(kq)
        self.label_kqq0.setText(str(round(kq,4)))
        global corrected_meter_reading
        corrected_meter_reading = mu * kpol * kelec * ks * ktp
        self.label_mcrt.setText(str(round(corrected_meter_reading,4))+ "nC/MU")

        global dose_to_water

        dose_to_water = ref_detector.loc[:, "Ndw value"]
        dose_to_water = dose_to_water.values.tolist()
        dose_to_water = dose_to_water[0]
        self.label_ndwq.setText(str(round(dose_to_water,4))+" Gy/nC")
        abs_ref_depth = corrected_meter_reading * kq * dose_to_water
        self.label_abs_ref.setText(str(round(abs_ref_depth,4))+" Gy/MU")

        name_of_linac = self.comboBox_linac.currentText()
        dmax_result = pd.read_excel('linac_library.xlsx', name_of_linac)
        energy_selected = self.comboBox_energy.currentText()
        dmax_result = dmax_result.loc[lambda dmax_result: dmax_result["energy"] == energy_selected]
        if self.comboBox_phantom_2.currentText() == "water phantom":
            dmax_result = dmax_result.loc[:, 'pdd']
            dmax_result = dmax_result.values.tolist()
            dmax_result = dmax_result[0]
        elif self.comboBox_phantom_2.currentText() == "virtual water":
            dmax_result = dmax_result.loc[:, 'pdd_vw']
            dmax_result = dmax_result.values.tolist()
            dmax_result = dmax_result[0]

        abs_dmax = 100 * (abs_ref_depth/dmax_result)

        self.label_abs_dmax.setText(str(round(abs_dmax,4))+" Gy/MU")

        baseline = pd.read_excel('linac_library.xlsx', name_of_linac)
        baseline = baseline.loc[lambda base_line: baseline["energy"] == energy_selected]
        baseline = baseline.loc[:, 'output_baseline']
        baseline = baseline.values.tolist()
        baseline = baseline[0]

        global  variation_of_output
        variation_of_output = ((abs_dmax - baseline)/baseline) * 100
        self.label_percent_variation.setText(str(round(variation_of_output,4))+ " %")

        name_of_the_la = self.comboBox_linac.currentText()
        energy_selected_mv = self.comboBox_energy.currentText()
        depth_of_dmax = pd.read_excel('linac_library.xlsx', name_of_the_la)
        depth_of_dmax = depth_of_dmax.loc[lambda depth_of_dmax: depth_of_dmax["energy"] == energy_selected_mv]
        depth_of_dmax = depth_of_dmax.loc[:, 'dmax_depth']
        depth_of_dmax = depth_of_dmax.values.tolist()
        depth_of_dmax = depth_of_dmax[0]
        self.label_dmax.setText(str(round(depth_of_dmax,4))+" cm")

    def chamber_dict(self):
        global detector_details, calibration_lab,calibration_date,polarizing_potential_v,calibration_polarity_ans
        global electrometer_serial_no,electrometer_calib_place,electrometer_calib_date, calibration_quality_ans,calibration_depth_ans
        global calibration_beam_quality_ans, electrometer_calib_sep, elec_range_setting
        chamber_details_filename = pd.read_excel("detector_library.xlsx", 'detectors',engine="openpyxl")
        detector_serial_number = self.comboBox_detector.currentText()
        ref_detector_for_details = chamber_details_filename.loc[lambda chamber_details_filename: chamber_details_filename["serial_no"] == int(detector_serial_number)]
        ref_detector_for_details = ref_detector_for_details.loc[:, "Chamber_type"]
        ref_detector_for_details = ref_detector_for_details.values.tolist()
        ref_detector_for_details = ref_detector_for_details[0]

        if ref_detector_for_details == "PTW_30006_30013_farmer":
            detector_details ={"wall_material":"PMMA", "wall_thickness":"0.057 g cm",
                               "build_material":"PMMA","build_thick":"0.541 g cm"}
        elif ref_detector_for_details == "PTW_30004_30012_farmer":
            detector_details = {"wall_material":"Graphite", "wall_thickness":"0.079 g cm",
                                "build_material":"PMMA","build_thick":"0.541 g cm"}
        elif ref_detector_for_details == "PTW_30002_30011_farmer":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.079 g cm", "build_material": "PMMA",
                                "build_thick": "0.541 g cm"}
        elif ref_detector_for_details == "PTW_30010_farmer":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.057 g cm", "build_material": "PMMA",
                                "build_thick": "0.541 g cm"}
        elif ref_detector_for_details == "PTW_30001_farmer":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.045 g cm", "build_material": "PMMA",
                                "build_thick": "0.541 g cm"}
        elif ref_detector_for_details == "PTW_23323_micro":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.197 g cm", "build_material": "PMMA",
                                "build_thick": "0.357 g cm"}
        elif ref_detector_for_details == "PTW_23331_rigid":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.060 g cm", "build_material": "PMMA",
                                "build_thick": "0.345 g cm"}
        elif ref_detector_for_details == "PTW_23332_rigid":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.054 g cm", "build_material": "PMMA",
                                "build_thick": "0.357 g cm"}
        elif ref_detector_for_details == "PTW_23333_3mm_cap":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.059 g cm", "build_material": "PMMA",
                                "build_thick": "0.356 g cm"}
        elif ref_detector_for_details == "PTW_23333_4.6_mm_cap":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.053 g cm", "build_material": "PMMA",
                                "build_thick": "0.551 g cm"}
        elif ref_detector_for_details == "PTW_31002_flexible":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.078 g cm", "build_material": "PMMA",
                                "build_thick": "0.357 g cm"}
        elif ref_detector_for_details == "PTW_31003_flexible":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.078 g cm", "build_material": "PMMA",
                                "build_thick": "0.357 g cm"}
        elif ref_detector_for_details == "PTW_31006_PinPoint":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.078 g cm", "build_material": "    ",
                                "build_thick": "   g cm"}
        elif ref_detector_for_details == "PTW_31014_PinPoint":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.086 g cm", "build_material": "    ",
                                "build_thick": "   g cm"}
        elif ref_detector_for_details == "SNC_100700_0_Farmer":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.060 g cm", "build_material": "PMMA",
                                "build_thick": "0.536 g cm"}
        elif ref_detector_for_details == "SNC_100700_1_Farmer":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.085 g cm", "build_material": "PMMA",
                                "build_thick": "0.536 g cm"}
        elif ref_detector_for_details == "Victoreen_Radocon_III_550":
            detector_details = {"wall_material": "Delrin", "wall_thickness": "0.529 g cm", "build_material": "    ",
                                "build_thick": "0.536 g cm"}
        elif ref_detector_for_details == "Victoreen_Radocon_II_555":
            detector_details = {"wall_material": "Polystyrene", "wall_thickness": "0.117 g cm", "build_material": "PMMA",
                                "build_thick": "0.481 g cm"}
        elif ref_detector_for_details == "Victoreen_30_348":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.060 g cm", "build_material": "PMMA",
                                "build_thick": "0.360 g cm"}
        elif ref_detector_for_details == "Victoreen_30_351":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.060 g cm", "build_material": "PMMA",
                                "build_thick": "0.360 g cm"}
        elif ref_detector_for_details == "Victoreen_30_349":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.060 g cm", "build_material": "PMMA",
                                "build_thick": "0.360 g cm"}
        elif ref_detector_for_details == "Victoreen_30_361":
            detector_details = {"wall_material": "PMMA", "wall_thickness": "0.144 g cm", "build_material": "PMMA",
                                "build_thick": "0.360 g cm"}
        elif ref_detector_for_details == "Scdx_Wellhofer_CC01":
            detector_details = {"wall_material": "C-522", "wall_thickness": "0.088 g cm", "build_material": "    ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Scdx_Wellhofer_CC04_IC04":
            detector_details = {"wall_material": "C-522", "wall_thickness": "0.070 g cm", "build_material": "    ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Scdx_Wellhofer_CC13_IC10_IC15":
            detector_details = {"wall_material": "C-522", "wall_thickness": "0.070 g cm", "build_material": "    ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Scdx_Wellhofer_CC08_IC05_IC06":
            detector_details = {"wall_material": "C-522", "wall_thickness": "0.070 g cm", "build_material": "    ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Scdx_Wellhofer_CC25_IC25":
            detector_details = {"wall_material": "C-522", "wall_thickness": "0.070 g cm", "build_material": "    ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Scdx_Wellhofer_FC23_C_IC28_Farmer_shortened":
            detector_details = {"wall_material": "C-522", "wall_thickness": "0.070 g cm", "build_material": "POM",
                                "build_thick": "0.560 g cm"}
        elif ref_detector_for_details == "Scdx_Wellhofer_FC65_P_IC69_Farmer":
            detector_details = {"wall_material": "C-522", "wall_thickness": "0.057 g cm", "build_material": "POM",
                                "build_thick": "0.560 g cm"}
        elif ref_detector_for_details == "Scdx_Wellhofer_FC65_G_IC70_Farmer":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.073 g cm", "build_material": "POM",
                                "build_thick": "0.560 g cm"}
        elif ref_detector_for_details == "Capintec_PR_05P_mini":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.220 g cm", "build_material": "Polystyrene",
                                "build_thick": "0.568 g cm"}
        elif ref_detector_for_details == "Capintec_PR_05_mini":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.220 g cm", "build_material": "Polystyrene",
                                "build_thick": "0.568 g cm"}

        elif ref_detector_for_details == "Capintec_PR_06_C_G_Farmer":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.050 g cm", "build_material": "   ",
                                "build_thick": "  g cm"}
        elif ref_detector_for_details == "Exradin_A2_Spokas":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.176 g cm", "build_material": "C-552",
                                "build_thick": " 0.352 g cm"}
        elif ref_detector_for_details == "Exradin_T2_Spokas":
            detector_details = {"wall_material": "A-150", "wall_thickness": "0.113 g cm", "build_material": "A-150",
                                "build_thick": " 0.451 g cm"}
        elif ref_detector_for_details == "Exradin_A1_mini_Shonka":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.176 g cm", "build_material": "C-552",
                                "build_thick": " 0.352 g cm"}
        elif ref_detector_for_details == "Exradin_T1_mini_Shonka":
            detector_details = {"wall_material": "A-150", "wall_thickness": "0.113 g cm", "build_material": "A-150",
                                "build_thick": " 0.451 g cm"}
        elif ref_detector_for_details == "Exradin_A12_Farmer":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.088 g cm", "build_material": "C-552",
                                "build_thick": " 0.493 g cm"}
        elif ref_detector_for_details == "Far_West_Tech_IC_18":
            detector_details = {"wall_material": "A-150", "wall_thickness": "0.183 g cm", "build_material": "A-150",
                                "build_thick": " 0.386 g cm"}
        elif ref_detector_for_details == "FZH_TK_01":
            detector_details = {"wall_material": "Delrin", "wall_thickness": "0.071 g cm", "build_material": "Delrin",
                                "build_thick": " 0.430 g cm"}
        elif ref_detector_for_details == "Nuclear_Assoc_30_750":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.068 g cm", "build_material": "   ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Nuclear_Assoc_30_749":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.068 g cm", "build_material": "   ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Nuclear_Assoc_30_744":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.068 g cm", "build_material": "   ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Nuclear_Assoc_30_716":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.068 g cm", "build_material": "   ",
                                "build_thick": " g cm"}
        elif ref_detector_for_details == "Nuclear_Assoc_30_753_Farmer_shortened":
            detector_details = {"wall_material": "C-552", "wall_thickness": "0.068 g cm", "build_material": "Delrin",
                                "build_thick": " 0.560 g cm"}
        elif ref_detector_for_details == "Nuclear_Assoc_30_752_Farmer":
            detector_details = {"wall_material": "Graphitr", "wall_thickness": "0.072 g cm", "build_material": "Delrin",
                                "build_thick": " 0.560 g cm"}
        elif ref_detector_for_details == "Nuclear_Assoc_30_751_Farmer":
            detector_details = {"wall_material": "Delrin", "wall_thickness": "0.056 g cm", "build_material": "Delrin",
                                "build_thick": " 0.560 g cm"}
        elif ref_detector_for_details == "NE_2515":
            detector_details = {"wall_material": "Tufnol", "wall_thickness": "0.074 g cm", "build_material": "PMMA",
                                "build_thick": " 0.543 g cm"}
        elif ref_detector_for_details == "NE_2515_3":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.066 g cm", "build_material": "PMMA",
                                "build_thick": " 0.543 g cm"}
        elif ref_detector_for_details == "NE_2577":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.066 g cm", "build_material": "Delrin",
                                "build_thick": " 0.552 g cm"}
        elif ref_detector_for_details == "NE_2505_Farmer":
            detector_details = {"wall_material": "Tufnol", "wall_thickness": "0.075 g cm", "build_material": "PMMA",
                                "build_thick": " 0.545 g cm"}
        elif ref_detector_for_details == "NE_2505_A_Farmer":
            detector_details = {"wall_material": "nylon66", "wall_thickness": "0.063 g cm", "build_material": "PMMA",
                                "build_thick": " 0.545 g cm"}
        elif ref_detector_for_details == "NE_2505_3_3A_Farmer":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.065 g cm", "build_material": "PMMA",
                                "build_thick": " 0.551 g cm"}
        elif ref_detector_for_details == "NE_2505_3_3B_Farmer":
            detector_details = {"wall_material": "Nylon66", "wall_thickness": "0.041 g cm", "build_material": "PMMA",
                                "build_thick": " 0.551 g cm"}
        elif ref_detector_for_details == "NE_2571_Farmer":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.065 g cm", "build_material": "Delrin",
                                "build_thick": " 0.551 g cm"}
        elif ref_detector_for_details == "NE_2581_Farmer_PMMA_cap":
            detector_details = {"wall_material": "A-150", "wall_thickness": "0.041 g cm", "build_material": "PMMA",
                                "build_thick": " 0.584 g cm"}
        elif ref_detector_for_details == "NE_2581_Farmer_Polystyrene_cap":
            detector_details = {"wall_material": "A-150", "wall_thickness": "0.041 g cm", "build_material": "Polystyrene",
                                "build_thick": " 0.584 g cm"}
        elif ref_detector_for_details == "NE_2561_2611_Sec_Std":
            detector_details = {"wall_material": "Graphite", "wall_thickness": "0.090 g cm", "build_material": "Delrin",
                                "build_thick": " 0.600 g cm"}


        calibration_details_full = chamber_details_filename.loc[lambda chamber_details_filename: chamber_details_filename["serial_no"] == int(detector_serial_number)]
        calibration_lab = calibration_details_full.loc[:, "calibration_laboratory"]
        calibration_lab = calibration_lab.values.tolist()
        calibration_lab = calibration_lab[0]
        calibration_date = calibration_details_full.loc[:, "calibration_date"]
        calibration_date = calibration_date.values.tolist()
        calibration_date = calibration_date[0]
        polarizing_potential_v = calibration_details_full.loc[:,"polarizing_potential"]
        polarizing_potential_v = polarizing_potential_v.values.tolist()
        polarizing_potential_v = polarizing_potential_v[0]
        calibration_polarity_ans = calibration_details_full.loc[:,"calibration_polarity"]
        calibration_polarity_ans = calibration_polarity_ans.values.tolist()
        calibration_polarity_ans = calibration_polarity_ans[0]
        calibration_quality_ans = calibration_details_full.loc[:,"calibration_quality"]
        calibration_quality_ans = calibration_quality_ans.values.tolist()
        calibration_quality_ans = calibration_quality_ans[0]
        calibration_depth_ans = calibration_details_full.loc[:, "calibration_depth"]
        calibration_depth_ans = calibration_depth_ans.values.tolist()
        calibration_depth_ans = calibration_depth_ans[0]
        if calibration_quality_ans == "cobalt_60":
            calibration_beam_quality_ans = " - "
        elif calibration_quality_ans == "photons":
            calibration_beam_quality_ans = calibration_details_full.loc[:, "photon_beam_quality"]
            calibration_beam_quality_ans = calibration_beam_quality_ans.values.tolist()
            calibration_beam_quality_ans = calibration_beam_quality_ans[0]

        electrometer_name_1 = self.comboBox_electrometer.currentText()
        electrometer_details_filename = pd.read_excel("detector_library.xlsx", 'electrometer',engine="openpyxl")
        electrometer_details_full = electrometer_details_filename.loc[lambda electrometer_details_filename: electrometer_details_filename["name"] == electrometer_name_1]
        electrometer_serial_no = electrometer_details_full.loc[:,"serial_no"]
        electrometer_serial_no = electrometer_serial_no.values.tolist()
        electrometer_serial_no = electrometer_serial_no[0]
        electrometer_calib_sep = electrometer_details_full.loc[:,"calibrated_seperately"]
        electrometer_calib_sep = electrometer_calib_sep.values.tolist()
        electrometer_calib_sep = electrometer_calib_sep[0]
        if electrometer_calib_sep == "yes":
            electrometer_calib_place = electrometer_details_full.loc[:,"calibration_lab"]
            electrometer_calib_place = electrometer_calib_place.values.tolist()
            electrometer_calib_place = electrometer_calib_place[0]
            electrometer_calib_date = electrometer_details_full.loc[:,"calibration_date"]
            electrometer_calib_date = electrometer_calib_date.values.tolist()
            electrometer_calib_date = electrometer_calib_date[0]

        elif electrometer_calib_sep == "no":
            electrometer_calib_place = "  -  "
            electrometer_calib_date = "  -  "

        elec_range_setting = electrometer_details_full.loc[:,"range_setting"]
        elec_range_setting = elec_range_setting.values.tolist()
        elec_range_setting = elec_range_setting[0]

    def printing(self):

        self.chamber_dict()
        print(detector_details.get("wall_material"))
        name_of_the_la = self.comboBox_linac.currentText()
        energy_selected_mv = self.comboBox_energy.currentText()
        depth_of_dmax = pd.read_excel('linac_library.xlsx', name_of_the_la)
        depth_of_dmax = depth_of_dmax.loc[lambda depth_of_dmax: depth_of_dmax["energy"] == energy_selected_mv]
        depth_of_dmax = depth_of_dmax.loc[:, 'dmax_depth']
        depth_of_dmax = depth_of_dmax.values.tolist()
        depth_of_dmax = depth_of_dmax[0]
        print(depth_of_dmax)
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.pdfgen import canvas
        import datetime
        def apply_scripting(textobject, text, rise):
            textobject.setFont("Helvetica-Oblique", 8)
            textobject.setRise(rise)
            textobject.textOut(text)
            textobject.setFont("Helvetica-Oblique", 12)
            textobject.setRise(0)

        canvas_obj = canvas.Canvas(self.comboBox_linac.currentText()+"_"+
                                   self.comboBox_energy.currentText()+"_"+str(datetime.date.today())+".pdf")
        canvas_obj.setPageSize(A4)
        canvas_obj.setTitle(" absorbed dose to water in a high-energy photon beam")
        canvas_obj.drawImage("logo.png", 10, 780, 40, 40)
        # Create textobject
        textobject = canvas_obj.beginText()
        textobject.setFont("Helvetica-Bold", 14)
        # Set text location (x, y)
        textobject.setTextOrigin(70, 780)
        textobject.setFillColorRGB(0.1, 0.1, 0.1)
        textobject.textOut('Determination of the absorbed dose to water in a high-energy photon beam')
        textobject.setFont('Courier', 10)
        textobject.setFillColorRGB(1, 0, 1)
        textobject.setTextOrigin(40, 730)
        textobject.textOut("User: "+self.comboBox__user.currentText())
        textobject.setTextOrigin(450, 730)
        textobject.textOut("Date: " + str(datetime.date.today()))
        textobject.setFont("Helvetica-Bold", 13)
        textobject.setTextOrigin(40, 680)
        textobject.setFillColorRGB(1, 0, 1)
        textobject.textOut("1. Radiation treatment unit and reference conditions for D")
        apply_scripting(textobject, 'w,Q', -4)
        textobject.setFont("Helvetica-Bold", 13)
        textobject.textOut(" determination")
        textobject.setTextOrigin(40, 660)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.setFillColorRGB(0.1, 0.1, 0.1)
        textobject.textOut("Accelerator: "+self.comboBox_linac.currentText())
        textobject.setTextOrigin(320, 660)
        textobject.textOut("Nominal Acc Potential: "+self.comboBox_energy.currentText())
        textobject.setTextOrigin(40, 640)
        textobject.textOut("Nominal dose rate: "+self.comboBox_dose_rate.currentText())
        textobject.setTextOrigin(320, 640)
        textobject.textOut("Beam quality, Q (TPR")
        apply_scripting(textobject, "20,10", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" ): "+str(round(tpr_2010,4)))
        textobject.setTextOrigin(40, 620)
        textobject.textOut("Reference phantom: "+self.comboBox_phantom_2.currentText())
        textobject.setTextOrigin(320, 620)
        textobject.textOut("Set up: SSD")
        textobject.setTextOrigin(40, 600)
        textobject.textOut('Reference field size: 10X10 cm')
        apply_scripting(textobject, '2', 4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.setTextOrigin(320, 600)
        textobject.textOut("Reference distance: 100 cm")
        textobject.setTextOrigin(40, 580)
        textobject.textOut("Reference depth z")
        apply_scripting(textobject, "ref", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" : "+ "10 g/cm")
        apply_scripting(textobject, '2', 4)
        if self.comboBox_phantom_2.currentText() == "virtual water":
            textobject.setTextOrigin(320,580)
            textobject.setFont("Helvetica-Oblique", 10)
            textobject.textOut("Reference depth in virtual water: "+depth_to_print+" cm")
        textobject.setFont("Helvetica-Bold", 13)
        textobject.setTextOrigin(40, 550)
        textobject.setFillColorRGB(1, 0, 1)
        print("1 ok")
        textobject.textOut("2. Ionization chamber and electrometer")
        textobject.setFillColorRGB(0.1, 0.1, 0.1)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.setTextOrigin(40, 520)
        textobject.textOut("Ionization chamber model: "+ref_detector_type+ "             "+
                           " Serial no.: "+self.comboBox_detector.currentText())
        textobject.setTextOrigin(40, 500)
        textobject.textOut("Chamber wall")
        textobject.setTextOrigin(180, 500)
        textobject.textOut("material: " + detector_details.get("wall_material"))
        textobject.setTextOrigin(340, 500)
        textobject.textOut("thickness: " + detector_details.get("wall_thickness"))
        apply_scripting(textobject, "-2", 4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.setTextOrigin(40, 480)
        textobject.textOut("Waterproof sleeve")
        textobject.setTextOrigin(180, 480)
        textobject.textOut("material: "+ detector_details.get("build_material"))
        textobject.setTextOrigin(340, 480)
        textobject.textOut("thickness: "+ detector_details.get("build_thick"))
        apply_scripting(textobject, "-2", 4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.setTextOrigin(40, 460)
        textobject.setFont("Helvetica-Bold", 10)
        textobject.textOut("Absorbed-dose-to-water calibration factor N")
        apply_scripting(textobject, "D,w,Q", -4)
        apply_scripting(textobject, '0', -7)
        textobject.setFont("Helvetica-Bold", 10)
        textobject.textOut(" = " +str(dose_to_water)+ " Gy nC")
        apply_scripting(textobject, "-1", 4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.setTextOrigin(40, 440)
        textobject.textOut("Calibration quality Q ")
        apply_scripting(textobject, '0', -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" : "+ calibration_quality_ans)
        textobject.setTextOrigin(320, 440)
        textobject.textOut("Calibration depth: " + str(calibration_depth_ans) +" g cm")
        apply_scripting(textobject, '-2', 4)
        textobject.setFont("Helvetica-Oblique", 10)
        print("2 half ok")
        textobject.setTextOrigin(40, 420)
        textobject.textOut("If Q")
        apply_scripting(textobject, "0", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" is photon beam, TPR")
        apply_scripting(textobject, "20,10 ", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" = "+str(calibration_beam_quality_ans))
        textobject.setTextOrigin(40, 400)
        textobject.textOut("Reference conditions for calibration ")
        textobject.setTextOrigin(225, 400)
        textobject.textOut("P")
        apply_scripting(textobject, "0", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" = "+ str(ref_pressure_mbar)+" mBar")
        textobject.setTextOrigin(320, 400)
        textobject.textOut("T")
        apply_scripting(textobject, "0", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" = "+str(ref_temp_celsius))
        apply_scripting(textobject, "o", 4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut("C")
        print("2 half half ok")
        textobject.setTextOrigin(380, 400)
        textobject.textOut("Relative Humidity ")
        textobject.setTextOrigin(40, 380)
        textobject.textOut("Polarizing potential V")
        apply_scripting(textobject, "1", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" : "+ str(polarizing_potential_v) + " V")
        textobject.setTextOrigin(320, 380)
        textobject.textOut("Calibration polarity:  "+ calibration_polarity_ans)
        textobject.setTextOrigin(40, 360)
        textobject.textOut("User polarity: "+self.comboBox.currentText())
        textobject.setTextOrigin(40, 340)
        textobject.textOut("Calibration laboratory "+calibration_lab)
        textobject.setTextOrigin(340, 340)
        textobject.textOut("Date: "+str(calibration_date))
        textobject.setTextOrigin(40, 320)
        textobject.textOut("Electrometer model: "+ self.comboBox_electrometer.currentText())
        textobject.setTextOrigin(340, 320)
        textobject.textOut("Serial no: "+str(electrometer_serial_no) )
        textobject.setTextOrigin(40, 300)
        textobject.textOut("Calibrated separately from chamber: "+ electrometer_calib_sep )
        textobject.setTextOrigin(340, 300)
        textobject.textOut("Range setting: "+elec_range_setting)
        textobject.setTextOrigin(40, 280)
        textobject.textOut("If yes")
        textobject.setTextOrigin(80, 280)
        textobject.textOut("Calibration laboratory: "+electrometer_calib_place)
        textobject.setTextOrigin(340, 280)
        textobject.textOut("Date: "+str(electrometer_calib_date))
        textobject.setTextOrigin(40, 250)
        textobject.setFont("Helvetica-Bold", 13)
        textobject.setFillColorRGB(1, 0, 1)
        print("2 ok")
        textobject.textOut("3. Dosimeter reading and correction for influence quantities")
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.setFillColorRGB(0.1, 0.1, 0.1)
        textobject.setTextOrigin(40, 220)
        textobject.textOut("Uncorrected dosimeter reading at V")
        apply_scripting(textobject, "1", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut("  and user polarity: " +self.lineEdit_m1.text() + " nC" )
        textobject.setTextOrigin(40, 200)
        textobject.textOut("Corresponding accelerator monitor units: "+self.lineEdit_mu.text()+ " MU")
        textobject.setTextOrigin(40, 180)
        textobject.textOut("Ratio of dosimeter reading and monitor units: ")
        textobject.setTextOrigin(320, 180)
        textobject.textOut("M")
        apply_scripting(textobject, "1", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" : "+str(round(mu,4))+" nC MU")
        apply_scripting(textobject, "-1", 4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.setTextOrigin(40, 160)
        textobject.textOut("(i) Pressure P: "+self.lineEdit_pressure.text()+" mBar")
        textobject.setTextOrigin(200, 160)
        textobject.textOut("Temperature T: "+self.lineEdit_temp.text()+" ")
        apply_scripting(textobject,"o",4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut("C")
        textobject.setTextOrigin(320, 160)
        textobject.textOut(" Rel. humidity (if known): ")
        canvas_obj.drawImage("ktp.png", 250, 100, 100, 40)
        textobject.setTextOrigin(360, 113)
        textobject.textOut(" = "+ str(round(ktp,4)))
        textobject.setTextOrigin(40, 80)
        textobject.textOut("(ii) Electrometer calibration factor K")
        apply_scripting(textobject, "elec", -4)
        textobject.setFont("Helvetica-Oblique", 10)
        textobject.textOut(" : "+self.lineEdit_elec_calib.text())


        canvas_obj.drawText(textobject)
        canvas_obj.showPage()
        textobject_1 = canvas_obj.beginText()
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.setTextOrigin(40, 780)
        textobject_1.textOut("(iii) Polarity correction ")
        textobject_1.setTextOrigin(250, 780)
        textobject_1.textOut("+V")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(":")
        textobject_1.textOut("M")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+self.lineEdit_m1.text())
        textobject_1.setTextOrigin(380, 780)
        textobject_1.textOut(" -V")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(":M")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+self.lineEdit_mminus.text())
        canvas_obj.drawImage("kpol.png", 250, 720, 100, 40)
        textobject_1.setTextOrigin(360, 738)
        textobject_1.textOut(" = "+str(round(kpol,4)))
        textobject_1.setTextOrigin(40, 700)
        textobject_1.textOut("(iv) Recombination correction (two-voltage method) ")
        textobject_1.setTextOrigin(50, 680)
        textobject_1.textOut("Polarizing voltages: ")
        textobject_1.setTextOrigin(250, 680)
        textobject_1.textOut("V")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" (normal): "+self.lineEdit_v1.text()+ " V")
        textobject_1.setTextOrigin(380, 680)
        textobject_1.textOut("V")
        apply_scripting(textobject_1, "2", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" (reduced): "+self.lineEdit_v2.text()+ " V")
        textobject_1.setTextOrigin(50, 660)
        textobject_1.textOut("Readings at each V:")
        textobject_1.setTextOrigin(250, 660)
        textobject_1.textOut("M")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+self.lineEdit_m1.text())
        textobject_1.setTextOrigin(380, 660)
        textobject_1.textOut("M")
        apply_scripting(textobject_1, "2", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+self.lineEdit_m2.text())
        textobject_1.setTextOrigin(50, 640)
        textobject_1.textOut("Voltage ratio V")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" / V")
        apply_scripting(textobject_1, "2", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+str(voltage_ratio))
        textobject_1.setTextOrigin(280, 640)
        textobject_1.textOut("Ratio of readings M")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" / M")
        apply_scripting(textobject_1, "2", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+str(round(float(self.lineEdit_m1.text())/float(self.lineEdit_m2.text()),4)))
        textobject_1.setTextOrigin(50, 620)
        textobject_1.textOut("Type of beam: "+self.comboBox_2.currentText())
        textobject_1.setTextOrigin(50, 600)
        textobject_1.textOut("a")
        apply_scripting(textobject_1, "0", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+str(a0))
        textobject_1.setTextOrigin(220, 600)
        textobject_1.textOut("a")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+str(a1))
        textobject_1.setTextOrigin(350, 600)
        textobject_1.textOut("a")
        apply_scripting(textobject_1, " 2", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+str(a2))
        canvas_obj.drawImage("ks.png", 250, 545, 120, 40)
        textobject_1.setTextOrigin(370, 560)
        textobject_1.textOut(" = "+str(round(ks,4)))
        textobject_1.setTextOrigin(50, 525)
        textobject_1.textOut("Corrected dosimeter reading at the voltage V")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" : ")
        textobject_1.setTextOrigin(240, 500)
        textobject_1.textOut("M")
        apply_scripting(textobject_1, "Q", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = ")
        textobject_1.textOut("M")
        apply_scripting(textobject_1, "1", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" K ")
        apply_scripting(textobject_1, "TP", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" K ")
        apply_scripting(textobject_1, "elec", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" K ")
        apply_scripting(textobject_1, "pol", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" K ")
        apply_scripting(textobject_1, "S", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+ str(round(corrected_meter_reading,4))+" nC MU")
        apply_scripting(textobject_1, "-1", 4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.setTextOrigin(40, 480)
        textobject_1.setFont("Helvetica-Bold", 13)
        textobject_1.setFillColorRGB(1, 0, 1)
        print("3 ok")
        textobject_1.textOut("4. Absorbed dose to water at the reference depth, z")
        apply_scripting(textobject_1, "ref", -4)
        textobject_1.setFillColorRGB(0.1, 0.1, 0.1)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.setTextOrigin(50, 455)
        textobject_1.textOut("Beam quality correction factor taken from table 6.III for user quality Q: k")
        apply_scripting(textobject_1, "Q,Qo", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = " + str(round(kq,4)))
        textobject_1.setTextOrigin(230, 425)
        textobject_1.textOut("D")
        apply_scripting(textobject_1, "w,Q", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" (Z")
        apply_scripting(textobject_1, "ref", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" ) =  ")
        textobject_1.textOut("M")
        apply_scripting(textobject_1, "Q", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" N")
        apply_scripting(textobject_1, "D,w,Q", -4)
        apply_scripting(textobject_1, '0', -7)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" k")
        apply_scripting(textobject_1, "Q,Qo", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = " + str(round(abs_ref_depth,4))+ " Gy MU")
        apply_scripting(textobject_1, "-1", 4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.setTextOrigin(40, 390)
        textobject_1.setFont("Helvetica-Bold", 13)
        textobject_1.setFillColorRGB(1, 0, 1)
        textobject_1.textOut("5. Absorbed dose to water at the depth of dose maximum, z")
        apply_scripting(textobject_1, "max", -4)
        textobject_1.setFillColorRGB(0.1, 0.1, 0.1)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.setTextOrigin(60, 370)
        textobject_1.textOut("Depth of dose maximum:   Z")
        apply_scripting(textobject_1, "max", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" = "+ str(depth_of_dmax)+" cm")
        textobject_1.setTextOrigin(40, 350)
        textobject_1.textOut("(i) SSD set-up ")
        textobject_1.setTextOrigin(60, 330)
        textobject_1.textOut("Percentage depth-dose at z")
        apply_scripting(textobject_1, "ref", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" for a 10 cm x 10 cm field size =  "+ str(round(dmax_result,4))+" % ")
        textobject_1.setTextOrigin(60, 310)
        textobject_1.textOut("Absorbed-dose calibration of monitor at z")
        apply_scripting(textobject_1, "max", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" : ")
        textobject_1.setTextOrigin(190, 270)
        textobject_1.textOut("D")
        apply_scripting(textobject_1, "w,Q", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" (Z")
        apply_scripting(textobject_1, "max", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" ) = 100 D")
        apply_scripting(textobject_1, "w,Q", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" (z")
        apply_scripting(textobject_1, "ref", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" ) / PDD(Z")
        apply_scripting(textobject_1, "ref", -4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.textOut(" ) = "+ str(round(abs_dmax,4))+" Gy MU")
        apply_scripting(textobject_1, "-1", 4)
        textobject_1.setFont("Helvetica-Oblique", 10)
        textobject_1.setTextOrigin(60,230)
        textobject_1.textOut("variation of output from baseline value: "+ str(round(variation_of_output,4))+" % " )
        textobject_1.setTextOrigin(40, 100)
        textobject_1.textOut("Signature of physicist who performed QA")
        textobject_1.setTextOrigin(400, 100)
        textobject_1.textOut("Signature of reviewing physicist")

        canvas_obj.drawText(textobject_1)
        canvas_obj.save()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())