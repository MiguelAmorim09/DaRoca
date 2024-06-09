# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmEditar.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QSizePolicy, QSpinBox, QStatusBar, QToolBar,
    QWidget)
import imgs_rc

class Ui_FrmEditar(object):
    def setupUi(self, FrmEditar):
        if not FrmEditar.objectName():
            FrmEditar.setObjectName(u"FrmEditar")
        FrmEditar.resize(800, 550)
        FrmEditar.setStyleSheet(u"background-color: #013C31;")
        self.action_Voltar = QAction(FrmEditar)
        self.action_Voltar.setObjectName(u"action_Voltar")
        icon = QIcon()
        icon.addFile(u":/prod/imgsDaRocaBD/voltar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Voltar.setIcon(icon)
        self.action_Salvar = QAction(FrmEditar)
        self.action_Salvar.setObjectName(u"action_Salvar")
        icon1 = QIcon()
        icon1.addFile(u":/prod/imgsDaRocaBD/salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Salvar.setIcon(icon1)
        self.centralwidget = QWidget(FrmEditar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(220, 100, 333, 167))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spbID = QSpinBox(self.layoutWidget)
        self.spbID.setObjectName(u"spbID")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.spbID.setFont(font1)
        self.spbID.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.spbID.setMinimum(1)

        self.gridLayout.addWidget(self.spbID, 0, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.edNome = QLineEdit(self.layoutWidget)
        self.edNome.setObjectName(u"edNome")
        self.edNome.setFont(font1)
        self.edNome.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")

        self.gridLayout.addWidget(self.edNome, 1, 1, 1, 2)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)

        self.edImagem = QLineEdit(self.layoutWidget)
        self.edImagem.setObjectName(u"edImagem")
        self.edImagem.setFont(font1)
        self.edImagem.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")

        self.gridLayout.addWidget(self.edImagem, 2, 2, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.dspbValor = QDoubleSpinBox(self.layoutWidget)
        self.dspbValor.setObjectName(u"dspbValor")
        self.dspbValor.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.dspbValor.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.dspbValor, 3, 2, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 2)

        self.edDescricao = QLineEdit(self.layoutWidget)
        self.edDescricao.setObjectName(u"edDescricao")
        self.edDescricao.setFont(font1)
        self.edDescricao.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")

        self.gridLayout.addWidget(self.edDescricao, 4, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.spbCategoria = QSpinBox(self.layoutWidget)
        self.spbCategoria.setObjectName(u"spbCategoria")
        self.spbCategoria.setFont(font1)
        self.spbCategoria.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.spbCategoria.setMinimum(1)
        self.spbCategoria.setMaximum(3)

        self.gridLayout.addWidget(self.spbCategoria, 5, 2, 1, 1)

        FrmEditar.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FrmEditar)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        FrmEditar.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FrmEditar)
        self.statusbar.setObjectName(u"statusbar")
        FrmEditar.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FrmEditar)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"background-color: #FE7411;\n"
"color: #fff;")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        FrmEditar.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_Voltar)
        self.toolBar.addAction(self.action_Salvar)

        self.retranslateUi(FrmEditar)

        QMetaObject.connectSlotsByName(FrmEditar)
    # setupUi

    def retranslateUi(self, FrmEditar):
        FrmEditar.setWindowTitle(QCoreApplication.translate("FrmEditar", u"Editar produto", None))
        self.action_Voltar.setText(QCoreApplication.translate("FrmEditar", u"&Voltar", None))
#if QT_CONFIG(tooltip)
        self.action_Voltar.setToolTip(QCoreApplication.translate("FrmEditar", u"Volta para a tela inicial", None))
#endif // QT_CONFIG(tooltip)
        self.action_Salvar.setText(QCoreApplication.translate("FrmEditar", u"&Salvar", None))
#if QT_CONFIG(tooltip)
        self.action_Salvar.setToolTip(QCoreApplication.translate("FrmEditar", u"Salva os dados alterados", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("FrmEditar", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("FrmEditar", u"Nome do produto:", None))
        self.label_6.setText(QCoreApplication.translate("FrmEditar", u"Imagem do produto:", None))
        self.label_3.setText(QCoreApplication.translate("FrmEditar", u"Valor do produto:", None))
        self.label_4.setText(QCoreApplication.translate("FrmEditar", u"Descri\u00e7\u00e3o do produto:", None))
        self.label_5.setText(QCoreApplication.translate("FrmEditar", u"Categoria do produto:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FrmEditar", u"toolBar", None))
    # retranslateUi

