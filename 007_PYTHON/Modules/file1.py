def f(fname,lname):
    return fname+" "+lname

def sum2no(a,b):
    return a +b


person = {"fname":"prashanth",
          "age":21,
          "Aid":123456,
          "friends":["skc","ak"],
          "skills":{
              "backed_skills": ["nodejs", "ruby"],
              "database":["redis","mysql","postgress"]
          }
        }
person["address"]="mathura"
# print(person)
# print(person.get("skills").get("backed_skills"))
# print(person.get("address"))
# print("address" in person)
# print(person.pop("address"))
# print(len(person))
# del person["friends"]
# print(len(person))
# print(person["skills"]["backed_skills"])
# person["skills"]["database"].append("mongodb")
# print(person["skills"]["database"])
