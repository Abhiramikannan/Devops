MultilineString='''
I am an intern in UST,
I wnt to become ceo of UST.
'''

print(MultilineString)

#concatination

Fname='Abhi'
Lname='rami'
print(Fname+' '+Lname)
print(len(Fname+' '+Lname))


String='''
I am an intern in UST, \nI wnt to become ceo of UST\t.We don\'t have have sat week off

'''
print(String)

#print area of circle
pi=22/7
r=3
circle_area=pi*r**2
print(circle_area)

#print table
num=2
for i in range(1,10):
    print(str(num) + '*' + str(i) + '=' + str(num * i))
     #or
    #print(f"{num}*{i}={num * i}")

#accessing string
length=len(String)
for i in range(1,length):
    print(String[i])

length=len(String)*-1
print(length)
for i in range(-1,length,-2):
    print(String[i])
print('=======================')
#slicing
String="abhiramikannan"
FirstThreeChar=String[0:3]
print(FirstThreeChar)
print('========================')
FirstThreeChar=String[::3]#skips 3 and print ..0 
print(FirstThreeChar)
print('========================')
FirstThreeChar=String[::-1]
print(FirstThreeChar)
print('========================')
FirstThreeChar=String[-3:]
print(FirstThreeChar)
print('========================')
FirstThreeChar=String[3:]
print(FirstThreeChar)
print('========================')
FirstThreeChar=String[0:10:2] #skip 1 go to next
print(FirstThreeChar)

#count:num of occurances of substring