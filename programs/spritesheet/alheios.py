from PIL import Image, ImageDraw, ImageFont
import os

# Caminho da fonte
CAMINHO_FONTE = "simbolos_alheios.ttf"  # <- coloque o nome exato do arquivo .ttf
TAMANHO_INICIAL = 300
PASTA_SAIDA = "saida"

# Garante que a pasta de saída existe
os.makedirs(PASTA_SAIDA, exist_ok=True)

def gerar_simbolo(texto, caminho_fonte):
    """Gera uma imagem com letras menores dentro da maior letra."""
    img = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    n = len(texto)

    if n == 1:
        # Se tiver apenas 1 letra, centraliza normalmente
        tamanho = 200
        fonte = ImageFont.truetype(caminho_fonte, tamanho)
        w, h = draw.textbbox((0,0), texto[0], font=fonte)[2:]
        draw.text(((400 - w)/2, (400 - h)/2), texto[0], font=fonte, fill=(255,255,255,255))

    elif n == 2:
        # Começa com um tamanho pequeno e aumenta progressivamente
        tamanho = 100  # tamanho inicial da menor letra
        incremento = 40  # quanto aumenta para cada letra

        for letra in texto:
            fonte_tam = ImageFont.truetype(caminho_fonte, tamanho)
            bbox = draw.textbbox((0, 0), letra, font=fonte_tam)
            w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

            # centraliza cada letra
            pos_x = (400 - w) / 2
            pos_y = (400 - h) / 2
            draw.text((pos_x, pos_y), letra, font=fonte_tam, fill=(255, 255, 255, 255))

            tamanho += incremento  # aumenta o tamanho para a próxima letra

    else:
        # 3 ou mais letras: todas menores dentro da maior
        maior = texto[-1]
        menores = texto[:-1]

        # Desenha a maior letra
        tamanho_maior = 200
        fonte = ImageFont.truetype(caminho_fonte, tamanho_maior)
        w, h = draw.textbbox((0,0), maior, font=fonte)[2:]
        draw.text(((400 - w)/2, (400 - h)/2), maior, font=fonte, fill=(255,255,255,255))

        # Desenha as menores lado a lado, centralizadas na maior
        tamanho_menor = 120
        espaco = 10
        total_largura = 0
        bboxes = []
        for letra in menores:
            fonte = ImageFont.truetype(caminho_fonte, tamanho_menor)
            bbox = draw.textbbox((0,0), letra, font=fonte)
            w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
            bboxes.append((w,h))
            total_largura += w
        total_largura += espaco * (len(menores)-1)

        x = (400 - total_largura)/2
        for i, letra in enumerate(menores):
            w, h = bboxes[i]
            y = (400 - h)/2
            fonte = ImageFont.truetype(caminho_fonte, tamanho_menor)
            draw.text((x, y), letra, font=fonte, fill=(255,255,255,255))
            x += w + espaco

    return img

def main():
    texto_usuario = input("Digite os grupos de letras (ex: abc def ghi): ").strip()
    grupos = texto_usuario.split(" ")

    simbolos = [gerar_simbolo(grupo, CAMINHO_FONTE) for grupo in grupos]

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
