from platform import system

from PySide6.QtWidgets import QFileDialog, QMainWindow

from interface.UI_main_window import Ui_MainWindow
from utils.cli_gen import generate_password
from utils.pop_up import pop_up


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Buttons actions
        self.pushGerarSenha.clicked.connect(self.main)
        self.pushLimpar.clicked.connect(self.listSaida.clear)
        self.pushSair.clicked.connect(self.close)

    def save_password(self, password):
        # Opções de salvamento
        options = QFileDialog.Options()
        options |= QFileDialog.DontConfirmOverwrite
        if system() == 'Linux':
            options |= QFileDialog.DontUseNativeDialog

        arquivo = QFileDialog.getSaveFileName(  # Abre janela de salvamento
            self,
            caption='Salvar senha',
            dir='senhas.txt',
            filter='Arquivo de texto (*.txt);;Todos os arquivos (*)',
            options=options
        )[0]

        if arquivo == '':  # Se o usuário não selecionou um arquivo
            return False

        # Salva a senha no arquivo
        with open(arquivo, 'a') as senhas:
            senhas.write(f'{password}\n')
        return True

    def main(self):
        # Pega os valores dos campos
        letras = int(self.spinLetras.value())
        numeros = int(self.spinNumeros.value())
        caracteres = int(self.spinCaracteres.value())

        if letras == numeros == caracteres == 0:
            pop_up('Erro', 'Impossível gerar senha vazia!', 'critical')
            return

        senha = generate_password(letras, numeros, caracteres)

        # Mostra a senha na tela
        self.listSaida.addItem(senha)
        self.listSaida.scrollToBottom()

        if not self.checkSalvarSenha.isChecked():
            # Se o usuário não quer salvar a senha, retorna
            return

        salvo = self.save_password(senha)

        if not salvo:
            # Se a senha não foi salva mostra uma mensagem de erro e retorna
            pop_up('Erro!', 'Erro ao salvar senha!', 'information')
            return

        pop_up('Senha Salva!', 'Senha salva com sucesso!', 'information')
