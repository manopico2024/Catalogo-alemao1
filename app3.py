from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sqlite3
import folium
import webbrowser
import os


class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.setFixedSize(1012, 668)
        root.setUnifiedTitleAndToolBarOnMac(False)

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")

        # Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, 0, 1161, 711))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")

        # Tab Configurações
        self.tab_configuracoes = QtWidgets.QWidget()
        self.tab_configuracoes.setObjectName("tab_configuracoes")

        # Frame Root
        self.frame_root = QtWidgets.QFrame(self.tab_configuracoes)
        self.frame_root.setGeometry(QtCore.QRect(-1, -3, 1151, 711))
        self.frame_root.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_root.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_root.setObjectName("frame_root")

        # Label do Logo
        self.lb_logo = QtWidgets.QLabel(self.frame_root)
        self.lb_logo.setGeometry(QtCore.QRect(10, 70, 150, 131))
        self.lb_logo.setStyleSheet("")
        self.lb_logo.setText("")
        self.lb_logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.lb_logo.setScaledContents(True)
        self.lb_logo.setObjectName("lb_logo")

        # Tabela para listar espécies
        self.table = QtWidgets.QTableWidget(self.tab_configuracoes)
        self.table.setGeometry(QtCore.QRect(500, 300, 480, 270))
        self.table.setColumnCount(5)  # Adicionamos uma coluna para a imagem
        self.table.setHorizontalHeaderLabels(["Id", "Nome", "Descrição", "Status", "Imagem"])
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 140)
        self.table.setColumnWidth(2, 170)
        self.table.setColumnWidth(3, 120)
        self.table.setColumnWidth(4, 150)
        self.table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        # Frame da Imagem
        self.frame_img = QtWidgets.QFrame(self.frame_root)
        self.frame_img.setGeometry(QtCore.QRect(480, 70, 520, 180))
        self.frame_img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_img.setAutoFillBackground(True)
        self.frame_img.setStyleSheet("border: 1px solid black;")
        self.frame_img.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_img.setLineWidth(1)
        self.frame_img.setMidLineWidth(1)
        self.frame_img.setObjectName("frame_img")

        # Text Edit para Descrição
        self.txt_descricao = QtWidgets.QTextEdit(self.frame_img)
        self.txt_descricao.setGeometry(QtCore.QRect(144, 5, 256, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_descricao.setFont(font)
        self.txt_descricao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_descricao.setAutoFillBackground(True)
        self.txt_descricao.setStyleSheet("border: 0.5px solid black;")
        self.txt_descricao.setFrameShape(QtWidgets.QFrame.Box)
        self.txt_descricao.setFrameShadow(QtWidgets.QFrame.Plain)
        self.txt_descricao.setLineWidth(0)
        self.txt_descricao.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txt_descricao.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txt_descricao.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.txt_descricao.setTabChangesFocus(True)
        self.txt_descricao.setObjectName("txt_descricao")

        self.lb_imagem = QtWidgets.QLabel(self.frame_img)
        self.lb_imagem.setGeometry(QtCore.QRect(410, 5, 104, 84))
        self.lb_imagem.setToolTipDuration(-1)
        self.lb_imagem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_imagem.setAutoFillBackground(False)
        self.lb_imagem.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "border: 1px solid black;")
        self.lb_imagem.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lb_imagem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lb_imagem.setLineWidth(0)
        self.lb_imagem.setText("")
        self.lb_imagem.setTextFormat(QtCore.Qt.PlainText)
        self.lb_imagem.setPixmap(QtGui.QPixmap("../../.designer/backup/img/RS.png"))
        self.lb_imagem.setScaledContents(True)
        self.lb_imagem.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_imagem.setWordWrap(True)
        self.lb_imagem.setIndent(7)
        self.lb_imagem.setOpenExternalLinks(False)
        self.lb_imagem.setObjectName("lb_imagem")
        self.btn_imagem = QtWidgets.QPushButton(self.frame_img)
        self.btn_imagem.setGeometry(QtCore.QRect(412, 94, 100, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_imagem.setFont(font)
        self.btn_imagem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_imagem.setAutoFillBackground(False)
        self.btn_imagem.setAutoDefault(True)
        self.btn_imagem.setDefault(True)
        self.btn_imagem.setFlat(False)
        self.btn_imagem.setObjectName("btn_imagem")
        # Label da Descrição
        self.lb_descricao = QtWidgets.QLabel(self.frame_img)
        self.lb_descricao.setGeometry(QtCore.QRect(64, 5, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_descricao.setFont(font)
        self.lb_descricao.setStyleSheet("border:1px solid black")
        self.lb_descricao.setObjectName("lb_descricao")

        # Botão para Salvar Arquivo
        self.btn_salvar_arquivo = QtWidgets.QPushButton(self.frame_img)
        self.btn_salvar_arquivo.setGeometry(QtCore.QRect(412, 120, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_salvar_arquivo.setFont(font)
        self.btn_salvar_arquivo.setAutoDefault(True)
        self.btn_salvar_arquivo.setDefault(True)
        self.btn_salvar_arquivo.setObjectName("btn_salvar_arquivo")

        # Frame da Tabela
        self.frame_table = QtWidgets.QFrame(self.frame_root)
        self.frame_table.setGeometry(QtCore.QRect(480, 272, 521, 320))
        self.frame_table.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                      "border:0.5px solid black;")
        self.frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")

        # Group Box da Tabela
        self.gb_tabela = QtWidgets.QGroupBox(self.frame_table)
        self.gb_tabela.setGeometry(QtCore.QRect(10, 10, 500, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_tabela.setFont(font)
        self.gb_tabela.setObjectName("gb_tabela")

        # Group Box dos Dados
        self.gb_dados = QtWidgets.QGroupBox(self.frame_root)
        self.gb_dados.setGeometry(QtCore.QRect(10, 273, 311, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_dados.setFont(font)
        self.gb_dados.setStyleSheet("background-color: rgb(230, 230, 230);\n"
                                    "border: 0.5px solid black;\n"
                                    "")
        self.gb_dados.setObjectName("gb_dados")

        # Frame dos Dados
        self.frame_dados = QtWidgets.QFrame(self.gb_dados)
        self.frame_dados.setGeometry(QtCore.QRect(10, 20, 291, 231))
        self.frame_dados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dados.setObjectName("frame_dados")

        # Campo de Nome
        self.txt_nome = QtWidgets.QLineEdit(self.frame_dados)
        self.txt_nome.setGeometry(QtCore.QRect(122, 10, 160, 20))
        self.txt_nome.setStyleSheet("border:1px solid black;\n"
                                    "background-color: rgb(255, 255, 255);")
        self.txt_nome.setObjectName("txt_nome")

        # Label do Status
        self.lb_status = QtWidgets.QLabel(self.frame_dados)
        self.lb_status.setGeometry(QtCore.QRect(10, 42, 57, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_status.setFont(font)
        self.lb_status.setStyleSheet("background-color: rgb(218, 218, 218);\n"
                                     "border:1px solid black;")
        self.lb_status.setObjectName("lb_status")

        # Combo Box do Status
        self.combobox_status = QtWidgets.QComboBox(self.frame_dados)
        self.combobox_status.setGeometry(QtCore.QRect(122, 42, 160, 20))
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

        # Label do Nome
        self.lb_nome = QtWidgets.QLabel(self.frame_dados)
        self.lb_nome.setGeometry(QtCore.QRect(10, 10, 106, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lb_nome.setFont(font)
        self.lb_nome.setMouseTracking(False)
        self.lb_nome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_nome.setAutoFillBackground(False)
        self.lb_nome.setStyleSheet("background-color: rgb(218, 218, 218);\n"
                                   "border: 1px solid black;")
        self.lb_nome.setObjectName("lb_nome")

        # Botão Remover
        self.btn_remover = QtWidgets.QPushButton(self.frame_root)
        self.btn_remover.setGeometry(QtCore.QRect(248, 540, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_remover.setFont(font)
        self.btn_remover.setToolTipDuration(-1)
        self.btn_remover.setAutoDefault(True)
        self.btn_remover.setDefault(True)
        self.btn_remover.setObjectName("btn_remover")

        # Botão Limpar
        self.btn_limpar = QtWidgets.QPushButton(self.frame_root)
        self.btn_limpar.setGeometry(QtCore.QRect(90, 540, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_limpar.setFont(font)
        self.btn_limpar.setToolTipDuration(-1)
        self.btn_limpar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_limpar.setAutoFillBackground(False)
        self.btn_limpar.setAutoDefault(True)
        self.btn_limpar.setDefault(True)
        self.btn_limpar.setObjectName("btn_limpar")

        # Botão Buscar
        self.btn_buscar = QtWidgets.QPushButton(self.frame_root)
        self.btn_buscar.setGeometry(QtCore.QRect(168, 540, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_buscar.setFont(font)
        self.btn_buscar.setToolTipDuration(-1)
        self.btn_buscar.setAutoDefault(True)
        self.btn_buscar.setDefault(True)
        self.btn_buscar.setFlat(False)
        self.btn_buscar.setObjectName("btn_buscar")

        # Botão Adicionar
        self.btn_adicionar = QtWidgets.QPushButton(self.frame_root)
        self.btn_adicionar.setGeometry(QtCore.QRect(10, 540, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_adicionar.setFont(font)
        self.btn_adicionar.setToolTipDuration(-1)
        self.btn_adicionar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_adicionar.setAutoFillBackground(False)
        self.btn_adicionar.setAutoRepeatDelay(300)
        self.btn_adicionar.setAutoDefault(True)
        self.btn_adicionar.setDefault(True)
        self.btn_adicionar.setFlat(False)
        self.btn_adicionar.setObjectName("btn_adicionar")

        # Adicionar Tab Configurações
        self.tabWidget.addTab(self.tab_configuracoes, "")
        root.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(root)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        root.setMenuBar(self.menubar)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(root)
        self.statusbar.setObjectName("statusbar")
        root.setStatusBar(self.statusbar)

        # Action Configurações
        self.actionConfiguracoes = QtWidgets.QAction(root)
        self.actionConfiguracoes.setObjectName("actionConfiguracoes")
        self.menuMenu.addAction(self.actionConfiguracoes)
        self.menubar.addAction(self.menuMenu.menuAction())

        # Conectar Botões
        self.btn_adicionar.clicked.connect(self.adicionar_especie)
        self.btn_imagem.clicked.connect(self.carregar_imagem)
        self.btn_buscar.clicked.connect(self.buscar_especie)
        self.btn_limpar.clicked.connect(self.limpar_campos)
        # Conectar o evento de clique na tabela
        self.table.cellClicked.connect(self.preencher_campos)

        # Inicializar Banco de Dados
        self.conn = sqlite3.connect('especies.db')
        self.cursor = self.conn.cursor()
        self.criar_tabela()
        self.caminho_imagem = None

        # Traduzir Interface
        self.retranslateUi(root)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(root)

        # Botão para abrir o mapa
        self.btn_mapa = QtWidgets.QPushButton(self.frame_root)
        self.btn_mapa.setGeometry(QtCore.QRect(330, 540, 100, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mapa.setFont(font)
        self.btn_mapa.setText("Abrir Mapa")
        self.btn_mapa.clicked.connect(self.abrir_mapa)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "Catalogo"))
        self.btn_imagem.setText(_translate("root", "Imagem"))
        self.lb_descricao.setText(_translate("root", "Descrição:"))
        self.btn_salvar_arquivo.setText(_translate("root", "Salvar Arquivo"))
        self.gb_tabela.setTitle(_translate("root", "Tabela"))
        self.gb_dados.setTitle(_translate("root", "Dados"))
        self.lb_status.setText(_translate("root", "Status:"))
        self.combobox_status.setItemText(1, _translate("root", "Pouco precoupante"))
        self.combobox_status.setItemText(2, _translate("root", "Preocupante"))
        self.combobox_status.setItemText(3, _translate("root", "Alerta"))
        self.combobox_status.setItemText(4, _translate("root", "Em Extinção"))
        self.combobox_status.setItemText(5, _translate("root", "Crítico"))
        self.combobox_status.setItemText(6, _translate("root", "Extinto"))
        self.lb_nome.setText(_translate("root", "Nome da Espécie:"))
        self.btn_remover.setText(_translate("root", "Deletar"))
        self.btn_limpar.setText(_translate("root", "Limpar"))
        self.btn_buscar.setText(_translate("root", "Buscar"))
        self.btn_adicionar.setText(_translate("root", "Cadastrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_configuracoes), _translate("root", "Configurações"))
        self.menuMenu.setTitle(_translate("root", "Menu"))
        self.actionConfiguracoes.setText(_translate("root", "Configuracoes"))

    def adicionar_especie(self):
        """Adiciona uma nova espécie ao banco de dados e atualiza a tabela"""
        nome = self.txt_nome.text().strip()
        status = self.combobox_status.currentText()
        descricao = self.txt_descricao.toPlainText().strip()

        if not nome:
            QtWidgets.QMessageBox.warning(None, "Erro", "O nome da espécie é obrigatório!")
            return

        try:
            imagem_blob = None
            if self.caminho_imagem:
                with open(self.caminho_imagem, "rb") as file:
                    imagem_blob = file.read()

            self.cursor.execute(
                "INSERT INTO especies (nome, status, descricao, imagem) VALUES (?, ?, ?, ?)",
                (nome, status, descricao, imagem_blob),
            )
            self.conn.commit()
            QtWidgets.QMessageBox.information(None, "Sucesso", "Espécie adicionada com sucesso!")
            self.listar_especies()  # Atualiza a tabela na interface
            self.limpar_campos()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Erro", f"Erro ao adicionar a espécie: {str(e)}")

    def criar_tabela(self):
        """Cria a tabela no banco de dados, se não existir"""
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
        """Abre o seletor de arquivos para escolher uma imagem e exibi-la na tela"""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Selecionar Imagem", "",
                                                   "Imagens (*.png *.jpg *.jpeg *.bmp);;", options=options)

        if file_path:
            self.caminho_imagem = file_path
            pixmap = QtGui.QPixmap(file_path)
            self.lb_imagem.setPixmap(pixmap)

    def listar_especies(self):
        """Carrega os dados do banco de dados e exibe na tabela"""
        self.cursor.execute("SELECT id, nome, descricao, status, imagem FROM especies")
        dados = self.cursor.fetchall()

        self.table.setRowCount(0)  # Limpa a tabela antes de preencher
        for row_index, row_data in enumerate(dados):
            self.table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                if col_index == 4:  # Coluna da imagem
                    if cell_data:
                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(cell_data)
                        label = QtWidgets.QLabel()
                        label.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio))
                        self.table.setCellWidget(row_index, col_index, label)
                    else:
                        self.table.setItem(row_index, col_index, QtWidgets.QTableWidgetItem("Sem imagem"))
                else:
                    self.table.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(cell_data)))

    def limpar_campos(self):
        """Limpa os campos do formulário"""
        self.txt_nome.clear()
        self.txt_descricao.clear()
        self.combobox_status.setCurrentIndex(0)
        self.lb_imagem.clear()
        self.caminho_imagem = None

    def buscar_especie(self):
        """Busca espécies no banco de dados com base no nome e exibe os resultados na tabela"""
        nome_busca = self.txt_nome.text().strip()

        if not nome_busca:
            QtWidgets.QMessageBox.warning(None, "Aviso", "Digite um nome para buscar!")
            return

        try:
            self.cursor.execute("SELECT id, nome, descricao, status, imagem FROM especies WHERE nome LIKE ?",
                                (f"%{nome_busca}%",))
            resultados = self.cursor.fetchall()

            if not resultados:
                QtWidgets.QMessageBox.information(None, "Resultado", "Nenhuma espécie encontrada!")
                return

            self.table.setRowCount(0)  # Limpa a tabela antes de preencher
            for row_index, row_data in enumerate(resultados):
                self.table.insertRow(row_index)
                for col_index, cell_data in enumerate(row_data):
                    if col_index == 4:  # Coluna da imagem
                        if cell_data:
                            pixmap = QtGui.QPixmap()
                            pixmap.loadFromData(cell_data)
                            label = QtWidgets.QLabel()
                            label.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio))
                            self.table.setCellWidget(row_index, col_index, label)
                        else:
                            self.table.setItem(row_index, col_index, QtWidgets.QTableWidgetItem("Sem imagem"))
                    else:
                        self.table.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(cell_data)))

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Erro", f"Erro ao buscar espécies: {str(e)}")

    def preencher_campos(self, row):
        """Preenche os campos do formulário com os dados da linha selecionada na tabela"""
        try:
            # Obtém os dados da linha clicada
            id_especie = self.table.item(row, 0).text()
            nome = self.table.item(row, 1).text()
            descricao = self.table.item(row, 2).text()
            status = self.table.item(row, 3).text()

            # Preenche os campos
            self.txt_nome.setText(nome)
            self.txt_descricao.setPlainText(descricao)
            self.combobox_status.setCurrentText(status)

            # Verifica se há uma imagem na célula
            if self.table.cellWidget(row, 4):
                imagem = self.table.cellWidget(row, 4).pixmap()
                self.lb_imagem.setPixmap(imagem)
            else:
                self.lb_imagem.clear()
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Erro", f"Erro ao preencher campos: {str(e)}")

    def abrir_mapa(self):
        """Gera um mapa interativo com Folium e abre no navegador padrão"""
        # Criar um mapa com Folium
        mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)  # Centralizado no Brasil

        # Adicionar marcadores com base nos dados do banco de dados
        self.cursor.execute("SELECT nome, descricao, status FROM especies")
        especies = self.cursor.fetchall()

        for especie in especies:
            nome, descricao, status = especie
            # Exemplo de coordenadas (substitua por coordenadas reais)
            lat, lon = -15.788497, -47.879873  # Coordenadas de Brasília
            popup = f"<b>{nome}</b><br>{descricao}<br>Status: {status}"
            folium.Marker([lat, lon], popup=popup).add_to(mapa)

        # Salvar o mapa em um arquivo HTML temporário
        mapa.save("mapa.html")

        # Abrir o arquivo HTML no navegador padrão
        webbrowser.open("mapa.html")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())