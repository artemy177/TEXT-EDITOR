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
def get_text_coord(s: str, i: int):
    """
    Из индекса символа получить "координату" в виде "номер_строки_текста.номер_символа_в_строке"
    """
    for row_number, line in enumerate(s.splitlines(keepends=True), 1):
        if i < len(line):
            return f'{row_number}.{i}'
        
        i -= len(line)


def on_edit(event):
    # Удалить все имеющиеся теги из текста
    for tag in text1.tag_names():
        text1.tag_remove(tag, 1.0, tk.END)
    
    # Разобрать текст на токены
    s = text1.get(1.0, tk.END)
    tokens = lexer.get_tokens_unprocessed(s)
    
    for i, token_type, token in tokens:
        print(i, token_type, repr(token))  # Отладочный вывод - тут видно какие типы токенов выдаются
        j = i + len(token)
        if token_type in token_type_to_tag:
            text1.tag_add(token_type_to_tag[token_type], get_text_coord(s, i), get_text_coord(s, j))

    # Сбросить флаг редактирования текста
    text1.edit_modified(0)



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
# Тэги
text1.tag_config("loops", foreground='#FF051D')
text1.tag_config("imports", foreground='green')
text1.tag_config("if_else", foreground='#8B00FF')
text1.tag_config("brackets", foreground='#1F75FE')
text1.tag_config("operators",foreground="#0095B6")
text1.tag_config("basic", foreground='black')
text1.tag_config("string", foreground='#CC5500')
text1.tag_config("int", foreground='#6600FF')
text1.tag_config("functions", foreground='#A9AD00')

# Словари с ключевыми словами
imports = ["import","from","as"]
loops = ["for","while","break","continue","range"]
if_else = ["if","elif","else","True","False"]
brackets = ["(",")","[","]","{","}"]
operators = ["in","=","==",">=","<=","!=","+=","-=",
"*=","/=","%=","//=","**=","|=","^=",">>=","<<=","&=","def"]
functions = ["print","input","int","str","bool","float"]
def checking():
    

    def replace_char(string,chars,separators):  
        for i in chars:
            string = string.replace(i,f"{separators}{i}{separators}")

        return string

    for i in text.tag_names(): # Очищаем тэги
        text.tag_remove(i,1.0,tk.END)
   
    a = text.get(1.0,tk.END)
    chars = [" ","\n","(",")","[","]","{","}",":",","]
    a = replace_char(a,chars,"⠀")
    a = a.split("⠀") 
    ''' Далее разбиваем строку по невидимым символам 
    (но этот вариант с невидимкой или другим любым символом не очень, 
    ведь его могут ввести в качестве строки в коде) и  ещё текст ткинтера его не различает'''

    text.delete(1.0,tk.END) # Очищаем текстовое поле
    
    # Проводим цикл по всем элементам списка
    for i in a:
        

        if i in loops: # Проверка по категориям 
            text.insert(tk.END,i,'loops')

        elif i in imports:   
            text.insert(tk.END,i,'imports') 

        elif i in if_else:   
            text.insert(tk.END,i,'if_else') 

        elif i in brackets:   
            text.insert(tk.END,i,'brackets')

        elif i in operators:   
            text.insert(tk.END,i,'operators') 

        elif i.startswith("'") and i.endswith("'") or i.startswith('"') and i.endswith('"'):
            text.insert(tk.END,i,'string') 

        elif i.isdigit():
            text.insert(tk.END,i,'int') 

        elif i in functions:
            text.insert(tk.END,i,'functions') 

        else:
            text.insert(tk.END,i,"basic")

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
text1 = Text(root)
text1.pack()
# создание окна

button2 = tk.Button(root, text="сохранить", bg ="black",fg="white", command=save_as_file)
button2.place(x=420, y=570)
button1 = tk.Button(root, text="открыть", bg ="black",fg="white", command=open_file)
button1.place(x=500, y=570)
# создание фрейма для поля поиска
#fram = Frame(root)





# Создаём теги с разными свойствами, которые будем присваивать соответствующим типам токенов
text.tag_config("keyword", foreground='blue')
text.tag_config("string_literal", foreground='red')

# Прописываем соответствие типа токена тегу подсветки
token_type_to_tag = {
    Token.Keyword: "keyword",
    Token.Operator.Word: "keyword",
    Token.Name.Builtin: "keyword",
    Token.Literal.String.Single: "string_literal",
    Token.Literal.String.Double: "string_literal",
}


#0 Token.Comment.Single '# Комментарий'
#13 Token.Text '\n'
#text.tag_config("comment", foreground='gray')
'''token_type_to_tag = {
    ...
    Token.Comment.Single: "comment",'''

text_info = Text (root, yscrollcommand=Scrollbar.set)
text_info.pack(fill=BOTH)
#text_info.grid (fill=BOTH)

#button1 = tk.Button(root, text="открыть", bg ="black",fg="white", command=open_file)
#button1.place(row=2, column=1 , padx=10, pady=5, )
 

#воспроизведение окна
root.mainloop()
