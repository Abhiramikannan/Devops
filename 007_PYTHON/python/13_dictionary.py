# person= {"first_name":"abhi","uid":290399,"friends":["abc","alu"],
#          "skills":{"backend":["python","java"]}}
# person["address"]="mathura"
# print(len(person))
# #print(person.get("skills").get("backend_skills"))#next line is or
# print(person["skills"]["backend"])
# person["skills"]["backend"].append("mongodb")
# print(person)
# #print(person.get("address"))
# print("address" in person)
# print(person.pop("address"))
# print(len(person))
# del person["friends"]
# print(len(person))

# print(person.items())
# person_copy=person.copy()
# del person
# print(person_copy)
# print(person_copy.keys())
# #key,get
# #get values out of dict:translation

# keys=person_copy.keys()
# for i in keys:
#     passif i=="address"
#     print(person_copy[i])
#     print("\n")

num=int(input("please enter the number"))
if num >10:
    print("num is greater than 10")
elif num <10:
    print("num is less than 10")
elif num <5:
    print("num is smaller than 10")
else:
    print("num out of range")