import os
import tkinter as tk
from tkinter import filedialog
from zipfile import ZipFile
from rarfile import RarFile
from py7zr import SevenZipFile

def extract_and_save(archive_ref, archive_file):
    archive_dir = os.path.splitext(os.path.basename(archive_file))[0]
    output_folder = os.path.join(os.path.dirname(archive_file), archive_dir)

    try:
        os.makedirs(output_folder, exist_ok=True)
        archive_ref.extractall(output_folder)
        print(f"Extraction completed successfully for {archive_file}.")
    except FileNotFoundError:
        print(f"Error: {archive_file} not found.")
    except Exception as e:
        print(f"Error extracting {archive_file}: {e}")

def open_file_picker():
    initial_dir = os.getcwd()  # Set the initial directory to the current working directory

    try:
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        file_paths = filedialog.askopenfilenames(
            title="Select Archive Files",
            filetypes=[("ZIP files", "*.zip"), ("RAR files", "*.rar"), ("7z files", "*.7z")],
            initialdir=initial_dir
        )

        for file_path in file_paths:
            try:
                file_extension = os.path.splitext(file_path)[1].lower()

                if file_extension == '.zip':
                    with ZipFile(file_path, 'r') as zip_ref:
                        extract_and_save(zip_ref, file_path)
                elif file_extension == '.rar':
                    with RarFile(file_path, 'r') as rar_ref:
                        extract_and_save(rar_ref, file_path)
                elif file_extension == '.7z':
                    with SevenZipFile(file_path, 'r') as sevenzip_ref:
                        extract_and_save(sevenzip_ref, file_path)
                else:
                    print(f"Unsupported file format: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    except tk.TclError:
        print("Error: Tkinter GUI not supported on this system.")

    print("\nThank you for using the Mass Zip Extractor!")
    print("This tool can be handy for managing multiple archive files.")
    print("If you've downloaded numerous GitHub projects, this script can help organize them easily.")
    print("Feel free to explore and contribute to the project on GitHub.")
    print("GitHub Repository: https://github.com/CipherNebula42/mass-zip-extractor")
    print(" ")
    print("Check out my webpage for more tools and resources: https://github.com/CipherNebula42/")


# Open file picker and extract files
open_file_picker()
