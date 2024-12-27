# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmenu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QSpacerItem, QStatusBar, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 30, 551, 481))
        self.MainMenu = QGridLayout(self.gridLayoutWidget)
        self.MainMenu.setObjectName(u"MainMenu")
        self.MainMenu.setContentsMargins(0, 0, 0, 0)
        self.Configuration = QLabel(self.gridLayoutWidget)
        self.Configuration.setObjectName(u"Configuration")

        self.MainMenu.addWidget(self.Configuration, 0, 0, 1, 1)

        self.Network = QToolButton(self.gridLayoutWidget)
        self.Network.setObjectName(u"Network")
        icon = QIcon()
        iconThemeName = u"preferences-system-network"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.Network.setIcon(icon)
        self.Network.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.Network, 1, 2, 1, 1)

        self.Settings = QToolButton(self.gridLayoutWidget)
        self.Settings.setObjectName(u"Settings")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        icon1 = QIcon(QIcon.fromTheme(u"preferences-system"))
        self.Settings.setIcon(icon1)
        self.Settings.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.Settings, 1, 0, 1, 1)

        self.History = QToolButton(self.gridLayoutWidget)
        self.History.setObjectName(u"History")
        sizePolicy.setHeightForWidth(self.History.sizePolicy().hasHeightForWidth())
        self.History.setSizePolicy(sizePolicy)
        icon2 = QIcon(QIcon.fromTheme(u"document-open-recent"))
        self.History.setIcon(icon2)
        self.History.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.History, 3, 0, 1, 1)

        self.Whitelist = QToolButton(self.gridLayoutWidget)
        self.Whitelist.setObjectName(u"Whitelist")
        sizePolicy.setHeightForWidth(self.Whitelist.sizePolicy().hasHeightForWidth())
        self.Whitelist.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        iconThemeName = u"security-high"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.Whitelist.setIcon(icon3)
        self.Whitelist.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.Whitelist, 1, 1, 1, 1)

        self.Scheduler = QToolButton(self.gridLayoutWidget)
        self.Scheduler.setObjectName(u"Scheduler")
        icon4 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.Scheduler.setIcon(icon4)
        self.Scheduler.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.Scheduler, 1, 3, 1, 1)

        self.History_2 = QLabel(self.gridLayoutWidget)
        self.History_2.setObjectName(u"History_2")

        self.MainMenu.addWidget(self.History_2, 2, 0, 1, 1)

        self.Quarantine = QToolButton(self.gridLayoutWidget)
        self.Quarantine.setObjectName(u"Quarantine")
        sizePolicy.setHeightForWidth(self.Quarantine.sizePolicy().hasHeightForWidth())
        self.Quarantine.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        iconThemeName = u"user-trash-full"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.Quarantine.setIcon(icon5)
        self.Quarantine.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.Quarantine, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.MainMenu.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.MainMenu.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.MainMenu.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.MainMenu.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.MainMenu.addWidget(self.label, 6, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.MainMenu.addWidget(self.label_2, 4, 0, 1, 1)

        self.ScanaFile = QToolButton(self.gridLayoutWidget)
        self.ScanaFile.setObjectName(u"ScanaFile")
        icon6 = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.ScanaFile.setIcon(icon6)
        self.ScanaFile.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.ScanaFile, 5, 0, 1, 1)

        self.Update = QToolButton(self.gridLayoutWidget)
        self.Update.setObjectName(u"Update")
        sizePolicy.setHeightForWidth(self.Update.sizePolicy().hasHeightForWidth())
        self.Update.setSizePolicy(sizePolicy)
        icon7 = QIcon()
        iconThemeName = u"software-update-available"
        if QIcon.hasThemeIcon(iconThemeName):
            icon7 = QIcon.fromTheme(iconThemeName)
        else:
            icon7.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.Update.setIcon(icon7)
        self.Update.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.Update, 7, 0, 1, 1)

        self.UpdateAssistant = QToolButton(self.gridLayoutWidget)
        self.UpdateAssistant.setObjectName(u"UpdateAssistant")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.UpdateAssistant.sizePolicy().hasHeightForWidth())
        self.UpdateAssistant.setSizePolicy(sizePolicy1)
        icon8 = QIcon()
        iconThemeName = u"system-help"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.UpdateAssistant.setIcon(icon8)
        self.UpdateAssistant.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.UpdateAssistant, 7, 1, 1, 1)

        self.ScanaDirectory = QToolButton(self.gridLayoutWidget)
        self.ScanaDirectory.setObjectName(u"ScanaDirectory")
        icon9 = QIcon()
        iconThemeName = u"folder-documents"
        if QIcon.hasThemeIcon(iconThemeName):
            icon9 = QIcon.fromTheme(iconThemeName)
        else:
            icon9.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.ScanaDirectory.setIcon(icon9)
        self.ScanaDirectory.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.ScanaDirectory, 5, 1, 1, 1)

        self.About = QToolButton(self.gridLayoutWidget)
        self.About.setObjectName(u"About")
        sizePolicy.setHeightForWidth(self.About.sizePolicy().hasHeightForWidth())
        self.About.setSizePolicy(sizePolicy)
        icon10 = QIcon()
        iconThemeName = u"help-about"
        if QIcon.hasThemeIcon(iconThemeName):
            icon10 = QIcon.fromTheme(iconThemeName)
        else:
            icon10.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.About.setIcon(icon10)
        self.About.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.About, 7, 2, 1, 1)

        self.Analysis = QToolButton(self.gridLayoutWidget)
        self.Analysis.setObjectName(u"Analysis")
        icon11 = QIcon()
        iconThemeName = u"system-search"
        if QIcon.hasThemeIcon(iconThemeName):
            icon11 = QIcon.fromTheme(iconThemeName)
        else:
            icon11.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.Analysis.setIcon(icon11)
        self.Analysis.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.MainMenu.addWidget(self.Analysis, 5, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Configuration.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.Network.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.History.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.Whitelist.setText(QCoreApplication.translate("MainWindow", u"Whitelist", None))
        self.Scheduler.setText(QCoreApplication.translate("MainWindow", u"Scheduler", None))
        self.History_2.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.Quarantine.setText(QCoreApplication.translate("MainWindow", u"Quarantine", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Updates", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.ScanaFile.setText(QCoreApplication.translate("MainWindow", u"Scan a File", None))
        self.Update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.UpdateAssistant.setText(QCoreApplication.translate("MainWindow", u"Update Assistant", None))
        self.ScanaDirectory.setText(QCoreApplication.translate("MainWindow", u"Scan a Directory", None))
        self.About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.Analysis.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
    # retranslateUi

