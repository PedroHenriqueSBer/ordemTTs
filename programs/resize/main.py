from PIL import Image
import os

input_folder = "imagens_originais"
output_folder = "imagens_redimensionadas"
new_size = (678, 781)

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".webp")):
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path).convert("RGBA")

        img.thumbnail(new_size, Image.Resampling.LANCZOS)

        new_img = Image.new("RGBA", new_size, (0, 0, 0, 0))

        offset_x = (new_size[0] - img.width) // 2
        offset_y = (new_size[1] - img.height) // 2
        new_img.paste(img, (offset_x, offset_y), img)

        output_path = os.path.join(output_folder, filename)
        new_img.save(output_path)

        print(f"Redimensionada: {filename}")