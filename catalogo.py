import sys
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QMessageBox, QVBoxLayout, QWidget, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib

matplotlib.use("QtAgg")


class GraficoCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        super().__init__(self.fig)
        self.atualizar_grafico()

    def atualizar_grafico(self):
        self.ax.clear()
        conn = sqlite3.connect("catalogo_especies.db")
        cursor = conn.cursor()
        cursor.execute("SELECT strftime('%Y-%m-%d', date('now')), COUNT(*) FROM especies GROUP BY 1")
        dados = cursor.fetchall()
        conn.close()

        if dados:
            datas, quantidades = zip(*dados)
            self.ax.bar(datas, quantidades, color='blue')
            self.ax.set_title("Espécies Catalogadas por Dia")
            self.ax.set_xlabel("Data")
            self.ax.set_ylabel("Quantidade")
            self.ax.set_xticklabels(datas, rotation=45)
        else:
            self.ax.text(0.5, 0.5, "Nenhuma espécie cadastrada", ha='center', va='center', transform=self.ax.transAxes)
        self.draw()


class Ui_root(object):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("catalogo_especies.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def setupUi(self, root):
        root.setObjectName("root")
        root.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")

        layout = QVBoxLayout(self.centralwidget)
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Nome", "Descrição", "Status"])
        layout.addWidget(self.table)

        self.button_adicionar = QtWidgets.QPushButton("Cadastrar")
        self.button_adicionar.clicked.connect(self.adicionar_especie)
        layout.addWidget(self.button_adicionar)

        self.frame_grafico = QFrame(self.centralwidget)
        self.frame_grafico.setFrameShape(QFrame.Box)
        self.frame_grafico.setFrameShadow(QFrame.Raised)
        self.frame_grafico.setStyleSheet("border: 2px solid black;")
        layout.addWidget(self.frame_grafico)

        frame_layout = QVBoxLayout(self.frame_grafico)
        self.canvas = GraficoCanvas(self.frame_grafico)
        frame_layout.addWidget(self.canvas)

        root.setCentralWidget(self.centralwidget)
        self.listar_especies()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS especies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE NOT NULL,
                status TEXT,
                descricao TEXT,
                data TEXT DEFAULT (date('now'))
            )
        """)
        self.conn.commit()

    def adicionar_especie(self):
        nome = "Nova Espécie"
        status = "Pouco preocupante"
        descricao = "Descrição exemplo"
        try:
            self.cursor.execute("""
                INSERT INTO especies (nome, status, descricao)
                VALUES (?, ?, ?)
            """, (nome, status, descricao))
            self.conn.commit()
            self.listar_especies()
            self.canvas.atualizar_grafico()
        except sqlite3.IntegrityError:
            QMessageBox.critical(None, "Erro", "Espécie já cadastrada!")

    def listar_especies(self):
        self.cursor.execute("SELECT nome, descricao, status FROM especies")
        especies = self.cursor.fetchall()
        self.table.setRowCount(len(especies))
        for i, (nome, descricao, status) in enumerate(especies):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(nome))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(descricao))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(status))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
