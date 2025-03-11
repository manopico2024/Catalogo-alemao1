import sqlite3
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import Image, ImageTk
import io

class CatalogoEspecies(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Conexão com o banco de dados
        self.conn = sqlite3.connect("catalogo_especies.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

        # Elementos da interface
        self.init_ui()

    def init_ui(self):
        # Layout principal
        self.setWindowTitle("Catálogo de Espécies")
        self.setGeometry(100, 100, 1366, 780)

        layout = QtWidgets.QVBoxLayout(self)

        # Campos de entrada
        self.label_nome = QtWidgets.QLabel("Nome da Espécie:")
        self.entry_nome = QtWidgets.QLineEdit()
        layout.addWidget(self.label_nome)
        layout.addWidget(self.entry_nome)

        self.label_status = QtWidgets.QLabel("Nível de Extinção:")
        self.combobox_status = QtWidgets.QComboBox()
        self.combobox_status.addItems(["Crítico", "Em Perigo", "Vulnerável", "Pouco Preocupante"])
        layout.addWidget(self.label_status)
        layout.addWidget(self.combobox_status)

        self.button_imagem = QtWidgets.QPushButton("Carregar Imagem")
        self.button_imagem.clicked.connect(self.carregar_imagem)
        layout.addWidget(self.button_imagem)

        self.label_descricao = QtWidgets.QLabel("Descrição:")
        self.text_descricao = QtWidgets.QTextEdit()
        layout.addWidget(self.label_descricao)
        layout.addWidget(self.text_descricao)

        # Botões
        self.button_adicionar = QtWidgets.QPushButton("Adicionar/Salvar Espécie")
        self.button_adicionar.clicked.connect(self.adicionar_especie)
        layout.addWidget(self.button_adicionar)

        self.button_remover = QtWidgets.QPushButton("Remover Espécie")
        self.button_remover.clicked.connect(self.remover_especie)
        layout.addWidget(self.button_remover)

        self.button_buscar = QtWidgets.QPushButton("Buscar Espécie")
        self.button_buscar.clicked.connect(self.buscar_especie)
        layout.addWidget(self.button_buscar)

        self.button_limpar = QtWidgets.QPushButton("Limpar")
        self.button_limpar.clicked.connect(self.limpar_treeview)
        layout.addWidget(self.button_limpar)

        self.button_roadmap = QtWidgets.QPushButton("Exibir Roadmap")
        self.button_roadmap.clicked.connect(self.exibir_roadmap_selecionado)
        layout.addWidget(self.button_roadmap)

        # Treeview para listar espécies
        self.treeview_especies = QtWidgets.QTableWidget()
        self.treeview_especies.setColumnCount(3)
        self.treeview_especies.setHorizontalHeaderLabels(["Nome", "Descrição", "Status"])
        self.treeview_especies.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeview_especies.itemSelectionChanged.connect(self.mostrar_no_roadmap)
        layout.addWidget(self.treeview_especies)

        # Exibir imagem
        self.canvas_imagem = QtWidgets.QLabel()
        self.canvas_imagem.setFixedSize(100, 100)
        layout.addWidget(self.canvas_imagem)

        # Canvas para roadmap
        self.canvas_roadmap = QtWidgets.QLabel()
        self.canvas_roadmap.setFixedSize(645, 332)
        layout.addWidget(self.canvas_roadmap)

        self.caminho_imagem = None
        self.imagem_tk = None

        # Preencher a Treeview com as espécies
        self.listar_especies()

        self.show()

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
        file_dialog = QtWidgets.QFileDialog()
        self.caminho_imagem, _ = file_dialog.getOpenFileName(self, "Abrir Imagem", "", "Arquivos de Imagem (*.jpg;*.png;*.jpeg)")
        if self.caminho_imagem:
            imagem = Image.open(self.caminho_imagem)
            imagem = imagem.resize((100, 100))
            imagem_qt = QtGui.QImage(imagem.tobytes(), imagem.width, imagem.height, imagem.width * 3, QtGui.QImage.Format_RGB888)
            self.imagem_tk = QtGui.QPixmap.fromImage(imagem_qt)
            self.canvas_imagem.setPixmap(self.imagem_tk)

    def adicionar_especie(self):
        nome = self.entry_nome.text().strip()
        status = self.combobox_status.currentText().strip()
        descricao = self.text_descricao.toPlainText().strip()

        if not nome:
            QtWidgets.QMessageBox.critical(self, "Erro", "O nome da espécie é obrigatório!")
            return

        imagem_bytes = None
        if self.caminho_imagem:
            with open(self.caminho_imagem, "rb") as file:
                imagem_bytes = file.read()

        try:
            self.cursor.execute("""
                INSERT OR REPLACE INTO especies (nome, status, descricao, imagem)
                VALUES (?, ?, ?, ?)
            """, (nome, status, descricao, imagem_bytes))
            self.conn.commit()
            QtWidgets.QMessageBox.information(self, "Sucesso", "Espécie salva com sucesso!")
            self.listar_especies()
            self.limpar_campos()
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.critical(self, "Erro", "Espécie já cadastrada!")

    def remover_especie(self):
        selected_row = self.treeview_especies.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.critical(self, "Erro", "Selecione uma espécie para remover!")
            return

        nome = self.treeview_especies.item(selected_row, 0).text()
        self.cursor.execute("DELETE FROM especies WHERE nome = ?", (nome,))
        self.conn.commit()
        QtWidgets.QMessageBox.information(self, "Sucesso", "Espécie removida com sucesso!")
        self.listar_especies()

    def buscar_especie(self):
        nome = self.entry_nome.text().strip()
        if not nome:
            QtWidgets.QMessageBox.critical(self, "Erro", "Digite o nome da espécie para buscar!")
            return

        self.cursor.execute("SELECT nome, status, descricao, imagem FROM especies WHERE nome = ?", (nome,))
        especie = self.cursor.fetchone()

        if especie:
            self.exibir_roadmap([especie])
        else:
            QtWidgets.QMessageBox.critical(self, "Erro", "Espécie não encontrada!")

    def exibir_roadmap(self, especies):
        # Limpar o conteúdo anterior
        self.canvas_roadmap.clear()
        self.canvas_roadmap.setText("")
        x, y = 10, 10

        for especie in especies:
            nome, status, descricao, imagem_bytes = especie

            # Exibe a imagem (se houver)
            if imagem_bytes:
                imagem = Image.open(io.BytesIO(imagem_bytes)).resize((90, 90))
                imagem_qt = QtGui.QImage(imagem.tobytes(), imagem.width, imagem.height, imagem.width * 3, QtGui.QImage.Format_RGB888)
                self.canvas_roadmap.setPixmap(QtGui.QPixmap.fromImage(imagem_qt))

            # Exibe os dados
            self.canvas_roadmap.setText(f"Nome: {nome}\nStatus: {status}\nDescrição: {descricao[:200]}...")

    def mostrar_no_roadmap(self):
        selected_row = self.treeview_especies.currentRow()
        if selected_row != -1:
            nome = self.treeview_especies.item(selected_row, 0).text()
            self.cursor.execute("SELECT nome, status, descricao, imagem FROM especies WHERE nome = ?", (nome,))
            especie = self.cursor.fetchone()
            if especie:
                self.exibir_roadmap([especie])

    def exibir_roadmap_selecionado(self):
        selected_row = self.treeview_especies.currentRow()
        if selected_row != -1:
            nome = self.treeview_especies.item(selected_row, 0).text()
            self.cursor.execute("SELECT nome, status, descricao, imagem FROM especies WHERE nome = ?", (nome,))
            especie = self.cursor.fetchone()
            if especie:
                self.exibir_roadmap([especie])
            else:
                QtWidgets.QMessageBox.critical(self, "Erro", "Nenhuma espécie selecionada!")
        else:
            QtWidgets.QMessageBox.critical(self, "Erro", "Selecione uma espécie para exibir o roadmap!")

    def limpar_treeview(self):
        self.treeview_especies.clear()

    def listar_especies(self):
        """Carrega as espécies do banco de dados e exibe na Treeview."""
        self.cursor.execute("SELECT nome, descricao, status FROM especies")
        self.treeview_especies.setRowCount(0)
        for especie in self.cursor.fetchall():
            row_position = self.treeview_especies.rowCount()
            self.treeview_especies.insertRow(row_position)
            self.treeview_especies.setItem(row_position, 0, QtWidgets.QTableWidgetItem(especie[0]))
            self.treeview_especies.setItem(row_position, 1, QtWidgets.QTableWidgetItem(especie[1]))
            self.treeview_especies.setItem(row_position, 2, QtWidgets.QTableWidgetItem(especie[2]))

    def limpar_campos(self):
        self.entry_nome.clear()
        self.combobox_status.setCurrentIndex(0)
        self.text_descricao.clear()
        self.canvas_imagem.clear()
        self.caminho_imagem = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CatalogoEspecies()
    sys.exit(app.exec_())
