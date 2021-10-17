import tkinter

root = tkinter.Tk()
root.geometry("1000x1000")
root.title("test")
root.configure(bg="Black")

def Dodawanie():
    h = int(input("Podaj 1 liczbe którą chcesz dodać"))
    j = int(input("Podaj 2 liczbe którą chcesz dodać"))
    n = h + j
    print("tyle", n)

b = tkinter.Button(root, text="dodawanie", command=Dodawanie, borderwidth=20)
b.pack()
b.place(x=500, y=500)

def dzielenie():
    u = int(input("Podaj 1 liczbe którą chcesz dzielić"))
    i = int(input("Podaj 2 liczbe którą chcesz dzielić"))
    o = u / i
    print("tyle", o)

l = tkinter.Button(root, text="Dzielenie", command=dzielenie, borderwidth=20)
l.pack()
l.place(x=300, y=300)

def Mnożenie():
    m = int(input("Podaj 1 liczbe którą chcesz mnożyć"))
    b = int(input("Podaj 2 liczbe którą chcesz mnożyć"))
    n = b * m
    print("tyle", m)

d = tkinter.Button(root, text="Mnożenie", command=Mnożenie, borderwidth=20)
d.pack()
d.place(x=700, y=700)

def odejmowanie():
    g = int(input("Podaj 1 liczbe którą chcesz odjąć"))
    k = int(input("Podaj 2 liczbe którą chcesz odjąć"))
    f = g - k
    print(k)

p = tkinter.Button(root, text="Odejmowanie", command=odejmowanie, borderwidth=20)
p.pack()
p.place(x=100, y=300)
root.mainloop()
#123