from PIL import Image

img = Image.open(r"teste.jpg").convert("RGBA")

img.save(f"img10.png")
