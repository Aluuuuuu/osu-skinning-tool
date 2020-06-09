import os
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import ttkthemes as ttkh
from tkinter import filedialog

root = tk.Tk()
tabs = ttk.Notebook()
extrasTab = ttk.Frame(tabs)
extrasTab.pack()
someOtherTab = ttk.Frame(tabs)
someOtherTab.pack()

tabs.add(extrasTab, text="Extras")
tabs.add(someOtherTab, text="Some Other Tab")

tabs.pack(expand=1, fill="both")

root.title("osu! Skinning Tool - Dev")
root.geometry("900x600")
root.minsize(500, 300)
root.resizable(1, 1)

def exit():
    root.destroy()

butExit = ttk.Button(root,
                text = "Exit",
                command = exit)

butExit.place(anchor="se",
            bordermode="outside",
            relx="0.15",
            rely="0.95")


themes = ttk.Style().theme_names()
ttk.Style().theme_use("clam")
themes = ttkh.ThemedStyle(root).theme_names()

theme = 0
def switchTheme():
    global theme
    if theme >= len(themes)-1:
        theme = 0
    else:
        theme = theme + 1
    print(themes[theme])
    ttk.Style().theme_use(themes[theme])


butThemeSwitch = ttk.Button(root,
                        text="Switch Theme",
                        command=switchTheme)

butThemeSwitch.place(anchor="se",
                    bordermode="outside",
                    relx="0.95",
                    rely="0.15")

ttkh.ThemedStyle(root).set_theme("black")
root.configure(bg="#333")

skDir = pathlib.Path(__file__).parent.absolute()

skinsBox = tk.Listbox(extrasTab, selectmode=tk.SINGLE, bg="#555", fg="#fff", highlightbackground="#777")
skinsBox.place(relheight="0.70", relwidth="0.8", relx="0.1", rely="0.1")
def getSelectedSkin():
    skinSelected = skinsBox.get(skinsBox.curselection())
    print(skinSelected)
skinsBox.bind("<<ListboxSelect>>", lambda x: getSelectedSkin())

def relistSkins(dir):
    skinsBox.delete(0, tk.END)
    for entry in os.scandir(dir):
        if(entry.is_file()):
            pass
        else:
            skinsBox.insert(tk.END, str(entry)[11:len(str(entry))-2])

relistSkins(skDir)

def getSkDir():
    global skDir
    skDir2 = skDir
    skDir = filedialog.askdirectory(title="Select your osu! Skins directory.")
    skDir = str(skDir)
    if(os.path.isdir(skDir) is False):
        skDir = skDir2
    relistSkins(skDir)
    return

butSkDir = ttk.Button(root,
                 text="Change Skins folder",
                 command=getSkDir)

butSkDir.place(anchor="se",
              bordermode="outside",
              relx="0.95",
              rely="0.95")

root.mainloop()
