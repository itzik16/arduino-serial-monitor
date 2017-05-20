# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
            }

            QLCDNumber {
                background-color: #000000;
                color: #FFFFFF;
            }

            QTextEdit {
                background-color: #000000;
                color: #00FF00;
                font-family: monospace;
                font-size: 10px;
            }
        """)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.MainPannel = QtWidgets.QWidget(MainWindow)
        self.MainPannel.setMinimumSize(QtCore.QSize(800, 0))
        self.MainPannel.setObjectName("MainPannel")
        self.SettingsPanel = QtWidgets.QGroupBox(self.MainPannel)
        self.SettingsPanel.setGeometry(QtCore.QRect(10, 10, 280, 270))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.SettingsPanel.setFont(font)
        self.SettingsPanel.setMouseTracking(False)
        self.SettingsPanel.setFlat(True)
        self.SettingsPanel.setCheckable(False)
        self.SettingsPanel.setObjectName("SettingsPanel")
        self.LBLBaudRate = QtWidgets.QLabel(self.SettingsPanel)
        self.LBLBaudRate.setGeometry(QtCore.QRect(10, 110, 80, 30))
        self.LBLBaudRate.setObjectName("LBLBaudRate")
        self.LBLSerialPort = QtWidgets.QLabel(self.SettingsPanel)
        self.LBLSerialPort.setGeometry(QtCore.QRect(10, 70, 80, 30))
        self.LBLSerialPort.setObjectName("LBLSerialPort")
        self.SELSerialPort = QtWidgets.QComboBox(self.SettingsPanel)
        self.SELSerialPort.setEnabled(False)
        self.SELSerialPort.setGeometry(QtCore.QRect(100, 70, 170, 30))
        self.SELSerialPort.setObjectName("SELSerialPort")
        self.SELSerialPort.addItem("")
        self.BTNOpenPort = QtWidgets.QPushButton(self.SettingsPanel)
        self.BTNOpenPort.setEnabled(False)
        self.BTNOpenPort.setGeometry(QtCore.QRect(100, 150, 80, 30))
        self.BTNOpenPort.setAutoDefault(False)
        self.BTNOpenPort.setFlat(False)
        self.BTNOpenPort.setObjectName("BTNOpenPort")
        self.BTNClosePort = QtWidgets.QPushButton(self.SettingsPanel)
        self.BTNClosePort.setEnabled(False)
        self.BTNClosePort.setGeometry(QtCore.QRect(190, 150, 80, 30))
        self.BTNClosePort.setDefault(False)
        self.BTNClosePort.setFlat(False)
        self.BTNClosePort.setObjectName("BTNClosePort")
        self.SELBaudRate = QtWidgets.QComboBox(self.SettingsPanel)
        self.SELBaudRate.setEnabled(False)
        self.SELBaudRate.setGeometry(QtCore.QRect(100, 110, 170, 30))
        self.SELBaudRate.setObjectName("SELBaudRate")
        self.SELBaudRate.addItem("")
        self.SELBaudRate.addItem("")
        self.SELBaudRate.addItem("")
        self.SELBaudRate.addItem("")
        self.SELBaudRate.addItem("")
        self.SELBaudRate.addItem("")
        self.SELBaudRate.addItem("")
        self.SELBaudRate.addItem("")
        self.SELBaudRate.addItem("")
        self.LBLSensorType = QtWidgets.QLabel(self.SettingsPanel)
        self.LBLSensorType.setGeometry(QtCore.QRect(10, 30, 80, 30))
        self.LBLSensorType.setObjectName("LBLSensorType")
        self.SELSensor = QtWidgets.QComboBox(self.SettingsPanel)
        self.SELSensor.setGeometry(QtCore.QRect(100, 30, 170, 30))
        self.SELSensor.setObjectName("SELSensor")
        self.SELSensor.addItem("")
        self.LBLDelay = QtWidgets.QLabel(self.SettingsPanel)
        self.LBLDelay.setGeometry(QtCore.QRect(10, 190, 80, 30))
        self.LBLDelay.setObjectName("LBLDelay")
        self.INDelay = QtWidgets.QLineEdit(self.SettingsPanel)
        self.INDelay.setEnabled(False)
        self.INDelay.setGeometry(QtCore.QRect(100, 190, 170, 30))
        self.INDelay.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.INDelay.setText("1000")
        self.INDelay.setMaxLength(7)
        self.INDelay.setCursorPosition(4)
        self.INDelay.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.INDelay.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.INDelay.setObjectName("INDelay")
        self.BTNSetDelay = QtWidgets.QPushButton(self.SettingsPanel)
        self.BTNSetDelay.setEnabled(False)
        self.BTNSetDelay.setGeometry(QtCore.QRect(100, 230, 170, 30))
        self.BTNSetDelay.setCheckable(False)
        self.BTNSetDelay.setFlat(False)
        self.BTNSetDelay.setObjectName("BTNSetDelay")
        # self.Separator = QtWidgets.QFrame(self.MainPannel)
        # self.Separator.setGeometry(QtCore.QRect(290, 0, 10, 600))
        # self.Separator.setFrameShape(QtWidgets.QFrame.VLine)
        # self.Separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.Separator.setObjectName("Separator")
        self.DisplayPanel = QtWidgets.QGroupBox(self.MainPannel)
        self.DisplayPanel.setGeometry(QtCore.QRect(300, 10, 490, 580))
        self.DisplayPanel.setObjectName("DisplayPanel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.DisplayPanel)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 471, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.PlotLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.PlotLayout.setContentsMargins(0, -1, -1, -1)
        self.PlotLayout.setSpacing(0)
        self.PlotLayout.setObjectName("PlotLayout")
        self.LDCTime = QtWidgets.QLCDNumber(self.DisplayPanel)
        self.LDCTime.setEnabled(False)
        self.LDCTime.setGeometry(QtCore.QRect(10, 30, 110, 30))
        self.LDCTime.setAutoFillBackground(False)
        self.LDCTime.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LDCTime.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LDCTime.setLineWidth(0)
        self.LDCTime.setSmallDecimalPoint(False)
        self.LDCTime.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LDCTime.setProperty("value", 0.0)
        self.LDCTime.setObjectName("LDCTime")
        self.LBLTime = QtWidgets.QLabel(self.DisplayPanel)
        self.LBLTime.setEnabled(False)
        self.LBLTime.setGeometry(QtCore.QRect(10, 70, 110, 30))
        self.LBLTime.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLTime.setObjectName("LBLTime")
        self.LCDMagnitude1 = QtWidgets.QLCDNumber(self.DisplayPanel)
        self.LCDMagnitude1.setEnabled(False)
        self.LCDMagnitude1.setGeometry(QtCore.QRect(130, 30, 110, 30))
        self.LCDMagnitude1.setAutoFillBackground(False)
        self.LCDMagnitude1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LCDMagnitude1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LCDMagnitude1.setLineWidth(0)
        self.LCDMagnitude1.setSmallDecimalPoint(False)
        self.LCDMagnitude1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LCDMagnitude1.setObjectName("LCDMagnitude1")
        self.LBLMagnitude1 = QtWidgets.QLabel(self.DisplayPanel)
        self.LBLMagnitude1.setEnabled(False)
        self.LBLMagnitude1.setGeometry(QtCore.QRect(130, 70, 110, 30))
        self.LBLMagnitude1.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLMagnitude1.setObjectName("LBLMagnitude1")
        self.LCDMagnitude2 = QtWidgets.QLCDNumber(self.DisplayPanel)
        self.LCDMagnitude2.setEnabled(False)
        self.LCDMagnitude2.setGeometry(QtCore.QRect(250, 30, 110, 30))
        self.LCDMagnitude2.setAutoFillBackground(False)
        self.LCDMagnitude2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LCDMagnitude2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LCDMagnitude2.setLineWidth(0)
        self.LCDMagnitude2.setSmallDecimalPoint(False)
        self.LCDMagnitude2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LCDMagnitude2.setObjectName("LCDMagnitude2")
        self.LBLMagnitude2 = QtWidgets.QLabel(self.DisplayPanel)
        self.LBLMagnitude2.setEnabled(False)
        self.LBLMagnitude2.setGeometry(QtCore.QRect(250, 70, 110, 30))
        self.LBLMagnitude2.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLMagnitude2.setObjectName("LBLMagnitude2")
        self.LCDMagnitude3 = QtWidgets.QLCDNumber(self.DisplayPanel)
        self.LCDMagnitude3.setEnabled(False)
        self.LCDMagnitude3.setGeometry(QtCore.QRect(370, 30, 110, 30))
        self.LCDMagnitude3.setAutoFillBackground(False)
        self.LCDMagnitude3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LCDMagnitude3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LCDMagnitude3.setLineWidth(0)
        self.LCDMagnitude3.setSmallDecimalPoint(False)
        self.LCDMagnitude3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.LCDMagnitude3.setObjectName("LCDMagnitude3")
        self.LBLMagnitude3 = QtWidgets.QLabel(self.DisplayPanel)
        self.LBLMagnitude3.setEnabled(False)
        self.LBLMagnitude3.setGeometry(QtCore.QRect(370, 70, 110, 30))
        self.LBLMagnitude3.setAlignment(QtCore.Qt.AlignCenter)
        self.LBLMagnitude3.setObjectName("LBLMagnitude3")
        self.SerialConsolePanel = QtWidgets.QGroupBox(self.MainPannel)
        self.SerialConsolePanel.setGeometry(QtCore.QRect(10, 290, 281, 301))
        self.SerialConsolePanel.setObjectName("SerialConsolePanel")
        self.SerialConsole = QtWidgets.QTextEdit(self.SerialConsolePanel)
        self.SerialConsole.setEnabled(False)
        self.SerialConsole.setGeometry(QtCore.QRect(10, 30, 260, 260))
        self.SerialConsole.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SerialConsole.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SerialConsole.setLineWidth(1)
        self.SerialConsole.setReadOnly(True)
        self.SerialConsole.setObjectName("SerialConsole")
        MainWindow.setCentralWidget(self.MainPannel)

        self.retranslateUi(MainWindow)
        self.SELBaudRate.setCurrentIndex(0)
        self.SELSensor.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.SELSensor, self.SELSerialPort)
        MainWindow.setTabOrder(self.SELSerialPort, self.SELBaudRate)
        MainWindow.setTabOrder(self.SELBaudRate, self.BTNOpenPort)
        MainWindow.setTabOrder(self.BTNOpenPort, self.BTNClosePort)
        MainWindow.setTabOrder(self.BTNClosePort, self.INDelay)
        MainWindow.setTabOrder(self.INDelay, self.BTNSetDelay)
        MainWindow.setTabOrder(self.BTNSetDelay, self.SerialConsole)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aruino Serial Monitor"))
        self.SettingsPanel.setTitle(_translate("MainWindow", "Settings"))
        self.LBLBaudRate.setText(_translate("MainWindow", "Baud Rate"))
        self.LBLSerialPort.setText(_translate("MainWindow", "Serial Port"))
        self.SELSerialPort.setItemText(0, _translate("MainWindow", "Select port"))
        self.BTNOpenPort.setText(_translate("MainWindow", "Open Port"))
        self.BTNClosePort.setText(_translate("MainWindow", "Close Port"))
        self.SELBaudRate.setItemText(0, _translate("MainWindow", "Select baud rate"))
        self.SELBaudRate.setItemText(1, _translate("MainWindow", "4800 baud"))
        self.SELBaudRate.setItemText(2, _translate("MainWindow", "9600 baud"))
        self.SELBaudRate.setItemText(3, _translate("MainWindow", "19200  baud"))
        self.SELBaudRate.setItemText(4, _translate("MainWindow", "38400  baud"))
        self.SELBaudRate.setItemText(5, _translate("MainWindow", "57600  baud"))
        self.SELBaudRate.setItemText(6, _translate("MainWindow", "115200  baud"))
        self.SELBaudRate.setItemText(7, _translate("MainWindow", "230400  baud"))
        self.SELBaudRate.setItemText(8, _translate("MainWindow", "250000  baud"))
        self.LBLSensorType.setText(_translate("MainWindow", "Sensor Type"))
        self.SELSensor.setItemText(0, _translate("MainWindow", "Select sensor"))
        self.LBLDelay.setText(_translate("MainWindow", "Delay [ms]"))
        self.BTNSetDelay.setText(_translate("MainWindow", "Set Delay"))
        self.DisplayPanel.setTitle(_translate("MainWindow", "Plot and display"))
        self.LBLTime.setText(_translate("MainWindow", "Time"))
        self.LBLMagnitude1.setText(_translate("MainWindow", "Magnitude 1"))
        self.LBLMagnitude2.setText(_translate("MainWindow", "Magnitude 2"))
        self.LBLMagnitude3.setText(_translate("MainWindow", "Magnitude 3"))
        self.SerialConsolePanel.setTitle(_translate("MainWindow", "Serial Monitor"))

