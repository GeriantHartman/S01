#author:Hartman 2017.9.21 varsion:4.0
import re,codecs
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
def start():
    c=0
    date = entry1.get()
    totil = entry2.get()
    totil = totil.replace('\n', '')
    totil = float(totil)
    date = date.replace('\n' , '')
    date = date.replace('日', '[日号]')
    data = text.get('1.0' ,'end')
    data = re.sub(date, '',data )
    clear_rule = re.compile('放生[生款]*|随喜|：|:|我;\n')
    name_rule = re.compile('(.*?)[.0-9]*[元块]')
    money_rule =re.compile('([.0-9]*)\d*[元块]')
    data = re.sub(clear_rule,'',data)
    name= re.findall(name_rule,data)
    money = re.findall(money_rule, data)
    file1 = codecs.open('name.txt', 'w', encoding='utf-8')
    for i in name:
      i=i+"\r\n"
      file1.write(i)
    file2 = codecs.open('money.txt', 'w', encoding='utf-8')
    for k in money:
      b=float(k)
      c=c+b
      k=k+"\r\n"
      file2.write(k)
    file1.close()
    file2.close()
    if(c==totil):
        tkinter.messagebox.showinfo("提示：", "表格创建完成")
    else:
        tkinter.messagebox.showinfo("提示：", "金额数目不符")
    return
def clear():
    text.delete('1.0', 'end')
    return
root = Tk()
root.geometry('+400+200')
root.title('报账用')
label1 = Label(root,text='输入日期')
label1.grid()
entry1 = Entry(root)
entry1.grid()
label2 = Label(root,text='输入总金额')
label2.grid()
entry2 = Entry(root)
entry2.grid()
text = ScrolledText(root, font=('微软雅黑', 10)) #设置滚动条
text.grid()
button1 = Button(root, text='创建表格', font=('微软雅黑',10,), command=start)#设置按键
button1.grid()
button2 = Button(root, text='清除内容', font=('微软雅黑',10,), command=clear)
button2.grid()
root.mainloop()
