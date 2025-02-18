#print hello message
def hello_world(message):
    print(message)

hello_world("hai haali")

#sum of elements in the list
def hello_world(nums):
   sum=0
   for i in nums:
       sum+=i
   print(sum)

hello_world([5,4,3,2,1])

#prime or not
def check_prime(num):
    for i in range(2,num//2):
        if num%2==0:
            print("not prime")
            return
    print("prime")
check_prime(9)

#first repaeting number
def repeating_num(nums):
    dict = set()
    for i in nums:
        if i in dict:
            return i  # First repeating number
        else:
            dict.add(i)
print(repeating_num([1,2,3,4,1,1,3]))

