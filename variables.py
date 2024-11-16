# All variables,which main.py use
from pathlib import Path

desktop = Path.home() / "Desktop"
files_list = [file for file in desktop.iterdir() if file.is_file()]
folders_list = [folder for folder in desktop.iterdir() if folder.is_dir()]

documents_folder = desktop / "Documents"
images_folder = desktop / "Images"
remainings_folder = desktop / "Remainings"
folders_folder = desktop / "Folders"
all_desktop_folders = [documents_folder, images_folder, remainings_folder, folders_folder]
existing_document_folders = [documents_folder / "Word", documents_folder / "Excel", documents_folder / "Powerpoint",documents_folder / "Txt"]
existing_folders_list = [documents_folder, documents_folder / "Pdf", documents_folder / "Word", documents_folder / "Excel", documents_folder / "Powerpoint",documents_folder / "Txt", folders_folder, images_folder, desktop / remainings_folder]
