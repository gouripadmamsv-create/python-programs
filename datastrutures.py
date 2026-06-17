'''#tuple
tuple1=(10,20,30,40)
print(tuple1)
nested_tuple=((4,5,6,7),20,"gouri","tvm")
print(nested_tuple)
                       
 #try out immutability
person=("gouri",20,"tvm")
name,age,place=person
print(name) 
print(age)
print(place)


number=(10,20,30,40,50)
#a=10 b=20 c=30 40 50
a,b,*c=number
print(a)
print(b)
print(c)

d,*e,f=number
print(d)
print(e)
print(f)

value=(2,3,2,4,5,6,2,4,6,4,6,6,4)
print(len(value))
print(value.count(2))
print(value.count(4))
print(value.index(3))
print(value[3])

userdata=input("enter a string")
count=0
for item in userdata:
    count+=1
print(count)   

#first non repeating character in a string
#print("the first non repeating character in a string")
user_input=input("enter a string")
count=0
for item in user_input:
    if user_input.count(item)==1:
        print("first non repeating character",item)
        break
else:
        print("there is no non repeating character")'''


#set
student1={"english","malayalam","hindi"}
student2={"tamil","hindi","english"}
student3={"telugu","tamil","kannada"}
student1.add("tamil")
print(student1)
student1.update(["java","css"])
print(student1)
student2.add("java")
print(student2)
#print(student1)

student1.add("malayalam")
print(student1)

student1.remove("hindi")
print(student1)
# student1.remove("german")
#print(student1)
student1.discard("german")
print(student1)


students1={"English","Hindi","Malyalam"}
students2={"English","Hindi","german"}
students3={"English","Korean","Malyalam"}