def max_prime(a):#做出质数表的函数
   global prime_list#全局变量
   for i in range(2,a):
       flag=False
       for j in prime_list:
           if i % j == 0:
               flag=True
               break;
       if flag==True:
           continue
       else:
           prime_list.append(i)
   return
def sum_factor(a):#计算出质数和
    sum=0
    global prime_list
    for j in prime_list:
        if a>j: #做个判断，防止输入不规律，如果输入4 8 1000 10 ，没有这条语句，会有巨量无意义的遍历
         for k in prime_list:
             if k<j: #去除重复遍历，2+5和5+7是一样的，需要去除一个
                 continue
             elif k+j==a:
                 sum=sum+1
        else:
            break
    return sum
fin = open('input.txt','r')
list=fin.readlines()
fin.close()
list1=[]
prime_list=[2]
for i in list:
    i1=i.replace('\r','')#去除换行符
    i1=int(i1)
    list1.append(i1)
max_number=max(list1)#找出输入数据中的最大值
max_prime(max_number)
fout=open('output.txt','w')
for j in list:
    j1=int(j)
    j2=sum_factor(j1)
    j2=str(j2)+'\n'
    fout.write(j2)
fout.close()





