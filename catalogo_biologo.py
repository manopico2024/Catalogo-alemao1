# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Catalogo1.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class Ui_Catalogo(object):
    def setupUi(self, Catalogo):
        Catalogo.setObjectName("Catalogo")
        Catalogo.resize(834, 552)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Catalogo.sizePolicy().hasHeightForWidth())
        Catalogo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Catalogo.setFont(font)
        Catalogo.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/img/RS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Catalogo.setWindowIcon(icon)
        Catalogo.setWindowOpacity(3.0)
        Catalogo.setToolTipDuration(-1)
        Catalogo.setLayoutDirection(QtCore.Qt.RightToLeft)
        Catalogo.setDocumentMode(True)
        Catalogo.setDockNestingEnabled(True)
        Catalogo.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(Catalogo)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(2, 7, 830, 540))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_configuracoes = QtWidgets.QWidget()
        self.tab_configuracoes.setObjectName("tab_configuracoes")
        self.frame_nome = QtWidgets.QFrame(self.tab_configuracoes)
        self.frame_nome.setGeometry(QtCore.QRect(6, 124, 261, 88))
        self.frame_nome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_nome.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(245, 245, 245);")
        self.frame_nome.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_nome.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_nome.setMidLineWidth(0)
        self.frame_nome.setObjectName("frame_nome")
        self.label_nome = QtWidgets.QLabel(self.frame_nome)
        self.label_nome.setGeometry(QtCore.QRect(10, 18, 106, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_nome.setFont(font)
        self.label_nome.setMouseTracking(False)
        self.label_nome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_nome.setAutoFillBackground(False)
        self.label_nome.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border: 1px solid black;")
        self.label_nome.setObjectName("label_nome")
        self.entry_nome = QtWidgets.QLineEdit(self.frame_nome)
        self.entry_nome.setGeometry(QtCore.QRect(122, 18, 128, 20))
        self.entry_nome.setStyleSheet("border:1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.entry_nome.setObjectName("entry_nome")
        self.combobox_status = QtWidgets.QComboBox(self.frame_nome)
        self.combobox_status.setGeometry(QtCore.QRect(122, 50, 129, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_status.sizePolicy().hasHeightForWidth())
        self.combobox_status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combobox_status.setFont(font)
        self.combobox_status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combobox_status.setAutoFillBackground(False)
        self.combobox_status.setStyleSheet("border:1px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.combobox_status.setEditable(False)
        self.combobox_status.setDuplicatesEnabled(False)
        self.combobox_status.setObjectName("combobox_status")
        self.combobox_status.addItem("")
        self.combobox_status.setItemText(0, "")
        self.combobox_status.addItem("")
        self.combobox_status.addItem("")
        self.combobox_status.addItem("")
        self.combobox_status.addItem("")
        self.combobox_status.addItem("")
        self.combobox_status.addItem("")
        self.label_status = QtWidgets.QLabel(self.frame_nome)
        self.label_status.setGeometry(QtCore.QRect(10, 50, 57, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border:1px solid black;")
        self.label_status.setObjectName("label_status")
        self.frame_img = QtWidgets.QFrame(self.tab_configuracoes)
        self.frame_img.setGeometry(QtCore.QRect(292, 33, 520, 180))
        self.frame_img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_img.setAutoFillBackground(True)
        self.frame_img.setStyleSheet("boder: 1px solid black;")
        self.frame_img.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_img.setLineWidth(1)
        self.frame_img.setMidLineWidth(1)
        self.frame_img.setObjectName("frame_img")
        self.text_descricao = QtWidgets.QTextEdit(self.frame_img)
        self.text_descricao.setGeometry(QtCore.QRect(144, 5, 256, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_descricao.setFont(font)
        self.text_descricao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_descricao.setAutoFillBackground(True)
        self.text_descricao.setStyleSheet("border: 0.5px solid black;")
        self.text_descricao.setFrameShape(QtWidgets.QFrame.Box)
        self.text_descricao.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_descricao.setLineWidth(0)
        self.text_descricao.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_descricao.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_descricao.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.text_descricao.setTabChangesFocus(True)
        self.text_descricao.setObjectName("text_descricao")
        self.label_imagem = QtWidgets.QLabel(self.frame_img)
        self.label_imagem.setGeometry(QtCore.QRect(410, 5, 104, 84))
        self.label_imagem.setToolTipDuration(-1)
        self.label_imagem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_imagem.setAutoFillBackground(False)
        self.label_imagem.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.label_imagem.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_imagem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_imagem.setLineWidth(0)
        self.label_imagem.setText("")
        self.label_imagem.setTextFormat(QtCore.Qt.PlainText)
        self.label_imagem.setPixmap(QtGui.QPixmap("../../.designer/backup/img/RS.png"))
        self.label_imagem.setScaledContents(True)
        self.label_imagem.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imagem.setWordWrap(True)
        self.label_imagem.setIndent(7)
        self.label_imagem.setOpenExternalLinks(False)
        self.label_imagem.setObjectName("label_imagem")
        self.button_imagem = QtWidgets.QPushButton(self.frame_img)
        self.button_imagem.setGeometry(QtCore.QRect(414, 94, 96, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_imagem.setFont(font)
        self.button_imagem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_imagem.setAutoFillBackground(False)
        self.button_imagem.setAutoDefault(True)
        self.button_imagem.setDefault(True)
        self.button_imagem.setFlat(False)
        self.button_imagem.setObjectName("button_imagem")
        self.button_imagem.clicked.connect(self.carregar_imagem)
        self.label_descricao = QtWidgets.QLabel(self.frame_img)
        self.label_descricao.setGeometry(QtCore.QRect(64, 5, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_descricao.setFont(font)
        self.label_descricao.setStyleSheet("border:1px solid black;\n"
"background-color: rgb(218, 218, 218);")
        self.label_descricao.setObjectName("label_descricao")
        self.button_salvar_arquivo = QtWidgets.QPushButton(self.frame_img)
        self.button_salvar_arquivo.setGeometry(QtCore.QRect(414, 120, 96, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button_salvar_arquivo.setFont(font)
        self.button_salvar_arquivo.setAutoDefault(True)
        self.button_salvar_arquivo.setDefault(True)
        self.button_salvar_arquivo.setObjectName("button_salvar_arquivo")
        ##self.button_salvar_arquivo.clicked.connect(self.adicionar_especie())
        self.label_logo = QtWidgets.QLabel(self.tab_configuracoes)
        self.label_logo.setGeometry(QtCore.QRect(7, 34, 262, 51))
        self.label_logo.setStyleSheet("background-color: rgb(245,245,245);\n"
"border:0.5px solid black;")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.button_limpar = QtWidgets.QPushButton(self.tab_configuracoes)
        self.button_limpar.setGeometry(QtCore.QRect(90, 230, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_limpar.setFont(font)
        self.button_limpar.setToolTipDuration(-1)
        self.button_limpar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_limpar.setAutoFillBackground(False)
        self.button_limpar.setAutoDefault(True)
        self.button_limpar.setDefault(True)
        self.button_limpar.setObjectName("button_limpar")
        ##self.button_limpar.clicked.connect(self.limpar_campos)
        self.button_adicionar = QtWidgets.QPushButton(self.tab_configuracoes)
        self.button_adicionar.setGeometry(QtCore.QRect(10, 230, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_adicionar.setFont(font)
        self.button_adicionar.setToolTipDuration(-1)
        self.button_adicionar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_adicionar.setAutoFillBackground(False)
        self.button_adicionar.setAutoRepeatDelay(300)
        self.button_adicionar.setAutoDefault(True)
        self.button_adicionar.setDefault(True)
        self.button_adicionar.setFlat(False)
        self.button_adicionar.clicked.connect(self.adicionar_especie)
        self.button_adicionar.setObjectName("button_adicionar")
        self.button_buscar = QtWidgets.QPushButton(self.tab_configuracoes)
        self.button_buscar.setGeometry(QtCore.QRect(170, 230, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_buscar.setFont(font)
        self.button_buscar.setToolTipDuration(-1)
        self.button_buscar.setAutoDefault(True)
        self.button_buscar.setDefault(True)
        self.button_buscar.setFlat(False)
        self.button_buscar.setObjectName("button_buscar")
        ##self.button_buscar.clicked.connect(self.b)
        self.button_remover = QtWidgets.QPushButton(self.tab_configuracoes)
        self.button_remover.setGeometry(QtCore.QRect(250, 230, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_remover.setFont(font)
        self.button_remover.setToolTipDuration(-1)
        self.button_remover.setAutoDefault(True)
        self.button_remover.setDefault(True)
        self.button_remover.setObjectName("button_remover")
        self.button_buscar.raise_()
        self.button_limpar.raise_()
        self.button_adicionar.raise_()
        self.frame_nome.raise_()
        self.frame_img.raise_()
        self.label_logo.raise_()
        self.button_remover.raise_()
        self.tabWidget.addTab(self.tab_configuracoes, "")
        Catalogo.setCentralWidget(self.centralwidget)

        self.retranslateUi(Catalogo)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Catalogo)
        # Tabela para listar espécies
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(8, 310, 818, 235))
        self.table.setColumnCount(4)  # Adicionamos uma coluna para a imagem
        self.table.setHorizontalHeaderLabels(["Nome", "Descrição", "Status", "Imagem"])
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 300)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 100)
        self.table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
    def retranslateUi(self, Catalogo):
        _translate = QtCore.QCoreApplication.translate
        Catalogo.setWindowTitle(_translate("Catalogo", "Catálogo"))
        self.label_nome.setText(_translate("Catalogo", "Nome da Espécie:"))
        self.combobox_status.setItemText(1, _translate("Catalogo", "Pouco precoupante"))
        self.combobox_status.setItemText(2, _translate("Catalogo", "Preocupante"))
        self.combobox_status.setItemText(3, _translate("Catalogo", "Alerta"))
        self.combobox_status.setItemText(4, _translate("Catalogo", "Em Extinção"))
        self.combobox_status.setItemText(5, _translate("Catalogo", "Crítico"))
        self.combobox_status.setItemText(6, _translate("Catalogo", "Extinto"))
        self.label_status.setText(_translate("Catalogo", "Status:"))
        self.button_imagem.setText(_translate("Catalogo", "Imagem"))
        self.label_descricao.setText(_translate("Catalogo", "Descrição:"))
        self.button_salvar_arquivo.setText(_translate("Catalogo", "Salvar Arquivo"))
        self.button_limpar.setText(_translate("Catalogo", "Limpar"))
        self.button_adicionar.setText(_translate("Catalogo", "Cadastrar"))
        self.button_buscar.setText(_translate("Catalogo", "Buscar"))
        self.button_remover.setText(_translate("Catalogo", "Deletar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_configuracoes), _translate("Catalogo", "Configurações"))
        # Carrega os dados na tabela ao iniciar
        self.listar_especies()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS especies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE NOT NULL,
                status TEXT,
                descricao TEXT,
                imagem BLOB
            )
        """)
        self.conn.commit()

    def carregar_imagem(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Imagem", "",
                                                   "Imagens (*.png *.jpg *.jpeg *.bmp);;", options=options)

        if file_path:
            self.caminho_imagem = file_path
            pixmap = QtGui.QPixmap(file_path)
            self.label_imagem.setPixmap(pixmap)

    def adicionar_especie(self):
        nome = self.entry_nome.text().strip()
        status = self.combobox_status.currentText().strip()
        descricao = self.text_descricao.toPlainText().strip()

        if not nome:
            QMessageBox.critical(None, "Erro", "O nome da espécie é obrigatório!")
            return

        imagem_bytes = None
        if self.caminho_imagem:
            with open(self.caminho_imagem, "rb") as file:
                imagem_bytes = file.read()

        try:
            self.cursor.execute("""
                INSERT INTO especies (nome, status, descricao, imagem)
                VALUES (?, ?, ?, ?)
            """, (nome, status, descricao, imagem_bytes))
            self.conn.commit()
            QMessageBox.information(None, "Sucesso", "Espécie cadastrada com sucesso!")
            self.listar_especies()
            self.limpar_campos()
        except sqlite3.IntegrityError:
            QMessageBox.critical(None, "Erro", "Espécie já cadastrada!")

    def editar_especie(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(None, "Aviso", "Selecione uma espécie para editar!")
            return

        nome = self.entry_nome.text().strip()
        status = self.combobox_status.currentText().strip()
        descricao = self.text_descricao.toPlainText().strip()

        imagem_bytes = None
        if self.caminho_imagem:
            with open(self.caminho_imagem, "rb") as file:
                imagem_bytes = file.read()

        self.cursor.execute("""
            UPDATE especies SET status = ?, descricao = ?, imagem = ?
            WHERE nome = ?
        """, (status, descricao, imagem_bytes, nome))
        self.conn.commit()

        QMessageBox.information(None, "Sucesso", "Espécie editada com sucesso!")
        self.listar_especies()

    def remover_especie(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(None, "Aviso", "Selecione uma espécie para remover!")
            return

        nome = self.table.item(selected_row, 0).text()

        resposta = QMessageBox.question(None, "Confirmar", f"Tem certeza que deseja remover '{nome}'?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resposta == QMessageBox.Yes:
            self.cursor.execute("DELETE FROM especies WHERE nome = ?", (nome,))
            self.conn.commit()
            QMessageBox.information(None, "Sucesso", "Espécie removida com sucesso!")
            self.listar_especies()

    def listar_especies(self):
        self.cursor.execute("SELECT nome, descricao, status, imagem FROM especies")
        dados = self.cursor.fetchall()

        self.table.setRowCount(len(dados))
        for row_index, row_data in enumerate(dados):
            nome, descricao, status, imagem_bytes = row_data

            # Adiciona os dados nas colunas de texto
            self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(nome))
            self.table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(descricao))
            self.table.setItem(row_index, 2, QtWidgets.QTableWidgetItem(status))

            # Adiciona a imagem na coluna de imagem
            if imagem_bytes:
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(imagem_bytes)
                icon = QtGui.QIcon(pixmap)
                item = QtWidgets.QTableWidgetItem()
                item.setIcon(icon)
                self.table.setItem(row_index, 3, item)

    def mostrar_detalhes_especie(self, row):
        nome = self.table.item(row, 0).text()
        descricao = self.table.item(row, 1).text()
        status = self.table.item(row, 2).text()
        imagem_bytes = self.cursor.execute("SELECT imagem FROM especies WHERE nome = ?", (nome,)).fetchone()[0]

        self.entry_nome.setText(nome)
        self.text_descricao.setText(descricao)
        self.combobox_status.setCurrentText(status)

        if imagem_bytes:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(imagem_bytes)
            self.label_imagem.setPixmap(pixmap)
        else:
            self.label_imagem.clear()

    def limpar_campos(self):
        """Limpa todos os campos de entrada"""
        self.entry_nome.clear()
        self.text_descricao.clear()
        self.combobox_status.setCurrentIndex(0)
        self.label_imagem.clear()
        self.caminho_imagem = None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Catalogo = QtWidgets.QMainWindow()
    ui = Ui_Catalogo()
    ui.setupUi(Catalogo)
    Catalogo.show()
    sys.exit(app.exec_())
