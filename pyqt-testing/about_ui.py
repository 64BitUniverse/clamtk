# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(591, 419)
        self.AboutLayout = QGridLayout(About)
        self.AboutLayout.setObjectName(u"AboutLayout")
        self.AboutLayout.setContentsMargins(-1, 9, -1, -1)
        self.DescRight = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.AboutLayout.addItem(self.DescRight, 3, 2, 1, 1)

        self.RepoLinks = QLabel(About)
        self.RepoLinks.setObjectName(u"RepoLinks")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RepoLinks.sizePolicy().hasHeightForWidth())
        self.RepoLinks.setSizePolicy(sizePolicy)
        self.RepoLinks.setTextFormat(Qt.TextFormat.MarkdownText)
        self.RepoLinks.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.RepoLinks.setOpenExternalLinks(True)

        self.AboutLayout.addWidget(self.RepoLinks, 4, 1, 1, 1)

        self.DescLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.AboutLayout.addItem(self.DescLeft, 3, 0, 1, 1)

        self.ClamLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.AboutLayout.addItem(self.ClamLeft, 1, 0, 1, 1)

        self.ClamRight = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.AboutLayout.addItem(self.ClamRight, 1, 2, 1, 1)

        self.Clam = QLabel(About)
        self.Clam.setObjectName(u"Clam")
        sizePolicy.setHeightForWidth(self.Clam.sizePolicy().hasHeightForWidth())
        self.Clam.setSizePolicy(sizePolicy)
        self.Clam.setPixmap(QPixmap(u"../images/clamtk.png"))
        self.Clam.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.AboutLayout.addWidget(self.Clam, 1, 1, 1, 1)

        self.Description = QLabel(About)
        self.Description.setObjectName(u"Description")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Description.sizePolicy().hasHeightForWidth())
        self.Description.setSizePolicy(sizePolicy1)
        self.Description.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.AboutLayout.addWidget(self.Description, 3, 1, 1, 1)

        self.Version = QLabel(About)
        self.Version.setObjectName(u"Version")
        sizePolicy.setHeightForWidth(self.Version.sizePolicy().hasHeightForWidth())
        self.Version.setSizePolicy(sizePolicy)
        self.Version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.AboutLayout.addWidget(self.Version, 2, 1, 1, 1)

        self.License = QPushButton(About)
        self.License.setObjectName(u"License")
        sizePolicy1.setHeightForWidth(self.License.sizePolicy().hasHeightForWidth())
        self.License.setSizePolicy(sizePolicy1)

        self.AboutLayout.addWidget(self.License, 5, 1, 1, 1)

        self.Credits = QPushButton(About)
        self.Credits.setObjectName(u"Credits")

        self.AboutLayout.addWidget(self.Credits, 5, 0, 1, 1)

        self.Close = QPushButton(About)
        self.Close.setObjectName(u"Close")
        sizePolicy1.setHeightForWidth(self.Close.sizePolicy().hasHeightForWidth())
        self.Close.setSizePolicy(sizePolicy1)

        self.AboutLayout.addWidget(self.Close, 5, 2, 1, 1)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"Form", None))
        self.RepoLinks.setText(QCoreApplication.translate("About", u"[GitLab](https://gitlab.com/dave_m/clamtk/-/wikis/Home 'GitLab Repo') | [GitHub](https://github.com/dave-theunsub/clamtk 'GitHub Repo')", None))
        self.Clam.setText("")
        self.Description.setText(QCoreApplication.translate("About", u"ClamTk is a graphical front-end for Clam Antivirus", None))
        self.Version.setText(QCoreApplication.translate("About", u"6.07", None))
        self.License.setText(QCoreApplication.translate("About", u"License", None))
        self.Credits.setText(QCoreApplication.translate("About", u"Credits", None))
        self.Close.setText(QCoreApplication.translate("About", u"Close", None))
    # retranslateUi

