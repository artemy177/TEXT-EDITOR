from tkinter import*
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import fileinput
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.messagebox import *
from idlelib.colorizer import ColorDelegator, color_config
from idlelib.percolator import Percolator
from idlelib.undo import UndoDelegator
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
def open_file():
    text.delete(1.0, END)
    open = askopenfilename()
    file_name.configure(text=open)
    for i in fileinput.input(open):
        text.insert(END, i)  
def save_as_file():

    save_as = asksaveasfilename(defaultextension=".txt")
    letter = text.get(1.0, END)
    f = open(save_as, "w")
    f.write(letter)
    f.close()
    file_name.configure(text=f.name)
# функция для поиска строки в тексте
def find():
    # Удаление тега «найдено» от индекса 1 до END
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        idx = '1.0'
        while True:
            # Поиск желаемой строки от индекса 1
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx:
                break
            # Последний индекс — сумма текущего индекса и длины текста
            lastidx = f"{idx}+{len(s)}c"
            # Пометка найденной строки
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        # Пометка найденной строки красным цветом
        text.tag_config('found', foreground='red')





#создание окна
root = Tk()



root.geometry ("600x600")
root.title("notebook")

#создание кнопки 
#buttonAdd = tk.Button(root, text="сохранить",  c, command=Save)
#buttonAdd.grid(row=2, column=0, padx=10, pady=1, sticky="we")
#buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")
scr = Scrollbar(root)
file_name = Label(root, text="Здесь будет имя открытого файла")
file_name.pack()
# добавление метки в поле поиска
labl1 =  tk.Label (root, text = 'поиск:' )
labl1.pack()


# добавление поля текста в одну строку
edit = Entry(root)
edit.pack(side = TOP, fill = NONE, expand = 1 )
edit.focus_set()
# добавление кнопки поиска
butt = tk.Button(root, text = 'поиск',bg ="black",fg="white", command=find)
#butt.place(x=300, y = 300)
butt.pack(side = RIGHT)
butt.pack(side = TOP)
# текстовый виджет в корневом окне
text = Text(root, yscrollcommand=scr.set, width=100, height=20)
text.pack(side=LEFT, fill=BOTH)
text.insert( '4.0' , '''''' )
text.pack(side = BOTTOM)


#2 тукст по англу читать




cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat().pattern, re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat().pattern, re.S)

# These five lines are optional. If omitted, default colours are used.
cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}

ip.Percolator(text).insertfilter(cdg)



button2 = tk.Button(root, text="сохранить", bg ="black",fg="white", command=save_as_file)
button2.place(x=420, y=570)
button1 = tk.Button(root, text="открыть", bg ="black",fg="white", command=open_file)
button1.place(x=500, y=570)
# создание фрейма для поля поиска
#fram = Frame(root)











text = Text (root, yscrollcommand=Scrollbar.set)

#text_info.grid (fill=BOTH)

#button1 = tk.Button(root, text="открыть", bg ="black",fg="white", command=open_file)
#button1.place(row=2, column=1 , padx=10, pady=5, )
 

#воспроизведение окна
root.mainloop()
