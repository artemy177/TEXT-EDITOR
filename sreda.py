from tkinter import*
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import fileinput
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.messagebox import *
from pygments.lexers import PythonLexer
from pygments.token import Token
def open_file():
    txtView.delete(1.0, END)
    open = askopenfilename()
    file_name.configure(text=open)
    for i in fileinput.input(open):
        txtView.insert(END, i)  
def save_as_file():

    save_as = asksaveasfilename(defaultextension=".txt")
    letter = txtView.get(1.0, END)
    f = open(save_as, "w")
    f.write(letter)
    f.close()
    file_name.configure(text=f.name)
# функция для поиска строки в тексте
def find():
    # Удаление тега «найдено» от индекса 1 до END
    txtView.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        idx = '1.0'
        while True:
            # Поиск желаемой строки от индекса 1
            idx = txtView.search(s, idx, nocase=1, stopindex=END)
            if not idx:
                break
            # Последний индекс — сумма текущего индекса и длины текста
            lastidx = f"{idx}+{len(s)}c"
            # Пометка найденной строки
            txtView.tag_add('found', idx, lastidx)
            idx = lastidx
        # Пометка найденной строки красным цветом
        txtView.tag_config('found', foreground='red')

#сохранение текстового файла
'''def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
                    with open(file_path, 'w') as file:
                        text_content = text_widget.get("1.0", "end-1c")
                        file.write(text_content)
                    status_label.config(text=f"File saved: {file_path}")
                except Exception as e:
                    status_label.config(text=f"Error saving file: {str(e)}")'''

#создание кнопки 



#создание окна
lexer = PythonLexer()
root = Tk()
text1 = tk.Text(root)
text1.pack()



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


txtView = Text(root, yscrollcommand=scr.set, width=100, height=20)
txtView.pack(side=LEFT, fill=BOTH)
#2 тукст по англу читать

# текстовый виджет в корневом окне
text = Text(root)
text.insert( '1.0' , '''Type your text here''' )
text.pack(side = BOTTOM)
from tkinter import *

# создание окна

button2 = tk.Button(root, text="сохранить", bg ="black",fg="white", command=save_as_file)
button2.place(x=420, y=570)
button1 = tk.Button(root, text="открыть", bg ="black",fg="white", command=open_file)
button1.place(x=500, y=570)
# создание фрейма для поля поиска
#fram = Frame(root)











text_info = Text (root, yscrollcommand=Scrollbar.set)
text_info.pack(fill=BOTH)
#text_info.grid (fill=BOTH)

#button1 = tk.Button(root, text="открыть", bg ="black",fg="white", command=open_file)
#button1.place(row=2, column=1 , padx=10, pady=5, )
 

#воспроизведение окна
root.mainloop()
