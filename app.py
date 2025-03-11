import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
                             QComboBox, QTextEdit, QFileDialog, QMessageBox, QTableWidget,
                             QTableWidgetItem, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import QByteArray
from PIL import ImageQt
import io


class CatalogoEspecies(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catálogo de Espécies")
        self.setGeometry(100, 100, 1366, 780)
        self.setStyleSheet("background-color: #f7fcf9;")

        self.conn = sqlite3.connect("catalogo_especies.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

        self.initUI()
        self.listar_especies()

    def initUI(self):
        self.label_nome = QLabel("Nome da Espécie:", self)
        self.label_nome.move(20, 65)
        self.entry_nome = QLineEdit(self)
        self.entry_nome.setGeometry(150, 65, 250, 25)

        self.label_status = QLabel("Nível de Extinção:", self)
        self.label_status.move(20, 100)
        self.combobox_status = QComboBox(self)
        self.combobox_status.addItems(["Crítico", "Em Perigo", "Vulnerável", "Pouco Preocupante"])
        self.combobox_status.setGeometry(150, 100, 250, 25)

        self.button_imagem = QPushButton("Carregar Imagem", self)
        self.button_imagem.setGeometry(420, 100, 150, 25)
        self.button_imagem.clicked.connect(self.carregar_imagem)

        self.label_descricao = QLabel("Descrição:", self)
        self.label_descricao.move(20, 140)
        self.text_descricao = QTextEdit(self)
        self.text_descricao.setGeometry(150, 140, 420, 100)

        self.button_adicionar = QPushButton("Adicionar/Salvar Espécie", self)
        self.button_adicionar.setGeometry(20, 280, 180, 40)
        self.button_adicionar.clicked.connect(self.adicionar_especie)

        self.button_remover = QPushButton("Remover Espécie", self)
        self.button_remover.setGeometry(220, 280, 180, 40)
        self.button_remover.clicked.connect(self.remover_especie)

        self.button_buscar = QPushButton("Buscar Espécie", self)
        self.button_buscar.setGeometry(420, 280, 150, 40)
        self.button_buscar.clicked.connect(self.buscar_especie)

        self.table_especies = QTableWidget(self)
        self.table_especies.setGeometry(20, 340, 600, 400)
        self.table_especies.setColumnCount(3)
        self.table_especies.setHorizontalHeaderLabels(["Nome", "Descrição", "Status"])
        self.table_especies.setSelectionBehavior(QTableWidget.SelectRows)

        self.image_view = QGraphicsView(self)
        self.image_view.setGeometry(580, 20, 150, 150)
        self.scene = QGraphicsScene()
        self.image_view.setScene(self.scene)

        self.caminho_imagem = None

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

    def buscar_especie(self):
        nome = self.entry_nome.text().strip()
        if not nome:
            QMessageBox.critical(self, "Erro", "Digite o nome da espécie para buscar!")
            return

        self.cursor.execute("SELECT nome, status, descricao, imagem FROM especies WHERE nome = ?", (nome,))
        especie = self.cursor.fetchone()

        if especie:
            nome, status, descricao, imagem_bytes = especie
            QMessageBox.information(self, "Espécie Encontrada",
                                    f"Nome: {nome}\nStatus: {status}\nDescrição: {descricao}")
            if imagem_bytes:
                imagem = ImageQt.ImageQt(io.BytesIO(imagem_bytes))
                pixmap = QPixmap.fromImage(imagem)
                self.scene.clear()
                self.scene.addPixmap(pixmap)
        else:
            QMessageBox.critical(self, "Erro", "Espécie não encontrada!")

    def carregar_imagem(self):
        options = QFileDialog.Options()
        self.caminho_imagem, _ = QFileDialog.getOpenFileName(self, "Carregar Imagem", "",
                                                             "Imagens (*.png *.jpg *.jpeg)", options=options)
        if self.caminho_imagem:
            pixmap = QPixmap(self.caminho_imagem).scaled(150, 150)
            self.scene.clear()
            self.scene.addPixmap(pixmap)

    def adicionar_especie(self):
        nome = self.entry_nome.text().strip()
        status = self.combobox_status.currentText()
        descricao = self.text_descricao.toPlainText().strip()

        if not nome:
            QMessageBox.critical(self, "Erro", "O nome da espécie é obrigatório!")
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
            QMessageBox.information(self, "Sucesso", "Espécie salva com sucesso!")
            self.listar_especies()
        except sqlite3.IntegrityError:
            QMessageBox.critical(self, "Erro", "Espécie já cadastrada!")

    def remover_especie(self):
        row = self.table_especies.currentRow()
        if row == -1:
            QMessageBox.critical(self, "Erro", "Selecione uma espécie para remover!")
            return

        nome = self.table_especies.item(row, 0).text()
        self.cursor.execute("DELETE FROM especies WHERE nome = ?", (nome,))
        self.conn.commit()
        self.listar_especies()
        QMessageBox.information(self, "Sucesso", "Espécie removida com sucesso!")

    def listar_especies(self):
        self.table_especies.setRowCount(0)
        self.cursor.execute("SELECT nome, descricao, status FROM especies")
        for row, especie in enumerate(self.cursor.fetchall()):
            self.table_especies.insertRow(row)
            for col, data in enumerate(especie):
                self.table_especies.setItem(row, col, QTableWidgetItem(str(data)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CatalogoEspecies()
    window.show()
    sys.exit(app.exec_())
