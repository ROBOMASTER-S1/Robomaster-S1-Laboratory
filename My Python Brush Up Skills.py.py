# My Python Brush Up Skills:


# Easy Counting Python Program Example:

say=('Enter any mumber and I will count to it \
for you right on the spot: ',' I just counted to ')
error=('Sorry! Positive numbers only please...',
"Sorry Hero! Zero doesn't count...",
'Sorry! Numbers only please...')
spacer=','

while True:
    try:
        number=int(input(say[0]).strip())
        if number<-number:
            print(error[0])
            continue
        elif number==0:
            print(error[1])
            continue
        for i in range(1,number):
            print(i,end=spacer)
            if i==number:
                pass
        print(say[1]+str(number)+':')
        break
    except ValueError:
        print(error[2])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Easy Dictionary Python Program Example:

get_value={
    0:'Button Zero: was pressed.',1:'Button One: was pressed.',
    2:'Button Two: was pressed.',3:'Button Thre: was pressed.',
    4:'Button Four: was pressed.',5:'Button Five: was pressed.',
    6:'Button Six: was pressed.',7:'Button Seven: was pressed.',
    8:'Button Eight: was pressed.',9:'Button Nine: was pressed.'}

say=('Press a number button: ','button: Not Found!')
error=('Sorry! Positive numbers only please...',
'Sorry! Numbers only please...')

while True:
    try:
        button=int(input(say[0]).strip())
        if button<-button:
            print(error[0])
            continue
        print(get_value.get(button,f'{button} '+say[1]),end=' ')
        break
    except ValueError:
        print(error[1])
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
condition=False
if condition:x=1
else:x=0
print(x)

condition=False
x=1 if condition else 0
print(x)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
dictionary={1:'One',2:'Two',3:'Three'}
for key,dictionary in dictionary.items():
        print('Key',key,'is',dictionary,'.')
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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
