import PySimpleGUI as sg
import os
import io
from PIL import Image
from pathlib import Path

DISPLAY_SIZE = (300,300)

def get_image_paths(path):
	for image in os.listdir(path):
		yield f"{path}/{image}"

variables_layout = [
    [sg.FolderBrowse('Source Folder'), sg.Input()],
    [sg.FolderBrowse('Target Folder'), sg.Input()],
    [sg.Button('Confirm')] 
]

window = sg.Window('Window Title', variables_layout)

event, values = window.read()

source_folder = values['Source Folder']
target_folder = values['Target Folder']
true_folder = Path(target_folder) / "True"
false_folder = Path(target_folder) / "False"
true_folder.mkdir(parents=True, exist_ok=True)
false_folder.mkdir(parents=True, exist_ok=True)

window.close()

images = get_image_paths(source_folder)
current_image_path = ""

def load_next_picture():
	global current_image_path
	current_image_path = next(images)
	current_image = Image.open(current_image_path).resize(DISPLAY_SIZE)
	bio = io.BytesIO()
	current_image.save(bio, format="PNG")
	window["-IMAGE-"].update(data=bio.getvalue())

labeller_layout = [
	[sg.Button("True")],
	[sg.Button("False")],
	[sg.Button("Skip")],
	[sg.Image(key="-IMAGE-")],
]

window = sg.Window("Labeller", labeller_layout, finalize=True, return_keyboard_events=True)
load_next_picture()

while True:
	event, values = window.read()
	if event == "Exit" or event == sg.WIN_CLOSED:
		break
	if event == "True" or event == "1":
		target_path = true_folder / Path(current_image_path).name
		os.rename(current_image_path, target_path)
		load_next_picture()
	if event == "False" or event == "2":
		target_path = false_folder / Path(current_image_path).name
		os.rename(current_image_path, target_path)
		load_next_picture()
	if event == "Skip" or event == "3":
		load_next_picture()

window.close()