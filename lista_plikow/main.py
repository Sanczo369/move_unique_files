import os
from tkinter import *
root = Tk()
root.title("Lista Plików")
def file_list(folder,name):
    if not os.path.exists(folder):
        root.quit()
    if len(folder)==0 or len(name)==0:
        name="lista"
        folder="C:\\"
    file_name=name+".txt"
    f = open(file_name,mode='w')
    folder_zrodlowy=folder
    for nazwa_pliku in os.listdir(folder_zrodlowy):
        f.write(nazwa_pliku+"\n")
    f.close()
    root.quit()

# Elements
folder_label = Label(root, text="Podaj ścieżkę do folderu")
name_label = Label(root, text="Podaj nazwe dla nowo powstalego pliku")
folder_entry = Entry(root)
name_entry = Entry(root)
generate_btn = Button(root, text="Generuj", command=lambda: file_list(folder_entry.get(),name_entry.get()))
# Position
folder_label.grid(row=0, column=0)
folder_entry.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
generate_btn.grid(row=2, columnspan=2)

if __name__ == '__main__':
    root.mainloop()
    #file_list()