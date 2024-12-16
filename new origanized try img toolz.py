from tkinter import Tk
from tkinter import Button, filedialog, Frame, Listbox
from PIL import Image, ImageTk
import os
import shutil
from tkinter import Frame, ttk

from image_toolz.image_tab import ImageTab
from image_toolz.image_viewer import ImageViewer
from image_toolz.thumbnail_tool import ImageThumbnailTool
class ImageTab:
    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

    def add_tab(self, title):
        frame = Frame(self.notebook)
        self.notebook.add(frame, text=title)
        return frame

from tkinter import Label, messagebox
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, parent, img_path=None):
        self.parent = parent
        self.img_path = img_path or "/path/to/default/image.jpg"
        self.image_label = Label(self.parent)
        self.image_label.pack(expand=True, fill="both")

        self.display_image()

    def display_image(self):
        try:
            img = Image.open(self.img_path)
            img.thumbnail((800, 600))
            tk_img = ImageTk.PhotoImage(img)
            self.image_label.config(image=tk_img)
            self.image_label.image = tk_img
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image: {e}")




class ImageTToolz:
      def __init__(self, tab, frm,json_file):
          
        self.image_paths = []
        self.selected_images = []
        
        self.frm2 = frm
        self.json_file = json_file
        self.path_var = StringVar()
        self.tab = tab
        self.bookmarks = self.load_bookmarks()
        self.image_paths = []
        self.selected_images = []
        self.merged_image = None
        self.current_img_index = -1  # Initialize to -1 to indicate no image selected yet
        self.setup_gui()
        self.frm = tab.canvaslevel(self.self.frm2)
        self.frm.title("Selected Files")
        self.frm.geometry("400x300")

        self.listbox = Listbox(self.frm, width=50, height=15)
        self.listbox.grid(row=1,column=1)
        self.remove_btn = Button(self.frm,bd=7,bg="orchid", text="Remove Selected", command=lambda: self.remove_selected(self.listbox))
        self.remove_btn.grid(row=2,column=2)

        self.close_btn = Button(self.frm,bd=7,bg="bisque", text="Close", command=self.frm.destroy)
        self.close_btn.grid(row=2,column=3)
        self.x = 180
        self.y = 180


        self.listbox = Listbox(self.parent, width=40, height=15)
        self.listbox.pack(side="left")

        Button(self.parent, text="Browse", command=self.browse_folder).pack()
        Button(self.parent, text="Copy Images", command=self.copy_images).pack()

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.image_paths = self.load_images(folder)
            self.display_thumbnails()

    def load_images(self, directory):
        supported_formats = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif')
        image_paths = []
        for fmt in supported_formats:
            image_paths.extend(glob(os.path.join(directory, fmt)))
        return image_paths

    def display_thumbnails(self):
        for img_path in self.image_paths:
            img = Image.open(img_path)
            img.thumbnail((128, 128))
            tk_img = ImageTk.PhotoImage(img)
            self.listbox.insert("end", os.path.basename(img_path))

    def copy_images(self):
        destination = filedialog.askdirectory()
        if not destination:
            return

        for img_path in self.selected_images:
            shutil.copy(img_path, destination)




  


    def copy_selected_images(self):
        """Copy selected images to another directory."""
        if not self.selected_images:
            messagebox.showwarning("No Selection", "No images selected to copy.")
            return

        destination = filedialog.askdirectory(title="Select Destination Directory")
        if not destination:
            return  # User cancelled the operation

        try:
            for img_path in self.selected_images:
                shutil.copy(img_path, destination)
            messagebox.showinfo("Copy Complete", f"Copied {len(self.selected_images)} images to {destination}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy images: {e}")




            
    def setup_gui(self):
        menu_bar = Menu(self.self.frm2)
        self.self.frm2.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Browse", command=self.browse_path)
        file_menu.add_command(label="Save Bookmark", command=self.save_bookmarks)
        file_menu.add_command(label="Delete Bookmark", command=self.delete_bookmark)
        file_menu.add_command(label="Add Bookmark", command=self.add_bookmark)
        file_menu.add_command(label="Copy Selected Images", command=self.copy_selected_images)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.self.frm2.quit)

        tools_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Get Images", command=self.get_images)
        tools_menu.add_command(label="Merge Images", command=self.merge_images)
        tools_menu.add_command(label="Show Selected Files", command=self.show_selected_files)
        view_menu =  Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Views", menu=view_menu)
        view_menu.add_command(label="Preview full size", command=self.view_full_image)
        view_menu.add_command(label="Thumnails 64x66", command=self.change_thumbnail_size1)
        view_menu.add_command(label="Thumnails 128x128", command=self.change_thumbnail_size2)
        view_menu.add_command(label="Thumnails 180x180", command=self.change_thumbnail_size3)
        view_menu.add_command(label="Thumnails 256x256", command=self.change_thumbnail_size4)
        self.dir_path = ttk.Entry(self.self.frm2, textvariable=self.path_var, width=50)
        self.dir_path.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.dir_path.insert(0, os.getcwd())
        self.btn_browse = Button(self.self.frm2, bd=8, bg="azure", text="Get Images", command=self.get_images)
        self.btn_browse.grid(row=14, column=0, padx=5)
        self.bookmark_var = StringVar()
        tk.Label(self.self.frm2, text="Bookmarks Drop Down").grid(row=15,column=2)
        self.bookmark_combo = ttk.Combobox(self.self.frm2, textvariable=self.bookmark_var, values=list(self.bookmarks.keys()))
        self.bookmark_combo.grid(row=16, column=2, columnspan=2, sticky="ew", padx=5, pady=5)
        self.bookmark_combo.bind("<<ComboboxSelected>>", self.select_bookmark)


        self.var_recursive = BooleanVar(value=False)
        self.check_recursive = Checkbutton(self.self.frm2, text="Recursive View", variable=self.var_recursive, command=self.update_mode_label)
        self.check_recursive.grid(row=13, column=4, padx=5)
        self.progress_bar = ttk.Progressbar(self.self.frm2, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.grid(row=16, column=4, columnspan=2, pady=5, sticky="ew")
        self.progress_label = tk.Label(self.self.frm2, text="if loading please wait... Progress Bar")
        self.progress_label.grid(row=15, column=4)
        self.mode_label = tk.Label(self.self.frm2, text=self.var_recursive)
        self.mode_label.grid(row=13, column=5)

        self.canvas = tk.Canvas(self.self.frm2, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=6, rowspan=4,sticky="nsew", padx=5, pady=5)
        self.v_scroll = ttk.Scrollbar(self.self.frm2, orient="vertical", command=self.canvas.yview)
        self.v_scroll.grid(row=1, column=8, sticky="ns")
        self.h_scroll = ttk.Scrollbar(self.self.frm2, orient="horizontal", command=self.canvas.xview)
        self.h_scroll.grid(row=11, column=0, columnspan=4, sticky="ew")
        self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)


        self.frame_thumbnails = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_thumbnails, anchor="nw")
        self.frame_thumbnails.bind("<Configure>", lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))
        self.clear_selection_btn = Button(self.self.frm2, bd=7,text="Clear Selection", command=self.clear_selection)
        self.clear_selection_btn.grid(row=14, column=2, padx=5, pady=5)

        self.save_merged_btn = Button(self.self.frm2,bd=6,bg="skyblue", text="Save Merged Image", command=self.save_merged_image)
        self.save_merged_btn.grid(row=14, column=3, padx=5, pady=5)
        self.view_selected_btn = Button(self.self.frm2,bd=5,bg="thistle", text="View Selected Files", command=self.show_selected_files)
        self.view_selected_btn.grid(row=14, column=4, padx=5, pady=5)
        self.copy_images_btn = Button(self.self.frm2, bd=6, bg="lightgreen", text="Copy Selected Images", command=self.copy_selected_images)
        self.copy_images_btn.grid(row=14, column=5, padx=5, pady=5)
    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)
        self.display_selected_thumbnails()
    def adjust_entry_width(self):
        path_length = len(self.path_var.get())
        self.dir_path.config(width=max(50, path_length))

    def delete_bookmark(self):
        selected = self.path_var.get()
        if selected in self.bookmarks:
            del self.bookmarks[selected]
            self.save_bookmarks()
            messagebox.showinfo("Bookmark Deleted", "Bookmark deleted successfully.")

    def add_bookmark(self):
        path = self.path_var.get()
        if not path or not os.path.exists(path):
            messagebox.showwarning("Invalid Path", "Select a valid path before adding a bookmark.")
            return

        name = simpledialog.askstring("Bookmark Name", "Enter a name for the bookmark:")
        if name:
            self.bookmarks[name] = path
            self.save_bookmarks()
            messagebox.showinfo("bokkmark added")

      
    def save_bookmarks(self):
        try:
            with open(self.json_file, "w") as file:
                json.dump(self.bookmarks, file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bookmarks: {e}")

    def delete_bookmark(self):
        selected = self.bookmark_var.get()
        if selected in self.bookmarks:
            del self.bookmarks[selected]
            self.update_bookmarks()
            messagebox.showinfo("Bookmark Deleted", f"Bookmark '{selected}' deleted successfully.")

    def select_bookmark(self, event=None):
        selected = self.bookmark_var.get()
        if selected in self.bookmarks:
            self.path_var.set(self.bookmarks[selected])
            self.adjust_entry_width()

    def use_path(self):
        path = self.path_var.get()
        if os.path.exists(path):
            try:
                if sys.platform == "win32":
                    os.startfile(path)
                elif sys.platform == "darwin":
                    subprocess.run(["open", path], check=True)
                elif sys.platform.startswith("linux"):
                    subprocess.run(["xdg-open", path], check=True)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open path: {e}")

    def load_bookmarks(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as file:
                return json.load(file)
        return {}

    def update_bookmarks(self):
        self.bookmark_combo['values'] = list(self.bookmarks.keys())
        self.save_bookmarks()


   
    def load_images(self, directory):
        extensions = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif')
        self.image_paths = []

        for ext in extensions:
            self.image_paths.extend(glob(os.path.join(directory, ext), recursive=False))

        if not self.image_paths:
            messagebox.showinfo("No Images", "No images found in the selected directory.")
            return

        self.display_thumbnails()
    def get_images(self):
        path = self.path_var.get()
        if not os.path.exists(path):
            messagebox.showerror("Error", "The selected path does not exist.")
            return

        extensions = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif')
        self.image_paths = []

        # Update progress bar parameters
        total_files = sum(len(glob(os.path.join(path, ext))) for ext in extensions)
        self.progress_bar["maximum"] = total_files
        self.progress_bar["value"] = 0

        # Load images and update progress bar
        for ext in extensions:
            for img_path in glob(os.path.join(path, ext)):
                self.image_paths.append(img_path)
                self.progress_bar["value"] += 1  # Increment progress bar
                self.self.frm2.update_idletasks()  # Update UI

        if not self.image_paths:
            messagebox.showinfo("No Images Found", "No images found in the selected directory.")
            return

        self.display_thumbnails()
        self.progress_bar["value"] = 0  # Reset progress bar

    def change_thumbnail_size1(self):
        self.x, self.y = 64,64
        self.display_thumbnails()
        return self.x,self.y
    def change_thumbnail_size2(self):
        self.x, self.y = 128,128
        self.display_thumbnails()
        return self.x,self.y

    def change_thumbnail_size3(self):
        self.x, self.y = 180,180
        self.display_thumbnails()
        return self.x,self.y
    def change_thumbnail_size4(self):
        self.x, self.y = 256,256
        self.display_thumbnails()
        return self.x,self.y       
    def display_thumbnails(self):
        for widget in self.frame_thumbnails.winfo_children():
            widget.destroy()

        for index, img_path in enumerate(self.image_paths):
            try:
                img = Image.open(img_path)
                img.thumbnail((self.x,self.y))
                tk_img = ImageTk.PhotoImage(img)

                frame = Frame(self.frame_thumbnails, bd=10, relief="ridge")
                frame.grid(row=index // 10, column=index % 10, padx=5, pady=5)

                lbl_img = Label(frame, image=tk_img)
                lbl_img.image = tk_img  # Keep reference to avoid garbage collection
                lbl_img.grid(row=0, column=0)

                lbl_img.bind("<Button-1>", lambda e, path=img_path: self.select_image(path))
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")
    def select_image(self, img_path):
        self.current_img_path = img_path  # Update the current image path
        if img_path in self.selected_images:
            self.selected_images.remove(img_path)
        else:
            self.selected_images.append(img_path)
        self.display_selected_thumbnails()

    
    def display_selected_thumbnails(self):
        for widget in self.frame_thumbnails.winfo_children():
            widget.config(bg="alice blue")

        for img_path in self.selected_images:
            index = self.image_paths.index(img_path)
            widget = self.frame_thumbnails.grid_slaves(row=index // 10, column=index % 10)[0]
            widget.config(bg="cyan")

    def show_selected_files(self):
        if not self.selected_images:
            messagebox.showinfo("No Selection", "No images selected.")
            return     
        for img in self.selected_images:
            self.listbox.insert(END, os.path.basename(img))

      
    def remove_selected(self, listbox):
        selected = self.listbox.curselection()
        if selected:
            file_to_remove = self.selected_images[selected[0]]
            self.selected_images.remove(file_to_remove)
            self.listbox.delete(selected)
            self.display_selected_thumbnails()

    def merge_images(self):
        if len(self.selected_images) < 2:
            messagebox.showwarning("Insufficient Images", "Select at least two images to merge.")
            return

        images = [Image.open(img) for img in self.selected_images]
        total_width = sum(img.width for img in images)
        max_height = max(img.height for img in images)

        merged = Image.new("RGB", (total_width, max_height))
        x_offset = 0
        for img in images:
            merged.paste(img, (x_offset, 0))
            x_offset += img.width

        self.preview_image(merged)

    def preview_image(self, img):
        self.frm2 = tab.canvaslevel(self.self.frm2)
        self.frm2.title("Merged Image Preview")
        tk_img = ImageTk.PhotoImage(img)
        lbl_img = Label(self.frm2, image=tk_img)
        lbl_img.image = tk_img  # Keep reference
        lbl_img.grid(row=2, column=4)

   
    def view_full_image(self):
        showimg = ImageViewer(self.self.frm2, self.current_img_path, self.navigate_image)
    def navigate_image(self, direction):
        """
        Updates the current image index and returns the new image path.
        - direction: -1 for Previous, 1 for Next.
        """
        if not self.image_paths:
            return None

        self.current_img_index = (self.current_img_index + direction) % len(self.image_paths)
        self.current_img_path = self.image_paths[self.current_img_index]
        return self.current_img_path

    def update_mode_label(self):
        mode = "Recursive Directory" if self.var_recursive.get() else "Flat Directory"
        self.mode_label.config(text=f"Mode: {mode}")
        self.update_view()  # Reload images on mode change
    def clear_selection(self):
        """Clear all selected images."""
        self.selected_images = []
        self.display_selected_thumbnails()
        messagebox.showinfo("Selection Cleared", "All selected images have been cleared.")
    def save_merged_image(self):
        """Save the merged image."""
        if not hasattr(self, 'merged_image'):
            messagebox.showerror("No Merged Image", "There is no merged image to save.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file_path:
            self.merged_image_save(file_path)
        messagebox.showinfo("Image Saved", f"Merged image saved as {file_path}")
    def update_view(self):
        """Reload images based on the current recursive setting."""
        directory = self.path_var.get()
        if os.path.exists(directory):
            self.load_images(directory)
        else:
            messagebox.showerror("Error", "The directory path is invalid.") 







def main():
    root = Tk()
    root.title("Image Toolz")

    # Initialize main components
    tab_manager = ImageTab(root)
    viewer_tab = tab_manager.add_tab("Viewer")
    thumbnail_tab = tab_manager.add_tab("Thumbnails")

    ImageViewer(viewer_tab)
    image_toolzs =ImageToolz(thumbnail_tab)

    root.mainloop()

if __name__ == "__main__":
    main()