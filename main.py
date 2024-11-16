from variables import  *

# The sub-function that moves files that don't have specific extension
def sort_remainings(file):
    name = file.name
    file.rename(desktop / "Remainings" / name)

# The sub-function that moves various document files into the folder
def sort_documents(file):
    extension = file.suffix
    name = file.name
    if extension == '.txt':
        file.rename(documents_folder / "Txt" / name)
    elif extension == '.docx' or extension == '.doc':
        file.rename(documents_folder / "Word" / name)
    elif extension == '.pptx' or extension == '.ppt':
        file.rename(documents_folder / "Powerpoint" / name)
    elif extension == '.pdf':
        file.rename(documents_folder / "Pdf" / name)
    else:
        file.rename(documents_folder / "Excel" / name)

# Sorts folders from desktop to the folder
def sort_folders(folder):
    name = folder.name
    if folder in existing_folders_list:
        pass
    else:
        try:
            folder.rename(folders_folder / name)
        except Exception as x:
            print("The directory already have folder with this name,try to rename the folder --> " + str(folder))

# The sub-function that moves various document files(Images) into the folder
def sort_images(file):
    name = file.name
    file.rename(desktop / "Images" / name)

# The function that check extensions and then allocates files in sub-functions
def main_files_sorter(file):
    extension = file.suffix

    if (extension == '.txt' or extension == '.docx' or extension == '.doc' or
            extension == '.pptx' or extension == '.ppt' or extension == '.xlsx' or extension == '.xls' or extension == '.pdf'):
        sort_documents(file)
    elif extension == '.jpeg' or extension == '.jpg' or extension == '.png' or extension == '.gif' or extension == '.webp' or extension == '.svg':
        sort_images(file)
    else:
        sort_remainings(file)

# Main sorter,which firstly sort files in files_sorter than folders
def main_sorter():
    for file in files_list:
        main_files_sorter(file)
    for folder in folders_list:
        sort_folders(folder)

# Check if the folders in which we want to sort the files exist
def check_existing_folders():
    for folder in existing_folders_list:
        if folder.exists():
            pass
        else:
            folder.mkdir()

# Check if the path to the Desktop exists
def check_existing_of_desktop():
    if desktop.exists():
        pass
    else:
        print("Program can't find path for your desktop,if you're using onedrive,that can be a problem")
        return 0

def main():
    if check_existing_of_desktop()==0:
        return 0
    check_existing_folders()
    main_sorter()

if __name__ == '__main__':
    main()

