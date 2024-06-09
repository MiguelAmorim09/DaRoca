# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmListar.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QToolBar, QWidget)
import imgs_rc

class Ui_FrmLista(object):
    def setupUi(self, FrmLista):
        if not FrmLista.objectName():
            FrmLista.setObjectName(u"FrmLista")
        FrmLista.resize(800, 549)
        FrmLista.setStyleSheet(u"background: #013C31;\n"
"")
        self.action_Voltar = QAction(FrmLista)
        self.action_Voltar.setObjectName(u"action_Voltar")
        icon = QIcon()
        icon.addFile(u":/prod/imgsDaRocaBD/voltar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Voltar.setIcon(icon)
        self.centralwidget = QWidget(FrmLista)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridProd = QTableWidget(self.centralwidget)
        if (self.gridProd.columnCount() < 6):
            self.gridProd.setColumnCount(6)
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.gridProd.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.gridProd.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.gridProd.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.gridProd.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.gridProd.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.gridProd.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.gridProd.setObjectName(u"gridProd")
        self.gridProd.setGeometry(QRect(90, 60, 602, 311))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.gridProd.setFont(font1)
        self.gridProd.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        FrmLista.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FrmLista)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        FrmLista.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FrmLista)
        self.statusbar.setObjectName(u"statusbar")
        FrmLista.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FrmLista)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setFont(font1)
        self.toolBar.setStyleSheet(u"background: #FE7411;\n"
"color: #fff;")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        FrmLista.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_Voltar)

        self.retranslateUi(FrmLista)

        QMetaObject.connectSlotsByName(FrmLista)
    # setupUi

    def retranslateUi(self, FrmLista):
        FrmLista.setWindowTitle(QCoreApplication.translate("FrmLista", u"Lista de produtos", None))
        self.action_Voltar.setText(QCoreApplication.translate("FrmLista", u"&Voltar", None))
#if QT_CONFIG(tooltip)
        self.action_Voltar.setToolTip(QCoreApplication.translate("FrmLista", u"Retorna para a tela inicial", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.gridProd.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FrmLista", u"ID", None));
        ___qtablewidgetitem1 = self.gridProd.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FrmLista", u"Nome", None));
        ___qtablewidgetitem2 = self.gridProd.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FrmLista", u"Imagem", None));
        ___qtablewidgetitem3 = self.gridProd.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FrmLista", u"Valor", None));
        ___qtablewidgetitem4 = self.gridProd.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FrmLista", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.gridProd.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FrmLista", u"Categoria", None));
        self.toolBar.setWindowTitle(QCoreApplication.translate("FrmLista", u"toolBar", None))
    # retranslateUi

