s="hello how r u doing"
x=s.index("r")
print(x)

x=s.index("u",11)#search start from this index
print(x)

sh="abhirami123"
print(sh.isalnum())#no spaces to check alphanumeric(letters+num)
print(sh.isalpha())

a="2789"
print(a.isalpha())

b="\u00b2"

print(b.isdecimal())
print(b.isdigit())
print(b.isnumeric())
c="10.5"
print(c.isdigit())
print(c.isnumeric())
s5 = "Ⅻ"  # Roman numeral for 12
print(s5.isnumeric())  # True (Roman numerals are considered numeric)
print('============')
s4="10\u00b2"#equivalent to 10^2
print(s4.isdecimal())
print(s4.isdigit())
print(s4.isnumeric())
print('===============')
s6="10\u00bd"
print(s6.isdecimal())
print(s6.isdigit())
print(s6.isnumeric())
print('===============')
print(s4.isidentifier()) 
print('==================')
a1="hi all"
a2=["hi","how","are","you"]
print(a1.islower())#true/false
print("?".join(a2))
print('=================')
a3=(" ".join(a2))
print(a3.strip("ha"))#remove ha only begining and end
print('=====================')


#split
print(a3.split(" "))

#title:first letter capital
print('=====================')
print(a3.title())

#swapcase : uppercase
print('=================')
print(a3.swapcase())

#replace
print('=================')
print(a3.replace("how","hello"))
print(a3.startswith("hi"))


#usecases
s1="devops"
s2="batch"
s3="2"
s=s1+s2+s3
print(s)
print(len(s))
print(s.upper().find("B"))
print(s[1:])
s=s1+" "+s2+" "+s3
print(s.split()[0])
print(s[len(s)-1])
print(s.index(s[-1]))
print(s.index("b"))
