#5.8 author:Hartman
import re,random,codecs
from tkinter import *
import tkinter.messagebox
def king():
    name=entry1.get('1.0','end')
    number=entry2.get()#读取左边输入框的内容
    number1=int(number)#把读取的字符串转换成整数型
    if not name : #判断是否输入了东西
         tkinter.messagebox.showinfo("提示：","请输入人数和名字")
         return
    end1.delete('1.0', 'end')  # 清空右边两个文本框原来的内容
    end2.delete('1.0', 'end')
    rule=re.compile(r'(.*?)\n')#编写正则，“\n”即换行符前的东西全匹配
    nlist=re.findall(rule,name)#匹配到的结果全保存进列表
    list1 = list(range(1, number1 + 1))#生成一个列表，range（）函数在PY3里返回的不是函数，需要用一个list()来承接
    king = random.randint(1, number1)
    random.shuffle(list1)
    for i in range(0, number1):
            str1=str(list1[i])+'  '+nlist[i]+'\n'
            end1.insert(INSERT,str1)
            if i+1==king:
              end2.insert(INSERT,nlist[i])
    return
root=Tk()#GUI设计
root.geometry("380x500+400+100")#设置窗口的大小，以及离屏幕两边的距离
root.title('kinggame')#设置标题
Label(root,text='顺序输入名字').grid(row=0,column=0)#四个标签
Label(root,text='输入人数').grid(row=2,column=0)
Label(root,text='结果').grid(row=0,column=2)
Label(root,text='国王是').grid(row=2,column=2)
numbers=IntVar()
entry1=Text(root,width=20,height=30)#4个文本框
entry1.grid(row = 1,column=0,padx=10,pady=10,sticky = W)
end1=Text(root,width=20, height=30)
end1.grid(row = 1,column=2,padx=1,sticky = E)
entry2=Entry(root,width=20, textvariable=numbers)
entry2.grid(row = 3,column=0,padx=10,pady=10,sticky = W)
end2=Text(root,width=20,padx=1, height=1)
end2.grid(row = 3,column=2,sticky = E)
button = Button(root,text='开始',font=('微软雅黑',10),fg='red',command=king)#一个按钮，按下就执行函数king
button.grid(row=1,column=1,padx=10)
root.mainloop()#创建窗口


