import sys
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QDialog, QTableWidgetItem
import pyodbc as bd
from FrmConexao_ui import Ui_dlgConexao
from FrmAdicionar_ui import Ui_FrmAdicionar
from FrmProds_ui import Ui_FrmProds
from FrmEditar_ui import Ui_FrmEditar
from FrmListar_ui import Ui_FrmLista
from FrmRemover_ui import Ui_FrmRemover

class DialogoConexao(QDialog, Ui_dlgConexao):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

class FormPrincipal(QMainWindow, Ui_FrmProds):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.action_Adicionar.triggered.connect(self.adicionarProduto)
        self.action_Editar.triggered.connect(self.editarProduto)
        self.action_Remover.triggered.connect(self.removerProduto)
        self.action_Lista.triggered.connect(self.listarProdutos)
        self.action_Sair.triggered.connect(self.sairDoPrograma)

        self.show()

    def adicionarProduto(self):
        self.janela = FormAdicionar()
        self.close()

    def editarProduto(self):
        self.janela = FormEditar()
        self.close()

    def removerProduto(self):
        self.janela = FormRemover()
        self.close()

    def listarProdutos(self):
        self.janela = FormListar()
        self.close()

    def sairDoPrograma(self):
        self.close()

class FormAdicionar(QMainWindow, Ui_FrmAdicionar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.action_Voltar.triggered.connect(self.voltar)
        self.action_Salvar.triggered.connect(self.salvarProduto)

        self.show()

    def salvarProduto(self):
        nomeProd = self.edNome.text()
        imagemProd = self.edImagem.text()
        precoProd = float(self.dspbValor.value())
        descricaoProd = self.edDescricao.text()
        categoriaProd = int(self.spbCategoria.value())
        sComando = "insert into daroca.produtos " +\
                "values "+\
            f"('{nomeProd}', '{imagemProd}', {precoProd}, '{descricaoProd}', {categoriaProd})"
        
        try:
            meuCursor.execute(sComando)
            meuCursor.commit()
            self.statusBar.showMessage('Inserido')
        except Exception as erro:
            if hasattr(erro, 'message'):
                mensagem = erro.message
            else:
                mensagem = erro.args[1]
            self.statusBar.showMessage(mensagem)
    
    def voltar(self):
        self.janela = FormPrincipal()
        self.close()

class FormEditar(QMainWindow, Ui_FrmEditar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.action_Voltar.triggered.connect(self.voltar)
        self.action_Salvar.triggered.connect(self.salvar)

        self.show()

    def voltar(self):
        self.janela = FormPrincipal()
        self.close()

    def salvar(self):
        idProd = int(self.spbID.value())
        nomeProd = self.edNome.text()
        imagemProd = self.edImagem.text()
        precoProd = float(self.dspbValor.value())
        descricaoProd = self.edDescricao.text()
        categoriaProd = int(self.spbCategoria.value())
        sComando = "update daroca.produtos " +\
                           f"    set nome = '{nomeProd}',"+\
                           f"        imagem = '{imagemProd}',"+\
                           f"        valor = {precoProd},"+\
                           f"        descricao = '{descricaoProd}',"+\
                           f"        categoria = {categoriaProd} "+\
                           f" where id = {idProd} "
        try:
            meuCursor.execute(sComando)
            meuCursor.commit()
            self.statusBar.showMessage('Alterado')
        except Exception as erro:
            if hasattr(erro, 'message'):
                mensagem = erro.message
            else:
                mensagem = erro.args[1]
            self.statusBar.showMessage(mensagem)

class FormRemover(QMainWindow, Ui_FrmRemover):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.action_Voltar.triggered.connect(self.voltar)
        self.action_Salvar.triggered.connect(self.salvar)

        self.show()

    def voltar(self):
        self.janela = FormPrincipal()
        self.close()

    def salvar(self):
        idProd = int(self.spbID.value())
        sComando = 'delete from daroca.produtos ' +\
                               f' where id = {idProd}'
        try:
            meuCursor.execute(sComando)
            meuCursor.commit()
            self.statusBar.showMessage("Excluído")
        except Exception as erro:
            if hasattr(erro, 'message'):
                mensagem = erro.message
            else:
                mensagem = erro.args[1]
            self.statusBar.showMessage(mensagem)

class FormListar(QMainWindow, Ui_FrmLista):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        self.action_Voltar.triggered.connect(self.voltar)
        
        self.show()

    def voltar(self):
        self.janela = FormPrincipal()
        self.close()

aplicacao = QApplication(sys.argv)
dlgCon = DialogoConexao()
if dlgCon.exec() == QDialog.Accepted:
    try:
        conexao = bd.connect(driver = 'SQL Server',
                             server = f'{dlgCon.edServidor.text()}',
                             database = f'{dlgCon.edBancoDeDados.text()}',
                             uid = f'{dlgCon.edUserId.text()}',
                             pwd = f'{dlgCon.edSenha.text()}')
        print('Conexão bem sucedida!')
        meuCursor = conexao.cursor()
        janela = FormPrincipal()
        aplicacao.exec()
    except:
        print('Não foi possível conectar ao banco de dados')