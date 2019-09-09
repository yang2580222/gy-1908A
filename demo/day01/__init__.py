
'''s = 0
for i in range(1,101):
    s += i
print(s)
for i in range(1,101):
    s += i
print(s)
'''
'''
s = 0
for i in range(1,101):
    s += i
print(s)

for i in range(100):
    if(i == 5):
      break
    print(i)

s = 0
for i in range(1,101):
    s += i
print(s)
for i in range(1,101):
    s*=i
print(s)


for i in range(2,100):
    f = False # 标记i是否被整除
    for j in range(2,i):
        if(i%j==0):
            f = True #如果i被整除，把f值改成True
            break
    if (not f):
        print(i)


f

a = [90,43,2,63,6,3,4]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if(a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
print(a)

'''
'''
for i in range(2,101):
    if(i == 2):
        print(i)
        continue
    f = 1
    for j in range(2,i):
        if(i%j == 0):
            f = 0
            break
    if(f == 1):
        print(i)

i = 1
while(i <= 100):
    print(i)
    i+=1

i = 1
while(i <= 100):
    i+=1
    print(i)
'''
'''
def jia_fa():
    a = 1
    b = 2
    print(a+b)

jia_fa()

a = 1
b = 2
print(a+b)
a = 1
b = 2
print(a+b)
'''
#无参无返回值


'''#有参无返回值
def pengyijie(a,b):
    print(a+b)
pengyijie(8,5)
#有参无返回值
def yang_yun_fei(a,b):
    print(a+b)
yang_yun_fei(3,5)
#y有参有返回值
def yang_yun_fei(a,b):
    return a + b
c = yang_yun_fei(4,7)
print(c)

#无参有返回值
def yang_yun_fei():
    a = 1
    b = 2
    return a + b
c = yang_yun_fei()
print(c)
'''
'''
#无参无返回值
def yang_y():
    a = 2
    b = 3
    print(a+b)

yang_y()
#无参有返回值
def yang_y():
    a = 2
    b = 3
    return a + b
c = yang_y()
print(c)
#有参有返回值
def yang_y(a,b):
    return a + b
c = yang_y(5,6)
print(c)
print(yang_y(5,6))


def yyy(a,b = 12):
    return a + b
print(yyy(22))
print(yyy(22,33))
print(yyy(22,b = 22))

def ccc(*args,**kwargs):
    print(args)
    print(kwargs)
ccc(2,3,5,6,9)
ccc(1,2,3,a=22,b=55)


def yang_y(a,b):
    return a + b
c = yang_y(5,6)
print(yang_y(5,6))

class ClassDemo():
    def xxx(self):
        print("哈哈哈")
    def yyy(self):
        print("你你你")
        self.xxx()
if __name__ == '__main__':
    c = ClassDemo()
    c.yyy()
    c.xxx()


class CkkDa():
    def a(self):
        print("hahha")
    def b(self):
        print("ninini")
        self.a()
if __name__ == '__main__':
    c = CkkDa()
    c.a()
    c.b()
#dergakio   要求生成两个新的字符串  drai  和egko
a = "dergakio"
print(a[::2])
print(a[1::2])
print(a[0:7:2])
print(a[1:8:2])

k = "nndgfcydftasuia"
print(k[2:6])
print(k[2:6:2])
print(k[2:8:-1])

d = '用例名,充值金额,断言'
print(d.split(","))

k = '吴亦凡,李易峰,罗云熙'
print(k.split(','))

#去空格
l = '   kdgsyydysv   '
print(l.strip())
#去左空格
print(l.lstrip())
#去右空格
print(l.rstrip())

#替换
p = 'nbui"dbc'
print(p.replace(' ',''))

print(p.replace('"',''))

'''
# GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
'''
#截取
'''
'''
a = "GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1"
print(a[:3])
a = 'bcuiegfevb'
print(a[::-1])
print(a[:1:-1])

m = [1,2,3,4,5,6,7,8,9,]
m.append(16)
print(m)
m.insert(2,11)
print(m)
n = [5,6,7,8]
m.extend(n)
print(m)
print(n)

print(m.pop())
print(m)
print(m.pop(2))
print(m)
print(m.pop(-5))
print(m)
m.remove(2)
print(m)

print(m.index(1))
m[m.index(1)] = 9
print(m)
print(len(m))
m.sort(reverse=True)
print(m)

a = {"name":"杨云飞","sex":"女"}
a["age"] = 18
print(a)
h = {'name':'杨云飞','age':'19',}
h['学历'] = '本科'
print(h)

print(h.pop("name"))
print(h)
del h["age"]
print(h)

del h
print(h)

h.clear()

x = {"name":"杨云飞","sex":"女"}
x ["age"] = 18
print(x)
x["学历"],x["地址"] = "本科","河南"
print(x)
x["name"] = "消化"
print(x)
print(x["name"])
#字典拼接
w = {1:'123',2:'325'}
w1 = {2:'145',4:'852'}
w.update(w1)
print(w)


class YangYun1():
    def hallo_lou_1(self):
        print("哈哈喽喽")
    def hallo_lou_2(self):
        print("哈哈喽喽2")
class YangYun2():
    def hallo_lou_3(self):
        print("哈哈喽喽3")
    def hallo_lou_4(self):
        print("哈哈喽喽4")

def aaa():
    print("嘻嘻哈哈")
    

'''
class ClassDemo1():
    def class_method_1(self):
        print("我是feng_zhuang_1模块里ClassDemo1类中的class_method_1方法")
    def class_method_2(self):
        print("我是feng_zhuang_1模块里ClassDemo1类中的class_method_2方法")
class ClassDemo2():
    def class_method_3(self):
        print("我是feng_zhuang_1模块里ClassDemo1类中的class_method_3方法")
    def class_method_4(self):
        print("我是feng_zhuang_1模块里ClassDemo1类中的class_method_4方法")




#h = open("text.txt","w")
#print(h.readlines())
#print(h.read())

#h.write('BCVSHFHET')
#h.writelines(["bbcbh\n","jjjjj\n","kkkk\n"])

#j = open("text.txt","r")
#print(j.read())
#print(j.readlines())

def div(a,b):
    try:
        c = a/b
    except:
        print("除数不能为0")
        return
    return c
print(div(19,0))

#def operate_file():
 #   try:
#        g = open("text.txt",'w')
#    except:FileNotFoundError:
#        print("文件不存在")
#   except:ValueError:
#       print("文件已关闭")

a = open("D:\\python\\demo\day01\\text.txt",encoding='utf-8')
#print(a.readlines())
print(a.read())


