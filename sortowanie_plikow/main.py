import os
import shutil
from tkinter import *
root = Tk()
root.title("Puki Majster")


def move_unique_files(folder_zrodlowy, folder_deocelowy):
    # Sprawdzenie istnienia folderu żródłowego jeśli nie istnieje program sie kończy
    if not os.path.exists(folder_zrodlowy):
        root.quit()
    # Sprawdzenie istnienia folderu docelowego jak cos to tworzy folder
    if not os.path.exists(folder_deocelowy):
        os.makedirs(folder_deocelowy)
    # Przechowywanie nazw plików
    lista_nazw_plikow = []
    lista_poczatkow_nazw_plikow = []
    # Przeszukiwanie folderu źródłowego
    for nazwa_pliku in os.listdir(folder_zrodlowy):
        poczatek_nazwy=nazwa_pliku.split("_")[0]
        if len(lista_nazw_plikow) == 0 and len(lista_poczatkow_nazw_plikow) == 0:
            lista_poczatkow_nazw_plikow.append(poczatek_nazwy)
            lista_nazw_plikow.append(nazwa_pliku)
        else:
            for plik_nazwa_new in lista_nazw_plikow:
                if not plik_nazwa_new.split("_")[0] == poczatek_nazwy:
                    lista_poczatkow_nazw_plikow.append(poczatek_nazwy)
                    lista_nazw_plikow.append(nazwa_pliku)
    # Przenoszenie plików do folderu docelowego
    for pojedynczy_plik in lista_nazw_plikow:
        source_path = os.path.join(folder_zrodlowy, pojedynczy_plik)
        destination_path = os.path.join(folder_deocelowy, pojedynczy_plik)
        shutil.move(source_path, destination_path)
        #print(f"Przeniesiono plik: {pojedynczy_plik}")




# Elements
folder_zrodlowy_label = Label(root, text="Podaj ścieżkę do folderu zródłowego")
folder_docelowy_label = Label(root, text="Podaj ścieżkę do folderu docelowego")
folder_zrodlowy_entry = Entry(root)
folder_docelowy_entry = Entry(root)
zipcode_btn = Button(root, text="Sortuj")
# Position
folder_zrodlowy_label.grid(row=0, column=0)
folder_zrodlowy_entry.grid(row=0, column=1)
folder_docelowy_label.grid(row=1, column=0)
folder_docelowy_entry.grid(row=1, column=1)
zipcode_btn.grid(row=2, columnspan=2)
if __name__ == '__main__':
    root.mainloop()