#!/usr/bin/env python3
"""
Text Replacer Application

This script provides a graphical user interface for replacing text in multiple files within a selected directory.
"""

import logging
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

# Configure logging
logging.basicConfig(level=logging.INFO)

__version__ = "ver. 0.5 / 25.08.2023"
print(f"\n  -- QFFNR {__version__} by Jonáš Schröder --\n")

class TextReplacerApp:
    """
    Text Replacer Application Class
    
    This class creates a GUI for replacing text in multiple files within a selected directory.
    """
    def __init__(self, root):
        """
        Initialize the application.
        
        Args:
            root (tk.Tk): The main Tkinter window.
        """
        self.root = root
        self.root.title("QFFNR")

        self.notification_label = tk.Label(self.root, text="", bg='white')
        self.notification_label.pack()
        self.notification_label.config(text="Notifications", fg='gray')

        # Change the background color to orange
        self.root.configure(bg='orange')

        # Increase default window size
        self.root.geometry("600x400")

        self.to_be_replaced = tk.StringVar(value="2-0")
        self.replaced_with = tk.StringVar(value="1-1")
        self.file_extension = tk.StringVar(value=".txt")

        self.create_widgets()

        # Add "made by Jonáš Schröder" text
        made_by_label = tk.Label(self.root, text="Made by Jonáš Schröder", font=("italic", 8), bg='orange', fg='gray')
        version_label = tk.Label(self.root, text=__version__, font=("italic", 8), bg='orange', fg='gray')
        
        made_by_label.pack(anchor='se', padx=5, pady=5, side=tk.LEFT)
        version_label.pack(anchor='se', padx=5, pady=5, side=tk.RIGHT)

    def create_widgets(self):
        """
        Create GUI widgets.
        """
        # Add version header
        version_header = tk.Label(self.root, text="Text Replacement in Files", font=("bold", 17), bg='orange')
        version_header.pack(pady=10)

        # Text replacement
        self.to_be_replaced_label = tk.Label(self.root, text="Replace:", bg='orange')
        self.to_be_replaced_label.pack()

        self.to_be_replaced_entry = tk.Entry(self.root, textvariable=self.to_be_replaced)
        self.to_be_replaced_entry.pack()

        self.replaced_with_label = tk.Label(self.root, text="With:", bg='orange')
        self.replaced_with_label.pack()

        self.replaced_with_entry = tk.Entry(self.root, textvariable=self.replaced_with)
        self.replaced_with_entry.pack()

        # File extension
        self.file_extension_label = tk.Label(self.root, text="File Extension:", bg='orange')
        self.file_extension_label.pack()

        self.file_extension_combobox = ttk.Combobox(self.root, textvariable=self.file_extension)
        self.file_extension_combobox['values'] = ['.txt', '.csv', '.log']  # Example extensions
        self.file_extension_combobox.pack()

        # Create a frame for replace options
        replace_option_frame = tk.Frame(self.root, bg='orange')
        replace_option_frame.pack()

        replace_option_label = tk.Label(replace_option_frame, text="Replace Option:", bg='orange')
        replace_option_label.pack(side=tk.LEFT, padx=10)

        self.replace_option = tk.StringVar(value="all")  # Default value for the replace option

        # Create a sub-frame for buttons
        option_buttons_frame = tk.Frame(replace_option_frame, bg='orange')
        option_buttons_frame.pack(padx=10, pady=10)

        all_option = tk.Radiobutton(option_buttons_frame, text="All", variable=self.replace_option, value="all", bg='orange')
        all_option.pack(anchor='w', padx=10)

        first_option = tk.Radiobutton(option_buttons_frame, text="First", variable=self.replace_option, value="first", bg='orange')
        first_option.pack(anchor='w', padx=10)

        last_option = tk.Radiobutton(option_buttons_frame, text="Last", variable=self.replace_option, value="last", bg='orange')
        last_option.pack(anchor='w', padx=10)

        # Create a frame for buttons
        button_frame = tk.Frame(self.root, bg='orange')
        button_frame.pack()

        self.select_dir_button = tk.Button(button_frame, text="Select Directory", command=self.select_directory, bg='dark gray', fg='white')
        self.select_dir_button.pack(side=tk.TOP, padx=30, pady=5)  # Stacked on top with padding

        self.process_button = tk.Button(button_frame, text="Process Files", command=self.process_files, bg='black', fg='white', height=2, width=15)
        self.process_button.pack(side=tk.TOP, padx=10, pady=5)  # Stacked on top with padding

    def select_directory(self):
        """
        Open a file dialog to select a directory.
        """
        selected_dir = filedialog.askdirectory()
        self.selected_dir = selected_dir

        if selected_dir:
            self.notification_label.config(text=f"'{selected_dir}'")

    def process_files(self):
        """
        Replace text in selected files based on the chosen file extension.
        """
        to_be_replaced = self.to_be_replaced.get()
        replaced_with = self.replaced_with.get()
        selected_extension = self.file_extension.get()

        if not hasattr(self, 'selected_dir'):
            logging.error("No directory selected.\n")
            self.notification_label.config(text=f"No directory selected.", fg='red')
            return

        selected_files = [f for f in os.listdir(self.selected_dir) if f.endswith(selected_extension)]

        if not selected_files:
            logging.error(f"  {self.selected_dir} -- There are no {selected_extension} files\n")
            self.notification_label.config(text=f"There are no {selected_extension} files in the directory !!!", fg='red')
            return

        for file_name in selected_files:
            file_path = os.path.join(self.selected_dir, file_name)
            with open(file_path, 'r+') as file:
                logging.info(f"  Processing file  :  {file_name}")
                self.notification_label.config(text=f"Processing file  :  {file_name}", fg='gray')
                contents = file.read()

                if self.replace_option.get() == "all":
                    new_contents = contents.replace(to_be_replaced, replaced_with)
                elif self.replace_option.get() == "first":
                    new_contents = contents.replace(to_be_replaced, replaced_with, 1)
                elif self.replace_option.get() == "last":
                    new_contents = contents[::-1].replace(to_be_replaced[::-1], replaced_with[::-1], 1)[::-1]

                file.seek(0)
                file.write(new_contents)
                file.truncate()

        print("\n  -- finished --\n")
        logging.info("  Files processed successfully.\n")
        self.notification_label.config(text=f"Files processed successfully.", fg='gray')

if __name__ == "__main__":
    root = tk.Tk()
    app = TextReplacerApp(root)
    root.mainloop()
