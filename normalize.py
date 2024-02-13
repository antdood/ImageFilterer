from PIL import Image

def normalize(pic):
	#grayscale
	return pic.convert('L')
	


if __name__ == "__main__":
	i = Image.open("img.png")

	t = normalize(i)

	t.save("grey.png")
