import os
import time

msg_box = ''' THIS PROGRAM IS USED FOR CREATE
 MODIFY AND REMOVING FILES ON THE COMPUTER
 INCLUDING A BACKUP !\n CREATED By Reds009'''
print(msg_box)

# directory and file settings
current_dicrectory = os.getcwd()

print(f"you're current directory is '{current_dicrectory}'")

# defining a function that will create files
def create_file():
    # creating a function that will check if the files submitted already exist
        def check_if_file_exist():
            #file_check = os.path.exists(file) # i was checking for the if the file directory exist that why I was getting the result True
            file_check = os.path.isfile(file)  # I think this os built-in method is doing the same as the one above it
            print(f"Status: {file_check}")
            if file_check == current_dicrectory:
                print("[*] Removing The Existing File")
                os.remove(file)
                return True
            else:
                print(f"File Check:     {file_check}")
                print("[*] Creating The New File")
                time.sleep(2)
                return False

        def file_extention():
            filename, extension = os.path.splitext(file)
            if extension:
                print(f"[*] File's extension is '{extension}'")
            else:
                print("[*] File has no extension")


        with open(file, 'w') as f:
            print("[*] File Creation In Progress...")
            time.sleep(2)
            f.write(thoughts)
            # closing the file to release system resources
            f.close()


def d_file():
    if os.path.isfile(file):
        print("[*] Deleting The Desired File...")
        time.sleep(2)
        os.remove(file)
        print(f"[*] File '{file}' successfully deleted!")
    else:
        print(f"[*] File '{file}' does not exist. Nothing to delete.")

while True:
    file = input("ENTER THE FILE'S NAME (or type 'exit' to quit):  ")
    file_directory = os.path.join(current_dicrectory, file)
    if file == 'exit' or file == 'quit':
        print("[*] Exiting The Program")
        time.sleep(3)
        print("[*] Thanks For Using This Program!")
        break


    print("Options:")
    print("1. Type 'create' or '1' To Create The file")
    print("2. Type 'delete' or '2' To Delete The file")
    print("3. Type 'exit' or '3' to quit the program")

    choice = input("Enter your choice: ").strip().lower()

    if choice == 'exit' or choice == '3':
        print("Thank you for using the File Handler. Goodbye!")
        break
    elif choice == '1' or choice == 'create':
        thoughts = input("WRITE WHATEVER YOU WANT HERE ==>  ")
        print("[*] Creating In Progress...")
        time.sleep(3)
        create_file()
    elif choice == '2' or choice == 'delete':
        print("[*] Deleting The File")
        time.sleep(3)
        d_file()
    else:
        print("Invalid option. Please try again.\n")



