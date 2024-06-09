# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmAdicionar.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFormLayout,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QSizePolicy, QSpinBox, QStatusBar,
    QToolBar, QWidget)
import imgs_rc

class Ui_FrmAdicionar(object):
    def setupUi(self, FrmAdicionar):
        if not FrmAdicionar.objectName():
            FrmAdicionar.setObjectName(u"FrmAdicionar")
        FrmAdicionar.resize(800, 550)
        FrmAdicionar.setStyleSheet(u"background: #013C31;")
        self.action_Voltar = QAction(FrmAdicionar)
        self.action_Voltar.setObjectName(u"action_Voltar")
        icon = QIcon()
        icon.addFile(u":/prod/imgsDaRocaBD/voltar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Voltar.setIcon(icon)
        self.action_Salvar = QAction(FrmAdicionar)
        self.action_Salvar.setObjectName(u"action_Salvar")
        icon1 = QIcon()
        icon1.addFile(u":/prod/imgsDaRocaBD/salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Salvar.setIcon(icon1)
        self.centralwidget = QWidget(FrmAdicionar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(230, 120, 321, 151))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.edNome = QLineEdit(self.layoutWidget)
        self.edNome.setObjectName(u"edNome")
        self.edNome.setFont(font)
        self.edNome.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")

        self.gridLayout.addWidget(self.edNome, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.edImagem = QLineEdit(self.layoutWidget)
        self.edImagem.setObjectName(u"edImagem")
        self.edImagem.setFont(font)
        self.edImagem.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")

        self.gridLayout.addWidget(self.edImagem, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.dspbValor = QDoubleSpinBox(self.layoutWidget)
        self.dspbValor.setObjectName(u"dspbValor")
        self.dspbValor.setFont(font)
        self.dspbValor.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.dspbValor.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.dspbValor, 2, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.edDescricao = QLineEdit(self.layoutWidget)
        self.edDescricao.setObjectName(u"edDescricao")
        self.edDescricao.setFont(font)
        self.edDescricao.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")

        self.gridLayout.addWidget(self.edDescricao, 3, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.spbCategoria = QSpinBox(self.layoutWidget)
        self.spbCategoria.setObjectName(u"spbCategoria")
        self.spbCategoria.setFont(font)
        self.spbCategoria.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.spbCategoria.setMinimum(1)
        self.spbCategoria.setMaximum(3)

        self.gridLayout.addWidget(self.spbCategoria, 4, 1, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout)

        FrmAdicionar.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FrmAdicionar)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        FrmAdicionar.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FrmAdicionar)
        self.statusbar.setObjectName(u"statusbar")
        FrmAdicionar.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FrmAdicionar)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setLayoutDirection(Qt.LeftToRight)
        self.toolBar.setStyleSheet(u"background: #FE7411;\n"
"color: #fff;\n"
"")
        self.toolBar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        FrmAdicionar.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_Voltar)
        self.toolBar.addAction(self.action_Salvar)

        self.retranslateUi(FrmAdicionar)

        QMetaObject.connectSlotsByName(FrmAdicionar)
    # setupUi

    def retranslateUi(self, FrmAdicionar):
        FrmAdicionar.setWindowTitle(QCoreApplication.translate("FrmAdicionar", u"Adicionar produto", None))
        self.action_Voltar.setText(QCoreApplication.translate("FrmAdicionar", u"&Voltar", None))
#if QT_CONFIG(tooltip)
        self.action_Voltar.setToolTip(QCoreApplication.translate("FrmAdicionar", u"Retorna para a tela inicial", None))
#endif // QT_CONFIG(tooltip)
        self.action_Salvar.setText(QCoreApplication.translate("FrmAdicionar", u"&Salvar", None))
        self.label.setText(QCoreApplication.translate("FrmAdicionar", u"Nome do produto:", None))
        self.label_2.setText(QCoreApplication.translate("FrmAdicionar", u"Imagem do produto:", None))
        self.label_3.setText(QCoreApplication.translate("FrmAdicionar", u"Valor do produto:", None))
        self.label_4.setText(QCoreApplication.translate("FrmAdicionar", u"Descri\u00e7\u00e3o do produto:", None))
        self.label_5.setText(QCoreApplication.translate("FrmAdicionar", u"Categoria do produto:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FrmAdicionar", u"toolBar", None))
    # retranslateUi

