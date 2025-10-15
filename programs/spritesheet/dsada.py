from PIL import Image, ImageDraw, ImageFont
import random
import os

# Caminho da fonte
FONTE_CAMINHO = "simbolos_alheios.ttf"  # <- coloque o nome exato do seu arquivo .ttf
TAMANHO_INICIAL = 300
PASTA_SAIDA = "saida"

# Garante que a pasta de saída existe
os.makedirs(PASTA_SAIDA, exist_ok=True)

def gerar_simbolo(texto, fonte):
    """Gera uma imagem com os símbolos sobrepostos conforme as letras digitadas."""
    img = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Aumenta ou reduz tamanho da fonte pra caber
    tamanho = TAMANHO_INICIAL
    while tamanho > 10:
        fonte_tam = ImageFont.truetype(fonte, tamanho)
        bbox = draw.textbbox((0, 0), texto[0], font=fonte_tam)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        if w < 380 and h < 380:
            break
        tamanho -= 5

    # Centraliza
    for i, letra in enumerate(texto):
        bbox = draw.textbbox((0, 0), letra, font=fonte_tam)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((400 - w) / 2, (400 - h) / 2), letra, font=fonte_tam, fill=(255, 255, 255, 255))

    return img

def main():
    texto_usuario = input("Digite os grupos de letras (ex: abc def ghi): ").strip()
    grupos = texto_usuario.split(" ")

    simbolos = [gerar_simbolo(grupo, FONTE_CAMINHO) for grupo in grupos]

    # Junta todas as imagens lado a lado
    largura_total = len(simbolos) * 420
    img_final = Image.new("RGBA", (largura_total, 420), (0, 0, 0, 0))

    for i, simb in enumerate(simbolos):
        img_final.paste(simb, (i * 420, 0), simb)

    caminho_saida = os.path.join(PASTA_SAIDA, "simbolos_alheios.png")
    img_final.save(caminho_saida)
    print(f"✅ Imagem gerada em: {caminho_saida}")

if __name__ == "__main__":
    main()
