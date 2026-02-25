# Biblioteca para manipulação de arquivos e diretórios
import os
# Biblioteca para mover arquivos
import shutil

TIPOS_DE_ARQUIVOS = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas" : [".xlsx", ".csv"],
    "Musicas": [".mp3", ".wav"],
    "Videos": [".mp4", "mkv"]
}

def organizar_arquivos(caminho):
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        if os.path.isdir(caminho_completo):
            continue
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        for pasta, extensoes in TIPOS_DE_ARQUIVOS.items():
            if extensao in extensoes:
                pasta_destino = os.path.join(caminho, pasta)
                if not os.path.exists(pasta_destino):
                    os.mkdir(pasta_destino)

                shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))

                print(f"✔ {arquivo} movido para a pasta '{pasta}'")
                break

caminho_usuario = input("Digite o caminho da pasta que deseja organizar: ")

if os.path.exists(caminho_usuario):
    organizar_arquivos(caminho_usuario)
    print("\n✅ Organização concluída com sucesso!")
else:
    print("❌ Caminho inválido! Verifique e tente novamente.")