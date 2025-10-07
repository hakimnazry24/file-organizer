import os

DIRECTORY = r"C:\Users\hakim\Downloads"
FILE_EXTENSION = ["jpg", "jpeg", "pdf"]

def main():
    print("Specified extension:", FILE_EXTENSION)
    print("Organizing files in directory:", DIRECTORY)

    files = [f for f in os.listdir(DIRECTORY) 
             if os.path.isfile(os.path.join(DIRECTORY, f)) and os.path.splitext(f)[1].replace(".", "") in FILE_EXTENSION]

    total_files = len(files)
    if total_files == 0:
        print("No files found! Terminate!")
        return
    else:
        print(f"{total_files} files found!")

    for ext in FILE_EXTENSION:
        folder_path = os.path.join(DIRECTORY, ext)
        if not os.path.exists(folder_path):
            print(f"Creating folder for {ext} files..")
            os.makedirs(folder_path)
        else:
            print(f"{ext} folder already exists!")

    for file in files:
        print(f"Moving file {file}")
        file_ext = os.path.splitext(file)[1].replace(".", "")
        folder_to_move = os.path.join(DIRECTORY, file_ext)
        file_current_path = os.path.join(DIRECTORY, file)
        file_new_path = os.path.join(folder_to_move, file)
        os.rename(file_current_path, file_new_path)

    print("Finish!")

if __name__ == "__main__":
    main()
