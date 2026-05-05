import os
import shutil
from datetime import datetime

# Configuração de caminhos
SOURCE_DIR = os.path.expanduser("~/Downloads")  # Pasta de origem
DEST_DIRS = {
    "Documentos": [".pdf", ".docx", ".txt"],
    "Scripts_e_Codigo": [".py", ".java", ".sh", ".sql"],
    "Relatorios_Monitoramento": [".csv", ".xlsx", ".log"],
    "Imagens": [".jpg", ".jpeg", ".png"]
}

def organize_files():
    print(f"[{datetime.now()}] Iniciando automação de limpeza...")
    
    # Cria pastas de destino se não existirem
    for folder in DEST_DIRS.keys():
        path = os.path.join(SOURCE_DIR, folder)
        if not os.path.exists(path):
            os.makedirs(path)

    # Varre os arquivos na pasta de origem
    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)
        
        # Ignora se for uma pasta
        if os.path.isdir(file_path):
            continue
            
        file_ext = os.path.splitext(filename)[1].lower()

        # Move o arquivo baseado na extensão
        for folder, extensions in DEST_DIRS.items():
            if file_ext in extensions:
                dest_path = os.path.join(SOURCE_DIR, folder, filename)
                shutil.move(file_path, dest_path)
                print(f"✓ Movido: {filename} -> {folder}")
                break

if __name__ == "__main__":
    organize_files()
    print("✨ Organização concluída com sucesso!")