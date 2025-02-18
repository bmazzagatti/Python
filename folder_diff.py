#!/usr/bin/env python3

""""
this script finds a diff between folders/files
"""

import os
import filecmp

def get_files(folder):
    """Returns a set of file names in the given folder."""
    return set(os.listdir(folder))

def compare_folders(folder1, folder2):
    """Compares files in two folders and reports differences."""
    
    files1 = get_files(folder1)
    files2 = get_files(folder2)

    # Files that are only in one of the folders
    only_in_folder1 = files1 - files2
    only_in_folder2 = files2 - files1

    # Files present in both folders
    common_files = files1 & files2

    # Files that have the same name but different content
    different_files = []
    for file in common_files:
        file1_path = os.path.join(folder1, file)
        file2_path = os.path.join(folder2, file)
        if os.path.isfile(file1_path) and os.path.isfile(file2_path):  # Ensure it's a file
            if not filecmp.cmp(file1_path, file2_path, shallow=False):  # Compare contents
                different_files.append(file)

    # Print results
    print("\nFiles only in", folder1, ":", only_in_folder1)
    print("Files only in", folder2, ":", only_in_folder2)
    print("Files with the same name but different content:", different_files)

if __name__ == "__main__":
    folder1 = input("Enter the path of the first folder: ").strip()
    folder2 = input("Enter the path of the second folder: ").strip()
    
    if os.path.isdir(folder1) and os.path.isdir(folder2):
        compare_folders(folder1, folder2)
    else:
        print("One or both of the paths are not valid directories.")
