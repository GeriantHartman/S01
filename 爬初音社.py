#5.7 author:Hartman
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import re,requests
def get():
    global var1
    page=int(pageget.get())
    text.delete('1.0',END)
    for z in range(0,page+1):#制作多页
     if z==1:#机器从0开始计数，目标网页page1指向page0
         continue
     else:
      hd ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3004.3 Safari/537.36'}#模拟浏览器操作
      author_url=urlget.get()+'/page/'+str(z)
      html= requests.get(author_url,headers=hd).text#获取网页源代码
      rule=re.compile(r'<article class="excerpt">.*?</header>',re.S)
      q=re.findall(rule,html)
      for i in q:
          rule1=re.compile(r'href="(.*?)"')
          url=re.findall(rule1,i)#findall模式才有零宽断言，这里需要用这个
          if url:
              rule2=re.compile(r'title="(.*?)"')
              title=re.findall(rule2,i)
              text.insert(END,title[0]+url[0]+'\n')
              var1.set('抓取中···')
      var1.set('抓取完毕！')
    return
root=Tk()
root.geometry('+400+200')#设置位置，如设置大小则在引号内一起加上400x200
root.title('简易爬虫')#标题命名
label=Label(root,text='初音社目标网址:').grid(row=0,sticky = W)
urlget=Entry(root,width=70)
urlget.grid(row=1,column=0,sticky=W)
label=Label(root,text='要爬取的页数：').grid()
pageget=Entry(root,width=3)
pageget.grid()
text = ScrolledText(root,font=('微软雅黑',10))#设置滚动条
text.grid()
button = Button(root,text='开始',font=('微软雅黑',10),command=get)#设置按键
button.grid()
var1=StringVar()#设置一个变量
labe2=Label(root,font=('微软雅黑',10),fg='blue',textvariable=var1)#设置一个微键
labe2.grid()
var1.set('已准备···')
root.mainloop()#发送创建窗口的指令，进入循环

