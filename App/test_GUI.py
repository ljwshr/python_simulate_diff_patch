import tkinter as tk  
from tkinter import filedialog  
  
root = tk.Tk()  
root.withdraw()  
  
file_path = filedialog.askopenfilenames()  
print(isinstance(file_path, tuple))
temp=list(file_path)
print(temp)