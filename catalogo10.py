from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pyqtgraph as pg  # Importando PyQtGraph
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout


class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.setGeometry(100, 100, 1366, 780)  # Tornar a janela responsiva
        root.setUnifiedTitleAndToolBarOnMac(False)

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        root.setCentralWidget(self.centralwidget)

        # Layout principal
        self.layout_principal = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout_principal.setContentsMargins(10, 10, 10, 10)
        self.layout_principal.setSpacing(10)

        # Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.layout_principal.addWidget(self.tabWidget)

        # Tab Configurações
        self.tab_configuracoes = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_configuracoes, "Configurações")

        # Layout da Tab Configurações
        self.layout_tab_configuracoes = QtWidgets.QVBoxLayout(self.tab_configuracoes)
        self.layout_tab_configuracoes.setContentsMargins(10, 10, 10, 10)

        # Frame Root
        self.frame_root = QtWidgets.QFrame(self.tab_configuracoes)
        self.frame_root.setObjectName("frame_root")
        self.layout_tab_configuracoes.addWidget(self.frame_root)

        # Layout do Frame Root
        self.layout_frame_root = QtWidgets.QVBoxLayout(self.frame_root)
        self.layout_frame_root.setContentsMargins(10, 10, 10, 10)

        # Label do Logo
        self.lb_logo = QtWidgets.QLabel(self.frame_root)
        self.lb_logo.setPixmap(QtGui.QPixmap("img/Logo.png"))
        self.lb_logo.setScaledContents(True)
        self.layout_frame_root.addWidget(self.lb_logo)

        # Tabela para listar espécies
        self.table = QtWidgets.QTableWidget(self.frame_root)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Id", "Nome", "Descrição", "Status", "Imagem"])
        self.layout_frame_root.addWidget(self.table)

        # Frame do Gráfico
        self.frame_grafico = QtWidgets.QFrame(self.frame_root)
        self.frame_grafico.setStyleSheet("border: 2px solid black;")
        self.layout_frame_root.addWidget(self.frame_grafico)

        # Layout do Frame do Gráfico
        self.layout_frame_grafico = QVBoxLayout(self.frame_grafico)
        self.frame_grafico.setLayout(self.layout_frame_grafico)

        # Canvas do Gráfico usando PyQtGraph
        self.canvas = pg.PlotWidget()  # Usando PyQtGraph
        self.layout_frame_grafico.addWidget(self.canvas)

        # Responsividade
        self.frame_grafico.setMinimumHeight(300)
        self.frame_grafico.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Ajustar layout automaticamente ao redimensionar
        root.resizeEvent = self.resizeEvent

        # Conectar Botões
        self.btn_adicionar = QtWidgets.QPushButton("Cadastrar", self.frame_root)
        self.btn_adicionar.clicked.connect(self.adicionar_especie)
        self.layout_frame_root.addWidget(self.btn_adicionar)

        # Inicializar Banco de Dados
        self.conn = sqlite3.connect('especies.db')
        self.cursor = self.conn.cursor()
        self.criar_tabela()

        # Carregar dados iniciais
        self.listar_especies()

    def resizeEvent(self, event):
        """Garante que o layout se ajuste ao redimensionar a janela."""
        self.tabWidget.setGeometry(10, 10, event.size().width() - 20, event.size().height() - 20)
        # Chama o método para atualizar o gráfico quando a janela for redimensionada
        self.atualizar_grafico()

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
            self.atualizar_grafico()
        except sqlite3.IntegrityError:
            QMessageBox.critical(None, "Erro", "Espécie já cadastrada!")

    def listar_especies(self):
        self.cursor.execute("SELECT id, nome, descricao, status, imagem FROM especies")
        dados = self.cursor.fetchall()
        self.table.setRowCount(len(dados))
        for row_index, row_data in enumerate(dados):
            for col_index, cell_data in enumerate(row_data):
                if col_index == 4:
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

    def atualizar_grafico(self):
        """Atualiza o gráfico com dados do banco de dados."""
        self.canvas.clear()  # Limpar o gráfico anterior

        # Exemplo de dados para o gráfico
        especies = ['Espécie 1', 'Espécie 2', 'Espécie 3']
        quantidade = [10, 20, 15]

        self.canvas.plot(especies, quantidade, pen='r')  # Plotar no gráfico

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
