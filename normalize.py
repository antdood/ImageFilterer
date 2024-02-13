from PIL import Image

def normalize(pic):
	#grayscale
	return pic.convert('LA')
	


if __name__ == "__main__":
	i = Image.open("img.png")

	t = normalize(i)

	t.save("grey.png")
