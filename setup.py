import sys
from cx_Freeze import setup, Executable

# Configurar arquivos a serem incluídos (banco de dados, ícones, etc.)
arquivos = ["dados_cadastro.txt", "img/RS.ico", ]  # Adicione arquivos extras aqui

# Configurações para a geração do executável
build_exe_options = {"packages": ["tkinter", "sqlite3", "pyqt5"], "include_files": arquivos}

setup(
    name="CatalogodeEspecies",
    version="1.0",
    description="Aplicação Tkinter com Banco de Dados",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "app.py",
            base="Win32GUI",  # Remove o console (somente Windows)
            icon="RS.ico"  # Ícone do executável
        )
    ]
)
