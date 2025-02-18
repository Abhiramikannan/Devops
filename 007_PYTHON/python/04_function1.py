#count function
String='''
I am an intern in UST, \nI wnt to become ceo of UST\t.We don\'t have have sat week off'''
print(String.count('m'))
print(String.count('ceo'))
print(String.endswith('off')) #instead of count,endswith return true/false
print('=================')
#expandtab
print(String.expandtabs(40))

print('===========================')
#find: return true/false
print(String.find('c'))
print('===========================')
String='abhirami'
print(String.find('abhirami'))