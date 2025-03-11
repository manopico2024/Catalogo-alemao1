import sqlite3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import io
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

class CatalogoEspecies:
    def __init__(self, root):
        self.root = root
        # Conexão com o banco de dados
        self.conn = sqlite3.connect("catalogo_especies.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

        # Elementos da interface
        self.label_nome = tk.Label(root, text="Nome da Espécie:")
        self.label_nome.place(x=20, y=65)
        self.entry_nome = tk.Entry(root, width=30)
        self.entry_nome.place(x=150, y=65)

        self.label_status = tk.Label(root, text="Nível de Extinção:")
        self.label_status.place(x=20, y=100)

        self.combobox_status = ttk.Combobox(root, values=["Crítico", "Em Perigo", "Vulnerável", "Pouco Preocupante"],
                                           state="readonly", width=27)
        self.combobox_status.place(x=150, y=100)

        self.button_imagem = tk.Button(root, text="Carregar Imagem", command=self.carregar_imagem)
        self.button_imagem.place(x=428, y=98)

        self.label_descricao = tk.Label(root, text="Descrição:")
        self.label_descricao.place(x=20, y=170)
        self.text_descricao = tk.Text(root, width=60, height=5, highlightbackground="black", highlightthickness=2)
        self.text_descricao.place(x=150, y=170)

        self.button_adicionar = tk.Button(root, text="Adicionar/Salvar Espécie", command=self.adicionar_especie,
                                          bg="#00bfff", font="Arial 10 bold")
        self.button_adicionar.place(x=20, y=280)

        self.button_remover = tk.Button(root, text="Remover Espécie", command=self.remover_especie,
                                        bg="#00bfff", font="Arial 10 bold")
        self.button_remover.place(x=205, y=280)

        self.button_buscar = tk.Button(root, text="Buscar Espécie", command=self.buscar_especie,
                                       bg="#00bfff", font="Arial 10 bold")
        self.button_buscar.place(x=340, y=280)

        self.button_limpar = tk.Button(root, text="Limpar", command=self.limpar_treeview,
                                       bg="#00bfff", font="Arial 10 bold")
        self.button_limpar.place(x=460, y=280)

        # Botão para exibir o roadmap
        self.button_roadmap = tk.Button(root, text="Exibir Roadmap", command=self.exibir_roadmap_selecionado,
                                        bg="#00bfff", font="Arial 10 bold")
        self.button_roadmap.place(x=580, y=280)

        # Treeview para listar espécies
        self.treeview_especies = ttk.Treeview(root, columns=("Nome", "Descrição", "Status"), show="headings", height=15,
                                              padding=(5, 5))
        self.treeview_especies.place(x=20, y=330)
        self.treeview_especies.heading("Nome", text="Nome")
        self.treeview_especies.heading("Descrição", text="Descrição")
        self.treeview_especies.heading("Status", text="Status")
        self.treeview_especies.column("Nome", width=150)
        self.treeview_especies.column("Descrição", width=300)
        self.treeview_especies.column("Status", width=150)

        # Evento de seleção na Treeview
        self.treeview_especies.bind("<<TreeviewSelect>>", self.mostrar_no_roadmap)

        # Exibir imagem
        self.canvas_imagem = tk.Canvas(root, width=100, height=100, bg="white", highlightbackground="black")
        self.canvas_imagem.place(x=535, y=20)

        # Canvas para roadmap
        self.canvas_roadmap = tk.Canvas(root, width=645, height=332, bg="#edece8", highlightbackground="black")
        self.canvas_roadmap.place(x=690, y=330)

        # Inicialização
        self.caminho_imagem = None
        self.imagem_tk = None

        # Preencher a Treeview com as espécies
        self.listar_especies()

        # Inicializar com campos limpos
        self.limpar_campos()

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
        self.caminho_imagem = filedialog.askopenfilename(filetypes=[("Arquivos de Imagem", "*.jpg;*.png;*.jpeg")])
        if self.caminho_imagem:
            imagem = Image.open(self.caminho_imagem)
            imagem = imagem.resize((100, 100))
            self.imagem_tk = ImageTk.PhotoImage(imagem)
            self.canvas_imagem.create_image(52, 52, image=self.imagem_tk)

    def adicionar_especie(self):
        nome = self.entry_nome.get().strip()
        status = self.combobox_status.get().strip()
        descricao = self.text_descricao.get("1.0", tk.END).strip()

        if not nome:
            messagebox.showerror("Erro", "O nome da espécie é obrigatório!")
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
            messagebox.showinfo("Sucesso", "Espécie salva com sucesso!")
            self.listar_especies()
            self.limpar_campos()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Espécie já cadastrada!")

    def remover_especie(self):
        selected_item = self.treeview_especies.selection()
        if not selected_item:
            messagebox.showerror("Erro", "Selecione uma espécie para remover!")
            return

        nome = self.treeview_especies.item(selected_item, "values")[0]
        self.cursor.execute("DELETE FROM especies WHERE nome = ?", (nome,))
        self.conn.commit()
        messagebox.showinfo("Sucesso", "Espécie removida com sucesso!")
        self.listar_especies()

    def buscar_especie(self):
        nome = self.entry_nome.get().strip()
        if not nome:
            messagebox.showerror("Erro", "Digite o nome da espécie para buscar!")
            return

        self.cursor.execute("SELECT nome, status, descricao, imagem FROM especies WHERE nome = ?", (nome,))
        especie = self.cursor.fetchone()

        if especie:
            self.exibir_roadmap([especie])
        else:
            messagebox.showerror("Erro", "Espécie não encontrada!")

    def exibir_roadmap(self, especies):
        self.canvas_roadmap.delete("all")  # Limpa o Canvas
        x, y = 10, 10

        for especie in especies:
            nome, status, descricao, imagem_bytes = especie

            # Exibe a imagem (se houver)
            if imagem_bytes:
                imagem = Image.open(io.BytesIO(imagem_bytes)).resize((90, 90))
                imagem_tk = ImageTk.PhotoImage(imagem)
                self.canvas_roadmap.create_image(x + 55, y + 57, image=imagem_tk)
                self.canvas_roadmap.image = imagem_tk  # Referência para manter no Canvas

            # Exibe os dados
            self.canvas_roadmap.create_text(x + 115, y + 8, anchor="nw", text=f"Nome: {nome}",
                                            font=("Arial", 15))
            self.canvas_roadmap.create_text(x + 115, y + 47, anchor="nw", text=f"Status: {status}", font=("Arial", 15))
            self.canvas_roadmap.create_text(x + 115, y + 83, anchor="nw", text=f"Descrição: {descricao[:200]}...",
                                            font=("Arial", 14))
            y += 120  # Espaçamento entre as espécies

    def mostrar_no_roadmap(self, event):
        selected_item = self.treeview_especies.selection()
        if selected_item:
            nome = self.treeview_especies.item(selected_item, "values")[0]
            self.cursor.execute("SELECT nome, status, descricao, imagem FROM especies WHERE nome = ?", (nome,))
            especie = self.cursor.fetchone()
            if especie:
                self.exibir_roadmap([especie])

    def exibir_roadmap_selecionado(self):
        selected_item = self.treeview_especies.selection()
        if selected_item:
            nome = self.treeview_especies.item(selected_item, "values")[0]
            self.cursor.execute("SELECT nome, status, descricao, imagem FROM especies WHERE nome = ?", (nome,))
            especie = self.cursor.fetchone()
            if especie:
                self.exibir_roadmap([especie])
            else:
                messagebox.showerror("Erro", "Nenhuma espécie selecionada!")
        else:
            messagebox.showerror("Erro", "Selecione uma espécie para exibir o roadmap!")

    def limpar_treeview(self):
        """Remove todos os itens exibidos na Treeview."""
        for item in self.treeview_especies.get_children():
            self.treeview_especies.delete(item)

    def listar_especies(self):
        """Carrega as espécies do banco de dados e exibe na Treeview."""
        self.limpar_treeview()  # Limpa a Treeview
        self.cursor.execute("SELECT nome, descricao, status FROM especies")
        for especie in self.cursor.fetchall():
            self.treeview_especies.insert("", tk.END, values=especie)

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.combobox_status.set("")
        self.text_descricao.delete("1.0", tk.END)
        self.canvas_roadmap.delete("all")
        self.caminho_imagem = None

    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = CatalogoEspecies(root)
    root.title("Catálogo de Espécies")
    root.geometry('1366x780')
    root.resizable(False, False)
    root.config(bg='#5b9c40')
    root.mainloop()