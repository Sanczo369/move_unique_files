from tkinter import *
root = Tk()
root.title("Lista Plików")
f = open("wynik.txt",mode='w')
f.write("test")
f.close()
if __name__ == '__main__':
    root.mainloop()