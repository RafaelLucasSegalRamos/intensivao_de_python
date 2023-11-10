from PIL import Image, ImageDraw, ImageFont

coord_1 = (50, 40)
coord_2 = (100, 80)
coord_3 = (150, 120)
coord_4_2 = (200, 800)
coord_2_4 = (100, 160)
cood_9_1 = (450, 40)

img = Image.open(r"teste.jpg")
img2 = Image.new("RGB", (1000, 800), "white")
caminho_fonte = r"C:\Windows\Fonts\comic.ttf"
font = ImageFont.truetype(caminho_fonte, 30)
rgb_black = (0, 0, 0)
rgb2 = (int(input("Digite o valor de RED: ")), int(input("Digite o valor de GREEN: ")), int(input("Digite o valor de BLUE: ")))
desenho1 = ImageDraw.Draw(img)
desenho2 = ImageDraw.Draw(img2)

desenho1.text(coord_1, "(100, 100)", font=font, fill=rgb_black)
desenho2.text(coord_2, "(200, 200)", font=font, fill=rgb2)
desenho1.text(coord_3, "(300, 300)", font=font, fill=rgb_black)
desenho2.text(coord_4_2, "(400, 200)", font=font, fill=rgb2)
desenho1.text(coord_2_4, "(200, 400)", font=font, fill=rgb_black)
desenho2.text(cood_9_1, "(900, 100)", font=font, fill=rgb2)

img.save(f"img1.jpg")
img.show()
img2.save(f"img2.jpg")
img2.show()
