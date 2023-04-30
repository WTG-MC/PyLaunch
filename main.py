import os
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Create a Tkinter window
window = tk.Tk()
window.title("Pylaunch V1.0")
window.geometry("500x450")
window.configure(bg="#383838")


# Define a function to browse for an application
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        app_list.insert("end", file_path)


# Define a function to launch the selected application
def launch_app():
    selected = app_list.curselection()
    if selected:
        app = app_list.get(selected)
        subprocess.Popen(app)


# Define a function to remove the selected application
def remove_app():
    selected = app_list.curselection()
    if selected:
        app_list.delete(selected)


# Create a list to hold the selected application paths
app_list = tk.Listbox(window, bg="white", fg="black", font=("Calibri", 10), height=6)
app_list.pack(padx=10, pady=(10, 0), fill="both", expand=True)

# Create a button to browse for an application
browse_button = ttk.Button(window, text="Add", command=browse_file)
browse_button.pack(pady=(5, 5))
style = ttk.Style()
style.map("TButton", foreground=[('active', '#383838'), ('!disabled', '#383838')],
          background=[('active', '#F79646'), ('!disabled', '#F79646')])
style.configure("TButton", padding=5, relief="flat", font=("Calibri", 12))
browse_button.configure(style="TButton")

# Create a button to launch the selected application
launch_button = ttk.Button(window, text="Launch", command=launch_app)
launch_button.pack(pady=(5, 5))
style.map("TButton", foreground=[('active', '#383838'), ('!disabled', '#383838')],
          background=[('active', '#0072C6'), ('!disabled', '#0072C6')])
launch_button.configure(style="TButton")

# Create a button to remove the selected application
remove_button = ttk.Button(window, text="Remove", command=remove_app)
remove_button.pack(pady=(0, 10))
style.map("TButton", foreground=[('active', '#383838'), ('!disabled', '#383838')],
          background=[('active', '#F79646'), ('!disabled', '#F79646')])
remove_button.configure(style="TButton")

# Run the Tkinter event loop
window.mainloop()
