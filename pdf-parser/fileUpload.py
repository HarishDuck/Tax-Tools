import tkinter as tk
from tkinter import filedialog

def fileUpload():
    """
    This function deals with extracting the file names not file
    """
    
    # Window
    window = tk.Tk()
    window.title("Select one or multiple files")
    window.withdraw()

    return filedialog.askopenfilename()
    