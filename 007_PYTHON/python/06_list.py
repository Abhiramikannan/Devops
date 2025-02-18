list=["apple","orange","grapes","mango","avacado"]
list.sort()
print(list)

#using function
def sort_list(fruits):
    fruits.sort(reverse=True)#reverse sort
    print(fruits)
    return sorted(fruits)

fruits=["apple","orange","grapes","mango","avacado"]
print(sort_list(fruits))

#diff b/w sort and sorted
