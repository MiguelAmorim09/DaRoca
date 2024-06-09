# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmRemover.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QSpinBox, QStatusBar,
    QToolBar, QWidget)
import imgs_rc

class Ui_FrmRemover(object):
    def setupUi(self, FrmRemover):
        if not FrmRemover.objectName():
            FrmRemover.setObjectName(u"FrmRemover")
        FrmRemover.resize(800, 549)
        FrmRemover.setStyleSheet(u"background: #013C31;\n"
"")
        FrmRemover.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.action_Voltar = QAction(FrmRemover)
        self.action_Voltar.setObjectName(u"action_Voltar")
        icon = QIcon()
        icon.addFile(u":/prod/imgsDaRocaBD/voltar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Voltar.setIcon(icon)
        self.action_Salvar = QAction(FrmRemover)
        self.action_Salvar.setObjectName(u"action_Salvar")
        icon1 = QIcon()
        icon1.addFile(u":/prod/imgsDaRocaBD/salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Salvar.setIcon(icon1)
        self.centralwidget = QWidget(FrmRemover)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(230, 90, 313, 182))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.spbID = QSpinBox(self.layoutWidget)
        self.spbID.setObjectName(u"spbID")
        self.spbID.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.spbID.setMinimum(1)

        self.gridLayout.addWidget(self.spbID, 0, 1, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        FrmRemover.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FrmRemover)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        FrmRemover.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FrmRemover)
        self.statusbar.setObjectName(u"statusbar")
        FrmRemover.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FrmRemover)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"background: #FE7411;\n"
"color: #fff;")
        FrmRemover.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_Voltar)
        self.toolBar.addAction(self.action_Salvar)

        self.retranslateUi(FrmRemover)

        QMetaObject.connectSlotsByName(FrmRemover)
    # setupUi

    def retranslateUi(self, FrmRemover):
        FrmRemover.setWindowTitle(QCoreApplication.translate("FrmRemover", u"Remover produto", None))
        self.action_Voltar.setText(QCoreApplication.translate("FrmRemover", u"&Voltar", None))
#if QT_CONFIG(tooltip)
        self.action_Voltar.setToolTip(QCoreApplication.translate("FrmRemover", u"Retorna para a tela inicial", None))
#endif // QT_CONFIG(tooltip)
        self.action_Salvar.setText(QCoreApplication.translate("FrmRemover", u"&Salvar", None))
#if QT_CONFIG(tooltip)
        self.action_Salvar.setToolTip(QCoreApplication.translate("FrmRemover", u"Remove o produto", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("FrmRemover", u"ID do produto:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FrmRemover", u"toolBar", None))
    # retranslateUi

