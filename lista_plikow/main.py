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
if __name__ == '__main__':
    #root.mainloop()
    file_list()