#整数
a = 1
print (type(a))
#小数
b = 2.22
print(type(b))
#字符串
c = "杨云飞"
print(type(c))
d = '杨云飞'
print(type(d))

e = ''''''
print(type(e))
f = """杨云飞"""
print(type(f))
#list列表
l = [2,3,4,5]
print(l)
print(type(l))
l[3] = 3
print(l)
print(type(l))
l[3] = 8
print(l)
#tupie元组
t = (1,)
print(t)
print(type(t))
#字典
d = {'name':'杨云飞','年龄':24}
print(d)
print(type(d))
y = 514
x = 452
print(y+x)
print(y*x)
print(y/x)
print(x%y)
print(y*x-y)

g = [3,4,5,6,7]
g[3] = 5
print(1 > 0)
print(1 != 0)
a = 1
b = 200
print(1 > 200)
print(1 != 2)
a = 'dfhdfn'
print('df' in a)
b = [1,2,3,5,6,]
print(2 in b)
c = {'name':"杨云飞",'sex':'女'}
print('name' in c)
print('sex' in c)
a = 'xxxxx'
b = 'xxxxx'
print(a == b)
# 80 以上优秀  60-80良好 60以下差
a = 75
if(a >= 80):
    print('小明成绩为优秀')
if(a >= 60 and a < 80):
    print('小明成绩为良好')
if(a < 60):
    print('小明成绩为差')
if(a >= 80):
    print('小明成绩为优秀')
elif(a >= 60):
    print('小明成绩为良好')
else:
    print('小明成绩为差')
if(a >= 80):
    print('小明成绩为优秀')
if(a >= 60 and a < 80):
    print('小明成绩为良好')
if(a < 60):
    print('小明成绩为差')
if(a >= 80):
    print('小明成绩为优秀')
elif(a >= 60):
    print('小明成绩为良好')
else:
    print('小明成绩为差')
for i in range(1,100,2):
    print(i)
for i in range(100):
    if(i == 5):
      break
    print(i)
for i in range(100):
    if(i%5==0):
        continue
    print(i)
for i in range(1,100):
    if(i == 5):
        break
    print(i)
for i in range(1,100):
if(i%5==0):
continue
print(i)
for i in range(100):
    if(i%2==0):
    point(i)
    

for i in range(1,101):
    if (i%2 == 1):
        print(i)

s = 0
for i in range(1,11):
    s += i
    print(s)


for i in range(1,101):
    s *= i
print(s)

s = 0
for i in range(1,101):
    s += i
    print(s)
