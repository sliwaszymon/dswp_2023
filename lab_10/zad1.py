import os

def create_folders(path_list):
    for path in path_list:
        folders = path.split('/')
        folders = [folder for folder in folders if folder.strip()]
        current_path = ''
        for folder in folders:
            current_path = os.path.join(current_path, folder)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
                print(f"Created folder: {current_path}")

        print("Folder creation completed.")

create_folders(['path/to/folder', 'path/to/other/folder', 'path/to/super/folder'])

# mkdirs version
# def create_folders(path_list):
#     for path in path_list:
#         if not os.path.exists(path):
#             os.makedirs(path)
#             print(f"Created folder: {path}")

#         print("Folder creation completed.")