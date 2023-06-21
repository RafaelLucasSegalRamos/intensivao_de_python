from PyQt5 import uic, QtWidgets
from sys import argv, exit


class Controle_financeiro:
    def __init__(self) -> None:
        pass

    def add_item(self):
        descricao = tela_prin.line_descricao.text()

        if tela_prin.entrada.isChecked():
            self.valor_entrou = float(self.valor_entrou) + float(valor)
            self.valor_total =  float(self.valor_total) + float(valor)

            tela_prin.btt_entrada.setText(f'R${self.valor_entrou:.2f}')
            tela_prin.btt_total.setText(f'R${self.valor_total:.2f}')

            tipo = '+'

        elif tela_prin.saida.isChecked():
            self.valor_saiu = float(self.valor_saiu) + float(valor)
            self.valor_total = float(self.valor_total) - float(valor)

            tela_prin.btt_saida.setText(f'R${self.valor_saiu:.2f}')
            tela_prin.btt_total.setText(f'R${self.valor_total:.2f}')

            tipo = '-'

        tela_prin.tableWidget.setRowCount(self.linha+1)
        tela_prin.tableWidget.setColumnCount(3)
        tela_prin.tableWidget.setItem(self.linha, 0,QtWidgets.QTableWidgetItem(f'{descricao}'))
        tela_prin.tableWidget.setItem(self.linha, 1, QtWidgets.QTableWidgetItem(f'{valor}'))
        tela_prin.tableWidget.setItem(self.linha, 2, QtWidgets.QTableWidgetItem(f'{tipo}'))


app = QtWidgets.QApplication(argv)
tela_prin = uic.loadUi(r'storage\front\guis\gui_principal.ui')
tela_prin.show()
funcao = Controle_financeiro()
tela_prin.adcionar.clicked.connect(funcao.add_item())
exit(app.exec_())