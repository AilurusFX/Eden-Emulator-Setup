import tkinter as tk
import eff_slotter
from tkinter import filedialog

root = tk.Tk()

folder_path = filedialog.askdirectory(initialdir="./", title="Open the root directory for your mod")

name = input("What is the name of the fighter? ")
slot = input("What costume slot do you want to move the effect to? ")

eff_slotter.do_it(folder_path, name, slot)