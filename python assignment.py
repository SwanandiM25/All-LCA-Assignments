#1st q
"""
my_dict={
    "Full Name":"Shradha Patil",
    "Age":19,
    "DOB":"2/8/2007",
    "Contact number":"xxxxxxxxx",
    "Address" : "A5 grand , sinhagad road pune"
 
}
my_dict["Student Email-id"]="shradha.patil@gmail.com"

my_dict.pop("Address")

print(my_dict)


#2nd q
key=["Full Name","Age","DOB","Contact number","Address" ]
values=["Shradha Patil",19,"02/08/2007","123456789","A5 grand , sinhagad road pune"]

result=dict(zip(key,values))

print("my dict=",result)

#3rd question 
my_dict={"name":"shradha","panel":"B","roll no":34,"marks":[65,87,67,94]}
print(sorted(my_dict))

#4th q
my_dict={"Full Name":"Shradha Patil",
    "Age":19,
    "DOB":"02/08/2007",
    "Contact number":"123456789",
    "Address" : "A5 grand , sinhagad road pune"}

print(list(my_dict.keys()))
print(list(my_dict.values()))

#5thq 
my_dict={"marks1":39,"marks2":45,"marks3":89,"marks4":67,"marks5":77}
print(my_dict.values())

mean=(sum(my_dict.values()))/len(my_dict)

print(mean)

#6th q
my_dict={'name':['Yash','Neel','Dev'],'roll no':[11,12,13],'marks':[78,56,98]}
print("name = ",my_dict['name'][2])
print("roll no =",my_dict['roll no'][1])
print("greatest marks = ",max(my_dict['marks']))


#7th q
s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print(freq)

#8th q
numerator=int(input("Enter numerator = "))
denominator=int(input("Enter denominator = "))

Remainder=numerator%denominator

Quotient=numerator/denominator

print(tuple((Remainder,Quotient)))

#9th q
d1=int(input("Enter day of first date: "))
m1=int(input("Enter month of first date: "))
y1=int(input("Enter year of first date: "))
date1=(d1, m1, y1)

d2=int(input("Enter day of second date: "))
m2=int(input("Enter month of second date: "))
y2=int(input("Enter year of second date: "))
date2=(d2, m2, y2)

days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Converting first date into number of days
total1= y1 * 365
for i in range(m1 - 1):
    total1 = total1 + days[i]

total1=total1 + d1

#Converting second date into number of days
total2= y2 * 365
for i in range(m2 - 1):
    total2 = total2 + days[i]

total2=total2 + d2

difference = total2 - total1

if difference < 0:
    difference=-difference

print("Number of days between the dates =", difference)
"""


