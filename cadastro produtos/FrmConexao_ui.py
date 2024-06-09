# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmConexao.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_dlgConexao(object):
    def setupUi(self, dlgConexao):
        if not dlgConexao.objectName():
            dlgConexao.setObjectName(u"dlgConexao")
        dlgConexao.resize(400, 300)
        dlgConexao.setStyleSheet(u"background: #013C31;")
        self.buttonBox = QDialogButtonBox(dlgConexao)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setStyleSheet(u"background: #33635A;\n"
"color: #fff;")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(dlgConexao)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 60, 271, 161))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.edServidor = QLineEdit(self.layoutWidget)
        self.edServidor.setObjectName(u"edServidor")
        self.edServidor.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.edServidor.setReadOnly(True)

        self.gridLayout.addWidget(self.edServidor, 0, 1, 1, 1)

        self.edBancoDeDados = QLineEdit(self.layoutWidget)
        self.edBancoDeDados.setObjectName(u"edBancoDeDados")
        self.edBancoDeDados.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.edBancoDeDados.setReadOnly(True)

        self.gridLayout.addWidget(self.edBancoDeDados, 1, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.edSenha = QLineEdit(self.layoutWidget)
        self.edSenha.setObjectName(u"edSenha")
        self.edSenha.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.edSenha.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.edSenha, 3, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #fff;")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.edUserId = QLineEdit(self.layoutWidget)
        self.edUserId.setObjectName(u"edUserId")
        self.edUserId.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.edUserId.setReadOnly(True)

        self.gridLayout.addWidget(self.edUserId, 2, 1, 1, 1)


        self.retranslateUi(dlgConexao)
        self.buttonBox.accepted.connect(dlgConexao.accept)
        self.buttonBox.rejected.connect(dlgConexao.reject)

        QMetaObject.connectSlotsByName(dlgConexao)
    # setupUi

    def retranslateUi(self, dlgConexao):
        dlgConexao.setWindowTitle(QCoreApplication.translate("dlgConexao", u"Conex\u00e3o ao banco de dados", None))
        self.label.setText(QCoreApplication.translate("dlgConexao", u"Endere\u00e7o do servidor:", None))
        self.edServidor.setText(QCoreApplication.translate("dlgConexao", u"regulus.cotuca.unicamp.br", None))
        self.edBancoDeDados.setText(QCoreApplication.translate("dlgConexao", u"BD24587", None))
        self.label_2.setText(QCoreApplication.translate("dlgConexao", u"Nome do BD:", None))
        self.edSenha.setPlaceholderText(QCoreApplication.translate("dlgConexao", u"Digite uma senha", None))
        self.label_3.setText(QCoreApplication.translate("dlgConexao", u"Nome de usu\u00e1rio:", None))
        self.label_4.setText(QCoreApplication.translate("dlgConexao", u"Senha:", None))
        self.edUserId.setText(QCoreApplication.translate("dlgConexao", u"BD24587", None))
    # retranslateUi

