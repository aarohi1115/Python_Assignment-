#Q2:

#5**9=1953125
#3//2=1
#7//3=2
#7/3=2.3333333333333335
#6==6 = True
#a=20; a+=30; a%=3; print(a) = 2
#True * False = 0
#True & False = False
#True and False = False
#((6>3) and (7<4) or(18==3)) and (9>3)
#True is False = False
#False in 'False' = error
#((True==False) or (False>True)) and (False<=True)

print("--------------------------------------------------------------------------")
#Q3:

s1="Nice to have it"
s2="here"
print(s1+" "+s2)

print("--------------------------------------------------------------------------")
#Q4:

a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
ind1=a[3]
ind2=ind1[1]
ind3=ind2[2]
ind=ind3[0]
print(ind)

print("--------------------------------------------------------------------------")
#Q5:

a.insert(0,s1)
a.append(s2)
print(a)

print("---------------------------------------------------------------------------")
#Q6:

numbers=[386,462,47,418,907,344,236,375,823,566,597,978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
print("Even Numbers :")
for i in numbers:
    if i%2==0:
        print(i)
    elif i==237:
        break

print("---------------------------------------------------------------------------")
#Q7:

color_list1=set(["White","Black","Red"])
color_list2=set(["Red","Green"])
print(color_list1.difference(color_list2))

print("--------------------------------------------------------------------------")
#Q8:

def check_Pangram(s):
    alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in alphabets:
        if c not in s.upper():
            return False
    return True
str=str(input("Enter a String : "))
if(check_Pangram(str)==True):
    print("The entered String is Pangram.")
else:
    print("The entered String is not a Pangram.")

print("---------------------------------------------------------------------------")
#Q9:

n=input("Enter a Number : ")
sum=int(n)+int(n*2)+int(n*3)
print("Output :",sum)

print("--------------------------------------------------------------------------")

#Q10:

inp = input("Enter the input:")
raw = inp.split("#")
for i in range(len(raw)):
    raw[i]=raw[i].split(" ")
rx=raw[0]
ry=raw[1]
x=[]
y=[]
for i in rx:
    x.append(int(i))
for i in ry:
    y.append(int(i))
print("x= ",x)
print("y= ",y)

print("--------------------------------------------------------------------------")

#Q11:

words=input("Enter words seperated with commas:")
words_list=words.split(",")
words_list.sort()
listToStr=','.join(words_list)
print("Final answer:", listToStr)

print("--------------------------------------------------------------------------")

#Q12

d={'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
students=d['Student']
marks=d['Marks']
max=max(marks)
i=marks.index(max)
print("Output:", students[i])

print("--------------------------------------------------------------------------")

#Q13
str_num = input("Input: ")
letters = 0
digits = 0
for i in str_num:
    if i.isalpha() == True:
        letters += 1
    if i.isdigit() == True:
        digits += 1
print("Number of letters: ", letters)
print("Number of digits: ", digits)

print("--------------------------------------------------------------------------")

#Q14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
name_1 = d['Name']
sub_1 = d['Subject']
ratings_1 = d['Ratings']
inp = input("Input: ")
a = []
b = []
c = []
count = sub_1.count(inp)
for i in range(count):
    x = sub_1.index(inp)
    a.append(name_1[x])
    b.append(sub_1[x])
    c.append(ratings_1[x])
    del name_1[x]
    del sub_1[x]
    del ratings_1[x]
new_data = dict()
new_data['Name'] = a
new_data['Subject'] = b
new_data['Ratings'] = c
print(new_data)

print("--------------------------------------------------------------------------")

#Q15
n = int(input("Enter an integer: "))
div_by_7 = [i for i in range(0, n) if (i % 7 == 0)]
print(div_by_7)

def div_checker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

div_checker(n)

print("--------------------------------------------------------------------------")

#Q16
import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")
        

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)

print("--------------------------------------------------------------------------")
