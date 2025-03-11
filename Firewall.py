import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return subprocess.run("net session", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0

def run_as_admin():
    if not is_admin():
        messagebox.showinfo("Permissão necessária", "Reiniciando como administrador...")
        subprocess.run(["powershell", "Start-Process", "python", "-ArgumentList", f"'{__file__}'", "-Verb", "RunAs"], shell=True)
        exit()

def bloquear_programa():
    caminho_programa = filedialog.askopenfilename(title="Selecione o programa para bloquear")
    if caminho_programa:
        regra_nome = os.path.basename(caminho_programa)
        comando = (
            f'netsh advfirewall firewall add rule name="{regra_nome}" '
            f'dir=out action=block program="{caminho_programa}" enable=yes'
        )
        try:
            subprocess.run(comando, shell=True, check=True)
            messagebox.showinfo("Sucesso", f"O programa {regra_nome} foi bloqueado com sucesso.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Erro", "Falha ao bloquear o programa. Execute como administrador.")

# Verifica e eleva permissões
run_as_admin()

# Criando a interface gráfica
root = tk.Tk()
root.title("Bloqueador de Programas no Firewall")
root.geometry("400x200")

tk.Label(root, text="Bloquear programas no Firewall do Windows", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Selecionar Programa e Bloquear", command=bloquear_programa).pack(pady=20)

root.mainloop()
