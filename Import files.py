import os

def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()
current_path()

os.chdir('/Users/tyrusyuen/Library/CloudStorage/OneDrive-TheChineseUniversityofHongKong/Uni Material Backup')

# assign directory
directory = '/Users/tyrusyuen/Library/CloudStorage/OneDrive-TheChineseUniversityofHongKong/Uni Material Backup/Unprocessed/'

#Create empty list for saving paths of all PDFs in the root folder
folder_list=[]
filename_list=[]
path_list=[]

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename[-4:] == ".pdf":
            folder_list.append(root.partition(directory)[-1]) #((os.path.join(root, filename)))
            filename_list.append(filename.partition(".")[0])
            path_list.append((os.path.join(root, filename)))
print(folder_list)
print(filename_list)
print(path_list)
