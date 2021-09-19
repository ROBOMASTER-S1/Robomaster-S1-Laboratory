# My Python Brush Ups:

condition=False
if condition:x=1
else:x=0
print(x)

condition=False
x=1 if condition else 0
print(x)

student={
'first_name':'Noyb','last_name':'Byon',
'Computer Science':['Programming','Robotics']}

print(student.get('first_name','Not Found:'))
print(student.get('last_name','Not Found:'))

for i in range(2):
        print(student.get('Computer Science')[i])

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
