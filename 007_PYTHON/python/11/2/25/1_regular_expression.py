import re
string= "Good Good morning all"
match=re.search("morning",string,re.I)
# match=re.findall("all",string,re.I)
# match=re.match("morning",string,re.I)
#re.match(): This function checks if the pattern
#  matches at the beginning of the string, not anywhere. 
# re.findall(): This function would return a list of all non-overlapping matches of the pattern in the string. 
# But it's commented out, so it's not being executed.
# re.search() searches through the entire string and
# returns the first match it finds for the given pattern.
print(match)
''' if match:
    print(match.group(0))'''
# Find all occurrences of 'morning' (case-insensitive)
match1=re.findall("(?i)morning",string)
print(match1)
# Find 'good.morning' (case-insensitive and allow '.' to match any character including newlines)
match2=re.findall("good.morning",string,re.I | re.DOTALL)#dot prints ecerything
print(match2)
match3=re.search("good.morning",string,re.I | re.DOTALL)
#.=any single charec....here space
#dotall=any single charecter+new line..here no new line
myspan=match3.span()
print(myspan)
#.span() is a method that returns a tuple representing the start
#and end indices of the matched string in the original string.

l=[]
for i in re.finditer(re.escape("Good"),string):  #need to give the crct word in string..case sensitive
      print(i)
      l.append(i.span())
print(l)

#to check case insensitive
l = []
for i in re.finditer(re.escape("Good"), string, re.I):  # Add re.I for case-insensitive search
    print(i)
    l.append(i.span())
print(l)

# match4=re.sub("[Gg]ood","Awesome",string,re.IGNORECASE)
match4=re.sub("(?i)Good","Awesome",string)
print(match4)
print(string)  

string1='''Hi
Welcome
Hello '''
match5=re.split("\n",string1)#check everyline 

print(match5)

pattern=r'[G].*'#from g it prints all
                # 0 or 1 tym=.?
match6=re.findall(pattern,string)
print(match6)

pattern=r'[d].*[r]'#from first d to last r
         
match6=re.findall(pattern,string)
print(match6)