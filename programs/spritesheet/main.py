import os
from PIL import Image

def create_stylesheet(input_folder, output_path, rows, cols):
    
    image_files = sorted([
        f for f in os.listdir(input_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])

    if not image_files:
        print("Nenhuma imagem encontrada na pasta.")
        return

    if len(image_files) > rows * cols:
        print(f"Atenção: mais imagens ({len(image_files)}) do que espaço no grid ({rows * cols}). As extras serão ignoradas.")

    
    first_image = Image.open(os.path.join(input_folder, image_files[0]))
    width, height = first_image.size

    
    sprite_sheet = Image.new('RGBA', (cols * width, rows * height), (0, 0, 0, 0))

    
    for index, filename in enumerate(image_files[:rows * cols]):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGBA")

        
        if img.size != (width, height):
            img = img.resize((width, height))

        row = index // cols
        col = index % cols

        sprite_sheet.paste(img, (col * width, row * height))

    
    sprite_sheet.save(output_path)
    print(f"Spritesheet salva em: {output_path}")


if __name__ == "__main__":
    pasta_imagens = "imagens"       
    arquivo_saida = "spritesheet.png"
    linhas = int(input('número de linhas: '))                    
    colunas = int(input('número de colunas: '))                   

    create_stylesheet(pasta_imagens, arquivo_saida, linhas, colunas)
