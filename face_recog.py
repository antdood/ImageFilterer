import face_recognition
from PIL import Image

def locate_faces(target_image):
	image = face_recognition.load_image_file(target_image)
	face_locations = face_recognition.face_locations(image)

	return face_locations

def crop_faces_and_resize(target_image, face_locations, resize_dimensions):
	image = Image.open(target_image)

	for face_location in face_locations:
		crop_location = face_location_to_crop_location(face_location)
		cropped_image = image.crop(crop_location)
		resized_image = resize_image(cropped_image, resize_dimensions)
		
		yield resized_image

def resize_image(target_image, target_dimensions):
	target_image.thumbnail(target_dimensions)

	return target_image

def face_location_to_crop_location(face_location):
	crop_location = (face_location[3],
					 face_location[0],
					 face_location[1],
					 face_location[2])

	return crop_location

if __name__ == "__main__":
	image = "test.png"

	face_locations = locate_faces(image)
	crop_faces(image, face_locations, (32, 32))