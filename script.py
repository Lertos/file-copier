import os
import shutil

search_folder_path = r'C:\Users\User123\test1'
output_folder_path = r'C:\Users\User123\test2'

ignore_file_ext = True


#Iterate over the folder to search in and compare against the given file names
def copy_files():
    for filename in os.listdir(search_folder_path):
        current_file = os.path.join(search_folder_path, filename)
        
        #Check if it is a file
        if os.path.isfile(current_file):
            if is_file_to_copy(filename):
                output_file = os.path.join(output_folder_path, filename)
                shutil.copyfile(current_file, output_file)

            
def is_file_to_copy(filename):
    if ignore_file_ext:
        index = filename.index('.')
        raw_filename = filename
        
        if index != -1:
            raw_filename = filename[:index]
        
        if raw_filename in filenames_to_copy:
            return True
    return False
            
            
def check_folder_paths():
    if os.path.exists(search_folder_path) and os.path.exists(output_folder_path):
        return True
    return False


#===============
#Main Script
#===============

filenames_to_copy = [
    'file1',
    'file2',
    'file3'
]

if not check_folder_paths():
    print('One or both of the folder paths does not exist')
else:
    #Sort the list of entries to search as OS walking does it alphabetically
    filenames_to_copy.sort()

    copy_files()
    
