import os
import random
import shutil

# Define source directory containing images
source_directory = 'fakepanel2142024'
dest = 'mars/images'

train_directory = os.path.join(dest, 'train_1')
test_directory = os.path.join(dest, 'test_1')
val_directory = os.path.join(dest, 'val_1')

dir_list = [train_directory, test_directory, val_directory]

def move_files():
    # Get list of all files in source directory
    files = os.listdir(source_directory)
    
    # Separate files into two lists: with and without zone identifiers
    without_zone_id = [f for f in files if 'zone' not in f.lower()]
    
    # Shuffle the list of files without zone identifiers
    random.shuffle(without_zone_id)
    
    # Determine number of files for each set
    total_files = len(without_zone_id)
    num_each_set = total_files // 3  # Divide by 3

    # Move files to destination directories
    for i in range(len(dir_list)):
        for j in range(num_each_set):
            if without_zone_id:
                file = without_zone_id.pop(0)
                src_path = os.path.join(source_directory, file)
                dest_path = os.path.join(dir_list[i], file)
                shutil.move(src_path, dest_path)
                print(f"Moved {file} to {dir_list[i]}")

# Move files
move_files()
