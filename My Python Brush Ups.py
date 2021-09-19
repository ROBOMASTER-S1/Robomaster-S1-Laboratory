# My Python Brush Ups!

condition=False
if condition:x=1
else:x=0
print(x)

condition=False
x=1 if condition else 0
print(x)

first_name='first name'
last_name='last name'
first='Noyb';last='Byon'
dream_job='Computer Science'
program='Programming'
robot='Robotics'
not_found='Not Found:'

student={
first_name:first,last_name:last,
dream_job:[program,robot]}

print(student.get(first_name,not_found))
print(student.get(last_name,not_found))

for i in range(2):
        print(student.get(dream_job)[i])

name_index=['Rob','Bob','Tom']
for i, name_index in enumerate(name_index,start=1):
        print(i,name_index)

fname_index=['Rob','Bob','Tom']
lname_index=['Small','Ball','Tall']

for i,j in enumerate(fname_index):
        person=lname_index[i]
        print(f'{j} {person}')

for i,j in zip(fname_index,lname_index):
        print(f'{i} {j}')

dictionary={1:'One',2:'Two',3:'Three'}
for key,dictionary in dictionary.items():
        print('Key',key,'is',dictionary,'.')

Scientist=[
'Stephen Hawking','Albert Einstein',
'Isaac Newton','Galileo Galilei']

Profession=[
'Theoretical Physicist and Cosmologist',
'Theoretical Physicist','Mathematician, Physicist, \
Astronomer and Theologian','Astronomer, \
Physicist and Engineer']

college_university=['Cambridge',
'Eth Zurich',"The King's School",'Pisa']

for s,p,cu in zip(Scientist,Profession,college_university):
        print(f'{s} is {p} and went to {cu}')
