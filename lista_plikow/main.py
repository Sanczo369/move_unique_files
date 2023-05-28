import os
from tkinter import *
root = Tk()
root.title("Lista Plików")
def file_list():
    f = open("wynik.txt",mode='w')
    folder_zrodlowy=input("Podaj sciezke do folderu")
    for nazwa_pliku in os.listdir(folder_zrodlowy):
        f.write(nazwa_pliku+"\n")
    f.close()

# Elements
folder_label = Label(root, text="Podaj ścieżkę do folderu")
name_label = Label(root, text="Podaj nazwe dla nowo powstalego pliku")
folder_entry = Entry(root)
name_entry = Entry(root)
generate_btn = Button(root, text="Generuj")
# Position
folder_label.grid(row=0, column=0)
folder_entry.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
generate_btn.grid(row=2, columnspan=2)

if __name__ == '__main__':
    root.mainloop()
    #file_list()