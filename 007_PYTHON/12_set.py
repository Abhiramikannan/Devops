data_set = set()
for i in range(8,1,-1):
    data_set.add(i)

for i in data_set:
    # Pop an element and print it
    print(i)
data_set.pop()
print(len(data_set))  # This will print the length of the set, which should be 0 after popping all elements
