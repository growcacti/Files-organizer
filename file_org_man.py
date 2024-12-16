import os
import time
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

def create_dir(base_dir, dn):
    for i in range(dn):
        os.mkdir(os.path.join(base_dir, f"{i}Folder"))

def create_file(base_dir, fn):
    for i in range(fn):
        with open(os.path.join(base_dir, f"{i}File.txt"), 'w') as f:
            pass

def file_counter(base_dir, output_text):
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(base_dir):
        output_text.insert(tk.END, f"Looking in: {root}\n")
        dir_count += len(dirs)
        file_count += len(files)

    output_text.insert(tk.END, f"Number of files: {file_count}\n")
    output_text.insert(tk.END, f"Number of directories: {dir_count}\n")
    output_text.insert(tk.END, f"Total: {file_count + dir_count}\n")

def search_file(base_dir, search_str, output_text):
    found = False
    for root, dirs, files in os.walk(base_dir):
        output_text.insert(tk.END, f"Looking in: {root}\n")
        for file in files:
            if search_str in file:
                output_text.insert(tk.END, f"{search_str} found in {root}\n")
                found = True
                break
    if not found:
        output_text.insert(tk.END, f"{search_str} not found.\n")

def organize_files(output_text):
    directories = {
        "HTML": [".html5", ".html", ".htm", ".xhtml"],
        "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png"],
        # Add other categories as needed...
    }
    file_formats = {ext: category for category, extensions in directories.items() for ext in extensions}

    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in file_formats:
            dir_path = Path(file_formats[file_format])
            dir_path.mkdir(exist_ok=True)
            file_path.rename(dir_path.joinpath(file_path))
    output_text.insert(tk.END, "Files organized successfully.\n")

def handle_action(action, base_dir, param, output_text):
    try:
        if action == "Create Directories":
            create_dir(base_dir, int(param))
        elif action == "Create Files":
            create_file(base_dir, int(param))
        elif action == "Organize Files":
            organize_files(output_text)
        elif action == "Count Files/Directories":
            file_counter(base_dir, output_text)
        elif action == "Search File":
            search_file(base_dir, param, output_text)
        messagebox.showinfo("Success", f"Action '{action}' completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
def main():
    root = tk.Tk()
    root.title("File Manager")
    
    # Labels
    ttk.Label(root, text="Base Directory:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    ttk.Label(root, text="Parameter:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    
    # Entries
    base_dir_entry = ttk.Entry(root, width=50)
    base_dir_entry.grid(row=0, column=1, padx=5, pady=5)
    param_entry = ttk.Entry(root, width=50)
    param_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Text Output
    output_text = tk.Text(root, height=15, width=70)
    output_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
    
    # Buttons
    actions = ["Create Directories", "Create Files", "Organize Files", "Count Files/Directories", "Search File"]
    for i, action in enumerate(actions):
        ttk.Button(root, text=action, command=lambda a=action: handle_action(
            a, base_dir_entry.get(), param_entry.get(), output_text)).grid(row=2, column=i, padx=5, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    main()
