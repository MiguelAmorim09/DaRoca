# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmProds.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QWidget)
import imgs_rc

class Ui_FrmProds(object):
    def setupUi(self, FrmProds):
        if not FrmProds.objectName():
            FrmProds.setObjectName(u"FrmProds")
        FrmProds.resize(800, 549)
        FrmProds.setStyleSheet(u"background-color: #013C31;\n"
"")
        FrmProds.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.action_Adicionar = QAction(FrmProds)
        self.action_Adicionar.setObjectName(u"action_Adicionar")
        icon = QIcon()
        icon.addFile(u":/prod/imgsDaRocaBD/adicionar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Adicionar.setIcon(icon)
        self.action_Editar = QAction(FrmProds)
        self.action_Editar.setObjectName(u"action_Editar")
        icon1 = QIcon()
        icon1.addFile(u":/prod/imgsDaRocaBD/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Editar.setIcon(icon1)
        self.action_Lista = QAction(FrmProds)
        self.action_Lista.setObjectName(u"action_Lista")
        icon2 = QIcon()
        icon2.addFile(u":/prod/imgsDaRocaBD/listar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Lista.setIcon(icon2)
        self.action_Remover = QAction(FrmProds)
        self.action_Remover.setObjectName(u"action_Remover")
        icon3 = QIcon()
        icon3.addFile(u":/prod/imgsDaRocaBD/remover.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Remover.setIcon(icon3)
        self.action_Sair = QAction(FrmProds)
        self.action_Sair.setObjectName(u"action_Sair")
        icon4 = QIcon()
        icon4.addFile(u":/prod/imgsDaRocaBD/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Sair.setIcon(icon4)
        self.centralwidget = QWidget(FrmProds)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 60, 461, 301))
        self.frame.setStyleSheet(u"background: #FE7411;\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 0, 391, 71))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 60, 71, 16))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #fff")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 120, 211, 21))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #fff")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 140, 181, 16))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: #fff")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 160, 141, 16))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: #fff")
        FrmProds.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FrmProds)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        FrmProds.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FrmProds)
        self.statusbar.setObjectName(u"statusbar")
        FrmProds.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FrmProds)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setFont(font1)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet(u"background: #FE7411;\n"
"color: #fff;")
        FrmProds.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_Adicionar)
        self.toolBar.addAction(self.action_Editar)
        self.toolBar.addAction(self.action_Remover)
        self.toolBar.addAction(self.action_Lista)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Sair)

        self.retranslateUi(FrmProds)

        QMetaObject.connectSlotsByName(FrmProds)
    # setupUi

    def retranslateUi(self, FrmProds):
        FrmProds.setWindowTitle(QCoreApplication.translate("FrmProds", u"Sistema de manuten\u00e7\u00e3o de banco de dados", None))
        self.action_Adicionar.setText(QCoreApplication.translate("FrmProds", u"&Adicionar", None))
#if QT_CONFIG(tooltip)
        self.action_Adicionar.setToolTip(QCoreApplication.translate("FrmProds", u"Incluir novo produto", None))
#endif // QT_CONFIG(tooltip)
        self.action_Editar.setText(QCoreApplication.translate("FrmProds", u"&Editar", None))
#if QT_CONFIG(tooltip)
        self.action_Editar.setToolTip(QCoreApplication.translate("FrmProds", u"Alterar os dados de um produto existente", None))
#endif // QT_CONFIG(tooltip)
        self.action_Lista.setText(QCoreApplication.translate("FrmProds", u"&Lista", None))
#if QT_CONFIG(tooltip)
        self.action_Lista.setToolTip(QCoreApplication.translate("FrmProds", u"Apresenta uma lista com todos os produtos", None))
#endif // QT_CONFIG(tooltip)
        self.action_Remover.setText(QCoreApplication.translate("FrmProds", u"&Remover", None))
#if QT_CONFIG(tooltip)
        self.action_Remover.setToolTip(QCoreApplication.translate("FrmProds", u"Excluir um produto existente", None))
#endif // QT_CONFIG(tooltip)
        self.action_Sair.setText(QCoreApplication.translate("FrmProds", u"&Sair", None))
#if QT_CONFIG(tooltip)
        self.action_Sair.setToolTip(QCoreApplication.translate("FrmProds", u"Fecha a conex\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("FrmProds", u"Sistema de manuten\u00e7\u00e3o de banco de dados", None))
        self.label_2.setText(QCoreApplication.translate("FrmProds", u"DaRo\u00e7a", None))
        self.label_3.setText(QCoreApplication.translate("FrmProds", u"Adicione, edite, remova e veja", None))
        self.label_4.setText(QCoreApplication.translate("FrmProds", u"os produtos DaRo\u00e7a com", None))
        self.label_5.setText(QCoreApplication.translate("FrmProds", u"facilidade e rapidez", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FrmProds", u"toolBar", None))
    # retranslateUi

